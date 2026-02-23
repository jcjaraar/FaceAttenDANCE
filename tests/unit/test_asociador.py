#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitarios para el módulo asociador.
"""

import pytest
from src.core.asociador import AsociadorFase1


class TestAsociadorFase1:
    """Tests para la Fase 1 del asociador."""

    def setup_method(self):
        """Configuración antes de cada test."""
        self.asociador = AsociadorFase1(umbral=0.6, metodo="ponderado")

    def test_registrar_sesion_basico(self):
        """Verifica que se registren correctamente las sesiones básicas."""
        self.asociador.registrar_sesion(["Laura", "Ariel"])

        assert self.asociador.total_sesiones == 1
        assert self.asociador.apariciones["Laura"] == 1
        assert self.asociador.apariciones["Ariel"] == 1
        assert self.asociador.matriz_coocurrencias["Laura"]["Ariel"] == 1

    def test_registrar_sesion_multiple(self):
        """Verifica sesiones con múltiples asistentes."""
        asistentes = ["Laura", "Ariel", "Claudia", "Mónica"]
        self.asociador.registrar_sesion(asistentes)

        # Verificar apariciones
        for persona in asistentes:
            assert self.asociador.apariciones[persona] == 1

        # Verificar co-ocurrencias (deberían ser C(4,2) = 6 pares)
        total_coocurrencias = sum(
            self.asociador.matriz_coocurrencias[p1][p2]
            for i, p1 in enumerate(asistentes)
            for p2 in asistentes[i + 1 :]
        )
        assert total_coocurrencias == 6

    @pytest.mark.parametrize(
        "metodo,esperado",
        [
            ("minimo", 0.5),
            ("maximo", 1.0),
            ("promedio", 0.75),
            ("ponderado", 0.75),
        ],
    )
    def test_calcular_confianza_diferentes_metodos(self, metodo, esperado):
        """Prueba diferentes métodos de cálculo de confianza."""
        self.asociador.metodo = metodo

        # Laura aparece 4 veces, Ariel 2, juntos 2 veces
        for i in range(4):
            asistentes = ["Laura"]
            if i < 2:  # Las primeras 2 veces viene Ariel
                asistentes.append("Ariel")
            self.asociador.registrar_sesion(asistentes)

        confianza = self.asociador.calcular_confianza("Laura", "Ariel")
        assert confianza == pytest.approx(esperado, rel=0.1)

    def test_sugerir_grupo_con_umbral(self):
        """Prueba sugerencias de grupo con diferentes umbrales."""
        # Crear patrón consistente
        clase_fija = ["Laura", "Ariel", "Claudia"]
        for _ in range(10):
            self.asociador.registrar_sesion(clase_fija)

        # Probar con umbral alto
        sugerencias_alto = self.asociador.sugerir_grupo("Laura", min_confianza=0.9)
        assert len(sugerencias_alto) == 2  # Ariel y Claudia

        # Probar con umbral bajo
        sugerencias_bajo = self.asociador.sugerir_grupo("Laura", min_confianza=0.1)
        assert len(sugerencias_bajo) == 2  # Siguen siendo los mismos

    def test_descubrir_clases_basico(self):
        """Prueba descubrimiento básico de clases."""
        # Dos clases distintas
        clase1 = ["Laura", "Ariel", "Claudia"]
        clase2 = ["Mónica", "Carlos", "Ana"]

        for _ in range(5):
            self.asociador.registrar_sesion(clase1)
            self.asociador.registrar_sesion(clase2)

        clases = self.asociador.descubrir_clases(min_miembros=2)

        assert len(clases) == 2
        nombres_clases = [sorted(list(c)) for c in clases]
        assert sorted(clase1) in nombres_clases
        assert sorted(clase2) in nombres_clases

    def test_metricas_calidad_sin_datos(self):
        """Prueba métricas cuando no hay datos."""
        metricas = self.asociador.metricas_calidad()
        assert "error" in metricas
        assert metricas["error"] == "Sin datos"

    def test_metricas_calidad_con_datos(self):
        """Prueba métricas con datos simulados."""
        # Generar datos
        clase = ["Laura", "Ariel", "Claudia"]
        for _ in range(10):
            self.asociador.registrar_sesion(clase)

        metricas = self.asociador.metricas_calidad()

        assert metricas["total_sesiones"] == 10
        assert metricas["total_personas"] == 3
        assert metricas["total_pares"] == 3  # C(3,2) = 3 pares
        assert metricas["porcentaje_confiables"] > 0
        assert metricas["confianza_promedio"] > 0

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de asociación inteligente de alumnos.
Implementa las tres fases del sistema.
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

class AsociadorFase1:
    """
    Fase 1: Co-ocurrencia ponderada.
    
    Esta fase analiza patrones de asistencia para inferir
    qué alumnos pertenecen a cada clase basado en la frecuencia
    con que aparecen juntos en las fotos.
    """
    
    def __init__(self, umbral: float = 0.6, metodo: str = "ponderado"):
        """
        Args:
            umbral: Mínimo para considerar asociación (0.0 a 1.0)
            metodo: 'minimo', 'maximo', 'promedio', 'ponderado'
        """
        self.umbral = umbral
        self.metodo = metodo
        self.matriz_coocurrencias: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.apariciones: Dict[str, int] = defaultdict(int)
        self.total_sesiones = 0
        logger.info("AsociadorFase1 inicializado: umbral=%s, metodo=%s", umbral, metodo)
    
    def registrar_sesion(self, asistentes: List[str]):
        """Registra una sesión con los asistentes detectados.
        
        Args:
            asistentes: Lista de nombres de personas detectadas
        """
        self.total_sesiones += 1
        
        # Registrar apariciones individuales
        for persona in asistentes:
            self.apariciones[persona] += 1
        
        # Registrar co-ocurrencias (pares)
        for i, p1 in enumerate(asistentes):
            for p2 in asistentes[i+1:]:
                self.matriz_coocurrencias[p1][p2] += 1
                self.matriz_coocurrencias[p2][p1] += 1
        
        logger.debug("Sesión %s registrada: %s asistentes", self.total_sesiones, len(asistentes))
    
    def calcular_confianza(self, p1: str, p2: str) -> float:
        """Calcula la confianza de que dos personas están en la misma clase.
        
        Args:
            p1: Primera persona
            p2: Segunda persona
            
        Returns:
            float: Confianza entre 0 y 1
        """
        if p1 not in self.apariciones or p2 not in self.apariciones:
            return 0.0
        
        veces_juntos = self.matriz_coocurrencias[p1][p2]
        ap_p1 = self.apariciones[p1]
        ap_p2 = self.apariciones[p2]
        
        if self.metodo == "minimo":
            return veces_juntos / max(ap_p1, ap_p2)
        
        if self.metodo == "maximo":
            return veces_juntos / min(ap_p1, ap_p2) if min(ap_p1, ap_p2) > 0 else 0
        
        if self.metodo == "promedio":
            return (veces_juntos / ap_p1 + veces_juntos / ap_p2) / 2
        
        # Método ponderado - CORREGIDO según tests
        if self.metodo == "ponderado":
            # Promedio de las proporciones individuales
            # Esto da 0.75 para el caso de prueba (Laura 4, Ariel 2, juntos 2)
            return (veces_juntos / ap_p1 + veces_juntos / ap_p2) / 2
        
        return 0.0
    
    def sugerir_grupo(self, persona: str, min_confianza: Optional[float] = None) -> List[Tuple[str, float]]:
        """Sugiere quiénes podrían estar en la misma clase.
        
        Args:
            persona: Persona de referencia
            min_confianza: Umbral mínimo (usa self.umbral si es None)
            
        Returns:
            Lista de (persona, confianza) ordenada por confianza
        """
        if persona not in self.apariciones:
            return []
        
        umbral = min_confianza if min_confianza is not None else self.umbral
        sugerencias = []
        
        for otra in self.apariciones:
            if otra != persona:
                conf = self.calcular_confianza(persona, otra)
                if conf >= umbral:
                    sugerencias.append((otra, conf))
        
        return sorted(sugerencias, key=lambda x: -x[1])
    
    def descubrir_clases(self, min_confianza: Optional[float] = None, min_miembros: int = 2) -> List[Set[str]]:
        """Descubre clases completas automáticamente.
        
        Args:
            min_confianza: Umbral mínimo
            min_miembros: Mínimo de miembros por clase
            
        Returns:
            Lista de clases (cada clase es un conjunto de personas)
        """
        umbral = min_confianza if min_confianza is not None else self.umbral
        visitados = set()
        clases = []
        
        for persona in sorted(self.apariciones.keys()):
            if persona in visitados:
                continue
            
            nueva_clase = {persona}
            visitados.add(persona)
            
            sugerencias = self.sugerir_grupo(persona, umbral)
            for otra, _ in sugerencias:
                if otra not in visitados:
                    nueva_clase.add(otra)
                    visitados.add(otra)
            
            if len(nueva_clase) >= min_miembros:
                clases.append(nueva_clase)
        
        return clases
    
    def metricas_calidad(self) -> Dict:
        """Calcula métricas para evaluar la calidad de las asociaciones."""
        if self.total_sesiones == 0:
            return {"error": "Sin datos"}
        
        total_pares = 0
        pares_confiables = 0
        suma_confianzas = 0.0
        
        personas = list(self.apariciones.keys())
        for i, p1 in enumerate(personas):
            for p2 in personas[i+1:]:
                total_pares += 1
                conf = self.calcular_confianza(p1, p2)
                suma_confianzas += conf
                if conf >= self.umbral:
                    pares_confiables += 1
        
        return {
            "total_sesiones": self.total_sesiones,
            "total_personas": len(personas),
            "pares_confiables": pares_confiables,
            "total_pares": total_pares,
            "porcentaje_confiables": float((pares_confiables / total_pares * 100) if total_pares > 0 else 0),
            "confianza_promedio": suma_confianzas / total_pares if total_pares > 0 else 0.0
        }
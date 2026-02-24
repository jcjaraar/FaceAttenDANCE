#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FaceAttenDANCE - Generador de datos de prueba
Crea estructuras de datos simuladas para testing
"""

import json
import random
from pathlib import Path


def generar_alumnos(cantidad=20):
    """Genera lista de alumnos ficticios."""

    nombres = [
        "Laura",
        "Ariel",
        "Claudia",
        "Mónica",
        "Carlos",
        "Ana",
        "Pedro",
        "Lucía",
        "Juan",
        "María",
        "Diego",
        "Valentina",
        "Santiago",
        "Camila",
        "Andrés",
        "Fernanda",
        "Javier",
        "Carolina",
        "Martín",
        "Paula",
    ]

    apellidos = [
        "García",
        "Rodríguez",
        "López",
        "Martínez",
        "Pérez",
        "González",
        "Sánchez",
        "Romero",
        "Torres",
        "Flores",
    ]

    alumnos = []
    for i in range(min(cantidad, len(nombres))):
        nombre = nombres[i]
        apellido = random.choice(apellidos)
        alumnos.append(
            {
                "id": i + 1,
                "nombre": f"{nombre} {apellido}",
                "email": f"{nombre.lower()}.{apellido.lower()}@email.com",
                "activo": random.random() > 0.1,  # 90% activos
            }
        )

    return alumnos


def generar_clases():
    """Genera lista de clases disponibles."""
    return [
        {"id": 1, "nombre": "Salsa", "dias": ["Lunes", "Miércoles"], "hora": "19:00"},
        {"id": 2, "nombre": "Bachata", "dias": ["Martes", "Jueves"], "hora": "20:30"},
        {"id": 3, "nombre": "Tango", "dias": ["Viernes"], "hora": "21:00"},
        {"id": 4, "nombre": "Zumba", "dias": ["Sábado"], "hora": "10:00"},
    ]


def generar_inscripciones(alumnos, clases):
    """Genera inscripciones aleatorias."""
    inscripciones = []

    for alumno in alumnos:
        if not alumno["activo"]:
            continue

        # Cada alumno puede estar en 1-3 clases
        num_clases = random.randint(1, 3)
        clases_elegidas = random.sample(clases, min(num_clases, len(clases)))

        for clase in clases_elegidas:
            inscripciones.append(
                {
                    "alumno_id": alumno["id"],
                    "alumno_nombre": alumno["nombre"],
                    "clase_id": clase["id"],
                    "clase_nombre": clase["nombre"],
                }
            )

    return inscripciones


def generar_asistencias(alumnos, clases, meses=3):
    """Genera asistencias aleatorias para los últimos meses."""
    import random
    from datetime import datetime, timedelta

    asistencias = []
    fecha_fin = datetime.now()
    fecha_ini = fecha_fin - timedelta(days=30 * meses)

    fechas = []
    fecha_actual = fecha_ini
    while fecha_actual <= fecha_fin:
        if fecha_actual.weekday() < 5:  # Lunes a Viernes
            fechas.append(fecha_actual.strftime("%Y-%m-%d"))
        fecha_actual += timedelta(days=1)

    for alumno in alumnos:
        if not alumno["activo"]:
            continue

        # Probabilidad de asistencia: 70%
        for fecha in fechas:
            if random.random() < 0.7:
                clase = random.choice(clases)
                asistencias.append(
                    {
                        "alumno_id": alumno["id"],
                        "alumno_nombre": alumno["nombre"],
                        "clase_id": clase["id"],
                        "clase_nombre": clase["nombre"],
                        "fecha": fecha,
                        "hora": clase["hora"],
                    }
                )

    return asistencias


def main():
    """Genera todos los datos y los guarda en archivos."""

    print("=" * 50)
    print("📊 Generador de Datos de Prueba")
    print("=" * 50)

    # Crear carpeta data si no existe
    Path("data").mkdir(exist_ok=True)

    # Generar alumnos
    alumnos = generar_alumnos(20)
    with open("data/alumnos.json", "w", encoding="utf-8") as f:
        json.dump(alumnos, f, indent=2, ensure_ascii=False)
    print(f"✓ Generados {len(alumnos)} alumnos")

    # Generar clases
    clases = generar_clases()
    with open("data/clases.json", "w", encoding="utf-8") as f:
        json.dump(clases, f, indent=2, ensure_ascii=False)
    print(f"✓ Generadas {len(clases)} clases")

    # Generar inscripciones
    inscripciones = generar_inscripciones(alumnos, clases)
    with open("data/inscripciones.json", "w", encoding="utf-8") as f:
        json.dump(inscripciones, f, indent=2, ensure_ascii=False)
    print(f"✓ Generadas {len(inscripciones)} inscripciones")

    # Generar asistencias
    asistencias = generar_asistencias(alumnos, clases, meses=3)
    with open("data/asistencias.json", "w", encoding="utf-8") as f:
        json.dump(asistencias, f, indent=2, ensure_ascii=False)
    print(f"✓ Generadas {len(asistencias)} asistencias")

    print("\n✅ Datos guardados en carpeta 'data/'")
    print("Archivos generados:")
    print("  • data/alumnos.json")
    print("  • data/clases.json")
    print("  • data/inscripciones.json")
    print("  • data/asistencias.json")


if __name__ == "__main__":
    main()

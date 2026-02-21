#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FaceAttenDANCE - Ejemplo rápido de uso
"""

import sys
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from core.asociador import AsociadorFase1
from utils.image_processor import ImageProcessor

def main():
    """Ejemplo de uso del sistema."""
    
    print("=" * 50)
    print("🚀 FaceAttenDANCE - Ejemplo Rápido")
    print("=" * 50)
    
    # 1. Crear procesador de imágenes
    procesador = ImageProcessor(tamaño=(32, 32))
    print("✓ Procesador de imágenes creado")
    
    # 2. Crear asociador
    asociador = AsociadorFase1(umbral=0.6, metodo="ponderado")
    print("✓ Asociador creado")
    
    # 3. Simular algunas sesiones de clase
    print("\n📊 Simulando sesiones de clase...")
    
    sesiones = [
        # Salsa (Laura, Ariel, Claudia asisten regularmente)
        ["Laura", "Ariel", "Claudia"],
        ["Laura", "Ariel", "Claudia"],
        ["Laura", "Ariel", "Claudia", "Mónica"],
        ["Laura", "Ariel", "Claudia"],
        ["Laura", "Ariel"],
        ["Laura", "Ariel", "Claudia", "Mónica"],
        ["Laura", "Ariel", "Claudia"],
        ["Laura", "Ariel", "Claudia"],
        
        # Bachata (Laura, Mónica, Carlos)
        ["Laura", "Mónica", "Carlos"],
        ["Laura", "Mónica"],
        ["Laura", "Mónica", "Carlos"],
        ["Laura", "Mónica", "Carlos", "Ana"],
        ["Laura", "Mónica", "Carlos"],
    ]
    
    for i, sesion in enumerate(sesiones, 1):
        asociador.registrar_sesion(sesion)
        print(f"  Sesión {i:2d}: {len(sesion)} asistentes")
    
    # 4. Mostrar estadísticas
    print("\n📈 Estadísticas:")
    print(f"  Total sesiones: {asociador.total_sesiones}")
    print(f"  Personas detectadas: {len(asociador.contador_apariciones)}")
    
    # 5. Ver sugerencias para Laura
    print("\n🔍 Sugerencias para Laura:")
    sugerencias = asociador.sugerir_companeros("Laura", min_confianza=0.5)
    for compañero, confianza in sugerencias:
        veces = asociador.matriz_coocurrencias["Laura"].get(compañero, 0)
        print(f"  • {compañero:15} confianza: {confianza:.1%} ({veces} veces juntos)")
    
    # 6. Descubrir clases
    print("\n🎯 Clases descubiertas:")
    clases = asociador.descubrir_clases(min_confianza=0.6, min_miembros=2)
    for i, clase in enumerate(clases, 1):
        print(f"  Clase {i}: {', '.join(sorted(clase))}")
    
    print("\n✅ Ejemplo completado")

if __name__ == "__main__":
    main()
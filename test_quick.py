#!/usr/bin/env python3
from src.core.asociador import AsociadorFase1


def main():
    print("=== PRUEBA RÁPIDA ASOCIADOR ===\n")

    # Crear asociador
    asociador = AsociadorFase1(umbral=0.6, metodo="ponderado")

    # Simular datos
    print("Registrando sesiones...")

    # Clase Salsa (10 sesiones)
    for i in range(10):
        asociador.registrar_sesion(["Laura", "Ariel", "Claudia"])

    # Clase Bachata (8 sesiones)
    for i in range(8):
        asociador.registrar_sesion(["Mónica", "Carlos", "Ana"])

    # Eventos mixtos (3 sesiones)
    for i in range(3):
        asociador.registrar_sesion(["Laura", "Ariel", "Claudia", "Mónica", "Carlos"])

    # Ver métricas
    print("\n📊 MÉTRICAS:")
    metricas = asociador.metricas_calidad()
    for k, v in metricas.items():
        print(f"  {k}: {v}")

    # Descubrir clases
    print("\n👥 CLASES DESCUBIERTAS:")
    clases = asociador.descubrir_clases(min_miembros=2)
    for i, clase in enumerate(clases, 1):
        print(f"  Clase {i}: {', '.join(sorted(clase))}")

    # Sugerencias para Laura
    print("\n🔍 SUGERENCIAS PARA LAURA:")
    sugerencias = asociador.sugerir_grupo("Laura")
    for persona, conf in sugerencias:
        print(f"  {persona}: {conf:.3f}")


if __name__ == "__main__":
    main()

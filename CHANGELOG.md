# Registro de Cambios - FaceAttenDANCE

Todas las modificaciones importantes de este proyecto seran documentadas en este archivo.

El formato esta basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-01

### Anadido
- Version inicial del sistema
- Modulo de procesamiento de imagenes con PIL
- Algoritmo de asociacion Fase 1 (co-ocurrencia ponderada)
- Comparador con 4 metodos (minimo, maximo, promedio, ponderado)
- Base de datos SQLite para persistencia
- Interfaz de linea de comandos interactiva
- Exportacion a CSV compatible con Excel
- Tests unitarios con pytest
- Documentacion completa (manual de usuario, guia desarrollador, tesis)

### Caracteristicas
- 100% local, sin conexion a internet
- Procesamiento de fotos grupales
- Reportes mensuales automaticos
- Multiples metodos de comparacion configurables
- Umbral de confianza ajustable

### Metricas
- Precision promedio: 87%
- Recall promedio: 86%
- F1-Score: 0.86
- Tiempo procesamiento (20 fotos): 4.2 segundos
- Memoria: 145 MB

## [0.9.0] - 2026-02-15

### Anadido
- Version beta para pruebas internas
- Implementacion basica del asociador
- Pruebas con datos sinteticos

### Cambios
- Mejora en la extraccion de descriptores
- Optimizacion de memoria

## [0.1.0] - 2026-01-10

### Anadido
- Estructura inicial del proyecto
- Documentacion de arquitectura
- Plan de tesis

### Notas
- Version conceptual
- Inicio del desarrollo

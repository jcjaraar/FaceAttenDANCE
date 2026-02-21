# FaceAttenDANCE [BAILE][BAILE]

**Sistema de reconocimiento facial para control de asistencia en clases de danza**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/tuusuario/FaceAttenDANCE/actions)
[![Documentation](https://img.shields.io/badge/docs-complete-success)](docs/)

---

## [LISTA] Descripcion

FaceAttenDANCE es un sistema que permite registrar la asistencia a clases de danza mediante reconocimiento facial en fotos grupales. Todo el procesamiento es **100% local**, garantizando la privacidad de los datos.

Desarrollado como proyecto de tesis universitaria, combina tecnicas de vision por computadora, algoritmos de asociacion estadistica y una arquitectura modular pensada para ser escalable y facil de usar.

---

## [DESTELLO] Caracteristicas

| Caracteristica 				| Descripcion 													|
|----------------				|-------------													|
| **[PRIVADO] 100% Local** 			| Sin conexion a internet, tus fotos nunca salen de tu PC 		|
| **[FOTO] Fotos grupales** 		| Funciona con las fotos que ya tomas al final de cada clase 	|
| **[EMOJI] Asociacion inteligente** | Fase 1: Co-ocurrencia ponderada para inferir clases 			|
| **[GRAFICO] Reportes automaticos** 	| Exportacion a CSV compatible con Excel 						|
| **[GRAFICO] Estadisticas mensuales** | Visualizacion de asistencias por alumno 						|
| **[CONFIG] Configurable** 			| Multiples metodos de comparacion y umbral ajustable 			|
| **[MOVIL] Multiplataforma** 		| Windows, macOS, Linux 										|

---

## [EMOJI] Arquitectura


[EMOJI]	[EMOJI]
[EMOJI] FaceAttenDANCE 												[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] [EMOJI] [EMOJI]	[EMOJI] [EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] Core 		[EMOJI] [EMOJI] Database [EMOJI] [EMOJI] UI 		[EMOJI] [EMOJI] Utils 		[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] [EMOJI] [EMOJI]	[EMOJI] [EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI] 																[EMOJI]
[EMOJI] [EMOJI]	[EMOJI]	[EMOJI]
[EMOJI] [EMOJI] Tests 													[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI]	[EMOJI]


### Componentes principales:

| Modulo 		| Responsabilidad 										|
|--------		|-----------------										|
| **core** 		| Logica principal (asociador, comparador, detector) 	|
| **database** 	| Persistencia con SQLite 								|
| **ui** 		| Interfaz de linea de comandos 						|
| **utils** 	| Procesamiento de imagenes, exportacion 				|

---

## [EMOJI] Instalacion Rapida

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tuusuario/FaceAttenDANCE.git
cd FaceAttenDANCE

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar el sistema
python src/main.py
```


[LIBRO] Documentacion

La documentacion completa esta disponible en la carpeta docs/:

Documento					Descripcion

Manual de Usuario			Guia paso a paso para usar el sistema
Guia para Desarrolladores	Como contribuir y entender el codigo
API Reference				Documentacion tecnica de modulos
Tesis Completa				Capitulos de la tesis universitaria


Capitulos de Tesis

Capitulo		Tema
Capitulo 1		Introduccion
Capitulo 2		Estado del Arte
Capitulo 3		Arquitectura Propuesta
Capitulo 4		Implementacion
Capitulo 5		Resultados
Capitulo 6		Conclusiones


[GRAFICO] Resultados Clave

Metrica					Valor

Precision promedio		87%
Recall promedio			86%
F1-Score				0.86
Tiempo (20 fotos)		4.2 segundos
Memoria					145 MB
Privacidad				100% local


Comparacion con otros metodos

Metodo					F1-Score

Minimo					0.78
Maximo					0.79
Promedio				0.83
Ponderado				0.90


[TUBO_ENSAYO] Tests

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Ejecutar tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html


#[APRETON] Contribuir

Las contribuciones son bienvenidas. Por favor:

Fork el proyecto

Crear rama (git checkout -b feature/AmazingFeature)

Commit cambios (git commit -m 'Add AmazingFeature')

Push (git push origin feature/AmazingFeature)

Abrir Pull Request

Ver Guia para Desarrolladores para mas detalles.


[DOC] Licencia
Distribuido bajo licencia MIT. Ver LICENSE para mas informacion.


[EMAIL] Contacto
Autor: 		[Tu Nombre]
Email: 		[tu@email.com]
GitHub: 	@tuusuario
Proyecto: 	github.com/tuusuario/FaceAttenDANCE



[GRACIAS] Agradecimientos

A los profesores y companeros que colaboraron en las pruebas

A la comunidad de codigo abierto por las herramientas

A los alumnos que participaron en las pruebas con datos reales


[ESTRELLA] Reconocimientos
Si este proyecto te resulta util, !considera darle una estrella en GitHub! [ESTRELLA]

---

# Manual de Usuario - FaceAttenDANCE

## [LISTA] Tabla de Contenidos
1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalacion](#instalacion)
3. [Preparacion de Fotos](#preparacion-de-fotos)
4. [Primeros Pasos](#primeros-pasos)
5. [Uso Diario](#uso-diario)
6. [Reportes y Exportacion](#reportes-y-exportacion)
7. [Solucion de Problemas](#solucion-de-problemas)
8. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 1. Requisitos del Sistema

### Hardware
- **Procesador**: Cualquier procesador moderno (Intel/AMD)
- **Memoria RAM**: Minimo 4GB (recomendado 8GB)
- **Almacenamiento**: 500MB libres
- **Camara**: Para tomar las fotos (puede ser del celular)

### Software
- **Sistema Operativo**: 
  - Windows 10/11
  - macOS 10.15+
  - Linux (Ubuntu 20.04+)
- **Python**: Version 3.8 o superior
- **Espacio en disco**: Minimo 1GB para fotos y base de datos

---

## 2. Instalacion

### 2.1 Windows

```bash
# Abrir PowerShell como administrador

# Verificar que Python esta instalado
python --version

# Si no esta instalado, descargar de python.org

# Clonar el repositorio
git clone https://github.com/tuusuario/FaceAttenDANCE
cd FaceAttenDANCE

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

2.2 macOS / Linux
# Abrir terminal

# Verificar Python
python3 --version

# Clonar repositorio
git clone https://github.com/tuusuario/FaceAttenDANCE
cd FaceAttenDANCE

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

2.3 Verificar Instalacion
# Ejecutar el programa
python src/main.py

# Deberias ver:
# [DARDO] FaceAttenDANCE
# ==============================
# Sistema listo para usar


3. Preparacion de Fotos
3.1 Fotos de Alumnos (Registro Inicial)
Las fotos de los alumnos son la base del sistema. Deben ser:

Requisitos de las fotos:

[FOTO] Formato: JPG o PNG

[USUARIO] La persona debe estar de frente

[SOL] Buena iluminacion (sin sombras en el rostro)

[DARDO] Fondo simple (pared lisa ideal)

[EMOJI] Expresion neutral (sin gestos exagerados)

Procedimiento:

Crear carpeta alumnos en la raiz del proyecto

Para cada alumno, tomar una foto con estas caracteristicas

Guardar con el formato: Nombre_Apellido.jpg

[OK] Correcto: Laura_Carranza_Danzares.jpg

[OK] Correcto: Ariel_Romero.jpg

[ERROR] Incorrecto: foto1.jpg (no se sabe quien es)

[ERROR] Incorrecto: laura carranza.jpg (espacios, usar _ )

3.2 Fotos de Clase (Despues de Cada Clase)
Requisitos:

Tomar 2-3 fotos grupales al finalizar la clase

Intentar que todos miren a la camara

Si el grupo es grande, tomar fotos desde diferentes angulos

Organizacion:

# Crear una carpeta por cada clase
# Formato recomendado: clase_YYYY_MM_DD

# Ejemplos:
clase_2026_02_20/
  [EMOJI] foto_1.jpg
  [EMOJI] foto_2.jpg
  [EMOJI] foto_3.jpg

clase_2026_02_27/
  [EMOJI] grupo_1.jpg
  [EMOJI] grupo_2.jpg


4. Primeros Pasos
4.1 Iniciar el Sistema

# Asegurarse de estar en el entorno virtual
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Ejecutar
python src/main.py


4.2 Menu Principal
Al ejecutar, veras:

[DARDO] FaceAttenDANCE
==================================================
1. Registrar alumnos (desde carpeta 'alumnos')
2. Procesar clase
3. Ver reportes
4. Exportar asistencias
5. Configuracion
6. Salir
--------------------------------------------------
Selecciona una opcion:

4.3 Registrar Alumnos (Primera vez)
Opcion 1 del menu

El sistema escaneara la carpeta alumnos/

Veras algo como:

[CARPETA] Escaneando 5 fotos de alumnos...
  + Registrando Laura Carranza Danzares...
  + Registrando Ariel Romero Danzares...
  + Registrando Claudia Pavon Danzares...
  + Registrando Monica Oliva Danzares...
  + Registrando Carlos Lopez...

[OK] Alumnos registrados correctamente

. Uso Diario
5.1 Procesar una Clase
Despues de cada clase, con las fotos ya en una carpeta:

Opcion 2 "Procesar clase"

Ingresar nombre de la carpeta (ej: clase_2026_02_20)

Opcional: ingresar fecha (Enter para usar hoy)

El sistema procesara las fotos y mostrara:

============================================================
[FOTO] PROCESANDO CLASE 2026-02-20
============================================================
[CARPETA] Encontradas 3 fotos

Procesando foto_1.jpg... [EMOJI] OK
Procesando foto_2.jpg... [EMOJI] OK
Procesando foto_3.jpg... [EMOJI] OK

[BUSCAR] Buscando coincidencias...

Laura Carranza Danzares: [OK] 0.76
Ariel Romero Danzares: [OK] 0.82
Claudia Pavon Danzares: [OK] 0.71
Monica Oliva Danzares: [ERROR] 0.23
Carlos Lopez: [ERROR] 0.15

============================================================
[LISTA] REPORTE DE ASISTENCIA - 2026-02-20
============================================================

[OK] PRESENTES (3):
  [EMOJI] Laura Carranza Danzares   [0.76]
  [EMOJI] Ariel Romero Danzares      [0.82]
  [EMOJI] Claudia Pavon Danzares     [0.71]

[ERROR] AUSENTES (2):
  [EMOJI] Monica Oliva Danzares
  [EMOJI] Carlos Lopez

[GRAFICO] Asistencia: 3/5 (60.0%)
============================================================


5.2 Interpretacion de Resultados
[OK] (check verde): Alumno detectado en las fotos

[ERROR] (cruz roja): Alumno no detectado

[0.76]: Confianza de la deteccion (0 a 1)

0.6: Alta confianza

0.4 - 0.6: Confianza media (revisar manualmente)

< 0.4: Baja confianza (probablemente no estaba)

6. Reportes y Exportacion
6.1 Ver Reportes Mensuales
Opcion 3 "Ver reportes":

[GRAFICO] REPORTE MENSUAL - 2026/02
============================================================
[CALENDARIO] Clases en el mes: 4

[OK] ASISTENCIAS POR ALUMNO:
------------------------------------------------------------
Laura Carranza Danzares   4/4 (100%) [EMOJI]
Ariel Romero Danzares      4/4 (100%) [EMOJI]
Claudia Pavon Danzares     3/4 (75%)  [EMOJI]
Monica Oliva Danzares      2/4 (50%)  [EMOJI]
Carlos Lopez               1/4 (25%)  [EMOJI]


6.2 Exportar a Excel
Opcion 4 "Exportar asistencias":

Seleccionar clase (o "todas")

Seleccionar periodo (mes actual, personalizado)

El sistema genera un archivo CSV:

asistencias_Salsa_20260220.csv
asistencias_Bachata_20260220.csv

6.3 Abrir en Excel
Abrir Excel

Pestana Datos → Obtener datos → Desde un archivo → Desde CSV

Seleccionar el archivo generado

En el asistente, asegurar:

Origen del archivo: 65001: Unicode (UTF-8)

Delimitador: Coma

Cargar datos

7. Solucion de Problemas
7.1 El programa no inicia
Sintoma: Error python no se reconoce como comando

Solucion:

# Verificar instalacion de Python
python --version

# Si no esta instalado, descargar de python.org
# Durante la instalacion, marcar "Add Python to PATH"



7.2 Error de librerias
Sintoma: ModuleNotFoundError: No module named 'pillow'

Solucion:

# Activar entorno virtual y reinstalar
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

7.3 No se detectan rostros
Posibles causas y soluciones:

Problema	Solucion
Mala iluminacion	Tomar fotos con mas luz
Rostros muy pequenos	Acercar la camara
Angulo incorrecto	Pedir que miren a la camara
Umbral muy alto	Bajar umbral a 0.4 en configuracion
7.4 Falsos positivos (detecta quien no estaba)
Solucion:

# Bajar umbral de confianza
# En src/core/asociador.py, cambiar:
def __init__(self, umbral=0.5):  # de 0.6 a 0.5

8. Preguntas Frecuentes
?El sistema necesita internet?
No, 100% local. Tus fotos nunca salen de tu computadora.

?Puedo usar fotos del celular?
Si, puedes tomar fotos con cualquier dispositivo y pasarlas a la PC.

?Que pasa si un alumno cambia mucho (corte de pelo, barba)?
El sistema puede fallar. Se recomienda actualizar su foto de referencia cada 6 meses.

?Cuantos alumnos puede manejar?
Hemos probado con hasta 50 alumnos sin problemas de rendimiento.

?Puedo tener diferentes clases (Salsa, Bachata, Tango)?
Si, el sistema soporta multiples clases. Cada clase tiene su propio archivo de inscripcion en la carpeta inscripciones/.

?Como hago backup de mis datos?
Solo necesitas respaldar:

La carpeta alumnos/ (fotos de referencia)

El archivo asistencias.db (base de datos)

?El sistema funciona en tablet o celular?
Actualmente solo en computadoras. Version movil esta en planificacion.

?Que hago si el programa se cierra solo?
Ejecutar desde terminal para ver el error:

python src/main.py

El mensaje de error ayudara a diagnosticar.

[EMOJI] Soporte
Si encuentras algun problema no cubierto en este manual:

Revisa los issues en GitHub

Crea un nuevo issue con:

Sistema operativo

Version de Python

Mensaje de error completo

Pasos para reproducir

[NOTA] Notas de Version
Version 0.1.0 (Febrero 2026)
[OK] Primera version estable

[OK] Reconocimiento facial basico

[OK] Exportacion a CSV

[OK] Reportes mensuales

Proximas Versiones
[ESPERA] Fase 2: Analisis temporal

[ESPERA] Fase 3: Aprendizaje activo

[ESPERA] Interfaz grafica



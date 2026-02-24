# API Reference - FaceAttenDANCE

---

## INDICE DE CONTENIDOS

1. [Modulo Core](#1-modulo-core)
   1.1 [AsociadorFase1](#11-asociadorfase1)
   1.2 [Comparador](#12-comparador)
   1.3 [ImageProcessor](#13-imageprocessor)

2. [Modulo Database](#2-modulo-database)
   2.1 [DatabaseConnection](#21-databaseconnection)
   2.2 [RepositorioAlumnos](#22-repositorioalumnos)
   2.3 [RepositorioAsistencias](#23-repositorioasistencias)

3. [Modulo Utils](#3-modulo-utils)
   3.1 [ExportadorCSV](#31-exportadorcsv)

4. [Modulo UI](#4-modulo-ui)
   4.1 [CLI](#41-cli)

5. [Codigos de Error](#5-codigos-de-error)

6. [Ejemplos de Uso](#6-ejemplos-de-uso)

---

## 1. Modulo Core

### 1.1 AsociadorFase1

Clase principal para la Fase 1 de asociacion por co-ocurrencia ponderada.

```python
from core.asociador import AsociadorFase1

asociador = AsociadorFase1(umbral=0.6, metodo="ponderado")
```

Constructor
def __init__(self, umbral: float = 0.6, metodo: str = "ponderado")
Parametros:
umbral (float): Valor minimo para considerar asociacion (0.0 a 1.0). Default: 0.6
metodo (str): Metodo de calculo. Opciones: "minimo", "maximo", "promedio", "ponderado". Default: "ponderado"

Rasise:
ValueError: Si el metodo no es valido o el umbral esta fuera de rango

Metodos

registrar_sesion
def registrar_sesion(self, asistentes: List[str]) -> None
Registra una sesion con los asistentes detectados.
Parametros:
asistentes (List[str]): Lista de nombres de personas detectadas en la sesion
Ejemplo:
asociador.registrar_sesion(["Laura", "Ariel", "Claudia"])

_calcular_confianza_par
def _calcular_confianza_par(self, p1: str, p2: str) -> float
Calcula la confianza de que dos personas estan en la misma clase.
Parametros:
p1 (str): Nombre de la primera persona
p2 (str): Nombre de la segunda persona
Retorna	:
float	: Confianza entre 0 y 1
Ejemplo:
confianza = asociador._calcular_confianza_par("Laura", "Ariel")
print(f"Confianza: {confianza:.2%}")

sugerir_companeros
def sugerir_companeros(self, persona: str, min_confianza: float = None) -> List[Tuple[str, float]]
Sugiere quienes podrian estar en la misma clase.
Parametros:
persona (str): Persona de referencia
min_confianza (float, opcional): Umbral minimo. Si es None, usa self.umbral
Retorna:
List[Tuple[str, float]]: Lista de (persona, confianza) ordenada por confianza descendente
Ejemplo:
sugerencias = asociador.sugerir_companeros("Laura", min_confianza=0.5)
for companero, confianza in sugerencias:
    print(f"{companero}: {confianza:.2%}")

descubrir_clases
def descubrir_clases(self, min_confianza: float = None, min_miembros: int = 2) -> List[Set[str]]
Descubre clases completas automaticamente.

Parametros:
min_confianza (float, opcional): Umbral minimo. Si es None, usa self.umbral
min_miembros (int): Minimo de miembros por clase. Default: 2
Retorna:
List[Set[str]]: Lista de clases, cada clase es un conjunto de nombres
Ejemplo:
clases = asociador.descubrir_clases(min_confianza=0.6, min_miembros=3)
for i, clase in enumerate(clases, 1):
    print(f"Clase {i}: {', '.join(sorted(clase))}")

### 1.2 Comparador

Clase con metodos estaticos para comparar descriptores faciales.
from core.comparador import Comparador

Metodos Estaticos

diferencia_absoluta
@staticmethod
def diferencia_absoluta(desc1: np.ndarray, desc2: np.ndarray) -> float
Compara usando diferencia absoluta media.
Parametros:
desc1 (np.ndarray): Primer descriptor
desc2 (np.ndarray): Segundo descriptor
Retorna:
float: Similitud entre 0 y 1
Ejemplo:
sim = Comparador.diferencia_absoluta(desc1, desc2)

correlacion
@staticmethod
def correlacion(desc1: np.ndarray, desc2: np.ndarray) -> float
Compara usando correlacion de Pearson.
Retorna:
float: Correlacion normalizada entre 0 y 1

distancia_euclidiana
@staticmethod
def distancia_euclidiana(desc1: np.ndarray, desc2: np.ndarray) -> float
Compara usando distancia euclidiana normalizada.
Retorna:
float: Similitud entre 0 y 1

### 1.3 ImageProcessor

Procesador de imagenes para extraccion de descriptores.
from utils.image_processor import ImageProcessor
procesador = ImageProcessor(tamano=(32, 32))
Constructor
def __init__(self, tamano: tuple = (32, 32))
Parametros:
tamano (tuple): Dimensiones (ancho, alto) para redimensionar. Default: (32, 32)

Metodos

extraer_descriptor
def extraer_descriptor(self, ruta_imagen: Union[str, Path]) -> Optional[np.ndarray]
Extrae un descriptor de una imagen.
Parametros:
ruta_imagen (str | Path): Ruta al archivo de imagen
Retorna:
Optional[np.ndarray]: Descriptor como vector de 1024 elementos, o None si hay error
Rasise:
FileNotFoundError: Si la imagen no existe
Ejemplo:
descriptor = procesador.extraer_descriptor("alumnos/Laura_Garcia.jpg")
if descriptor is not None:
    print(f"Descriptor extraido: {descriptor.shape}")

extraer_descriptores_lote
def extraer_descriptores_lote(self, lista_rutas: List[Union[str, Path]]) -> List[np.ndarray]
Extrae descriptores de multiples imagenes.
Parametros:
lista_rutas (List[str | Path]): Lista de rutas a imagenes
Retorna:
List[np.ndarray]: Lista de descriptores validos (los errores se omiten)
Ejemplo:
rutas = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
descriptores = procesador.extraer_descriptores_lote(rutas)
print(f"Procesados {len(descriptores)} de {len(rutas)} imagenes")


## 2. Modulo Database

### 2.1 DatabaseConnection

Manejador de conexion a base de datos SQLite.
from database.conexion import DatabaseConnection
db = DatabaseConnection("asistencias.db")

Constructor
def __init__(self, db_path: str = "asistencias.db")
Parametros:
db_path (str): Ruta al archivo de base de datos. Default: "asistencias.db"

Metodos

conexion (context manager)
@contextmanager
def conexion(self)
Context manager para conexiones a BD.
Ejemplo:
with db.conexion() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos")
    resultados = cursor.fetchall()

_inicializar_bd
def _inicializar_bd(self) -> None
Crea las tablas si no existen. Se llama automaticamente al instanciar.

### 2.2 RepositorioAlumnos

Repositorio para operaciones con alumnos.
from database.repositorio_alumnos import RepositorioAlumnos
repo_alumnos = RepositorioAlumnos(db)
Constructor
def __init__(self, db_connection: DatabaseConnection)
Parametros:
db_connection (DatabaseConnection): Conexion a base de datos

Metodos

guardar
def guardar(self, nombre: str, foto_path: str, descriptor=None) -> int
Guarda un alumno en la base de datos.
Parametros:
nombre (str): Nombre del alumno
foto_path (str): Ruta a la foto
descriptor (np.ndarray, opcional): Descriptor facial
Retorna:
int: ID del alumno guardado

buscar_por_nombre
def buscar_por_nombre(self, nombre: str) -> Optional[dict]
Busca un alumno por nombre.
Retorna:
Optional[dict]: Datos del alumno o None

listar_activos
def listar_activos(self) -> List[dict]
Lista todos los alumnos activos.
Retorna:
List[dict]: Lista de alumnos


### 2.3 RepositorioAsistencias

Repositorio para operaciones con asistencias.
from database.repositorio_asistencias import RepositorioAsistencias
repo_asistencias = RepositorioAsistencias(db)

Metodos

guardar_asistencia
def guardar_asistencia(self, alumno_id: int, clase_nombre: str, fecha: str, hora: str, similitud: float) -> int
Guarda una asistencia.

buscar_por_clase_y_fecha
def buscar_por_clase_y_fecha(self, clase_nombre: str, fecha: str) -> List[dict]
Busca asistencias por clase y fecha.

reporte_mensual
def reporte_mensual(self, clase_nombre: str, ano: int, mes: int) -> dict
Genera reporte mensual de asistencias.


## 3. Modulo Utils

### 3.1 ExportadorCSV

Exportador a formato CSV.
from utils.exporters import ExportadorCSV

Metodos Estaticos

exportar_asistencias
@staticmethod
def exportar_asistencias(asistencias: List[tuple], filename: str = None) -> str
Exporta asistencias a CSV.

Parametros:
asistencias (List[tuple]): Lista de tuplas (nombre, fecha, hora, similitud)
filename (str, opcional): Nombre del archivo. Si es None, se genera automatico
Retorna:
str: Nombre del archivo generado
Ejemplo:
asistencias = [
    ("Laura", "2026-02-20", "19:30", 0.92),
    ("Ariel", "2026-02-20", "19:30", 0.88),
]
archivo = ExportadorCSV.exportar_asistencias(asistencias)
print(f"Exportado a: {archivo}")


## 4. Modulo UI

### 4.1 CLI
Interfaz de linea de comandos.
from ui.cli import CLI

cli = CLI()

Metodos

menu_interactivo
def menu_interactivo(self) -> None

Muestra menu interactivo y maneja las opciones del usuario.

procesar_clase
def procesar_clase(self, carpeta: str, clase: str = None, fecha: str = None, umbral: float = 0.5) -> dict
Procesa las fotos de una clase.
Retorna:
dict: Diccionario con resultados (presentes, ausentes, etc.)


## 5. Codigos de Error

Codigo	Descripcion
E001	Error al abrir imagen
E002	Formato de imagen no soportado
E003	Descriptor invalido
E004	Umbral fuera de rango (debe ser 0-1)
E005	Metodo de comparacion no valido
E006	Error de base de datos
E007	Archivo no encontrado


## 6. Ejemplos de Uso

Ver carpeta examples/ para ejemplos completos:

quickstart.py: Ejemplo basico del sistema

generar_datos_prueba.py: Generador de datos sinteticos

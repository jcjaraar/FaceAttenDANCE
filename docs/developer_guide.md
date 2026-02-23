# Gu铆a para Desarrolladores - FaceAttenDANCE

## 馃搵 Tabla de Contenidos
1. [Arquitectura del Sistema](#arquitectura-del-sistema)
2. [Configuraci贸n del Entorno de Desarrollo](#configuraci贸n-del-entorno-de-desarrollo)
3. [Estructura de C贸digo](#estructura-de-c贸digo)
4. [M贸dulo Core](#m贸dulo-core)
5. [Base de Datos](#base-de-datos)
6. [Tests](#tests)
7. [Estilo de C贸digo](#estilo-de-c贸digo)
8. [Flujo de Trabajo Git](#flujo-de-trabajo-git)
9. [Roadmap de Desarrollo](#roadmap-de-desarrollo)

---

## 1. Arquitectura del Sistema

### 1.1 Visi贸n General


┌─────────────────────────────────────────────────────────────	┐
│ FaceAttenDANCE 												│
├─────────────────────────────────────────────────────────────	┤
│ ┌──────────	┐ ┌──────────┐ ┌──────────	┐ ┌──────────	┐ 	│
│ │ Core 		│ │ Database │ │ UI 		│ │ Utils 		│ 	│
│ └──────────	┘ └──────────┘ └──────────	┘ └──────────	┘ 	│
│ 																│
│ ┌──────────────────────────────────────────────────────	┐	│
│ │ Tests 													│ 	│
│ └──────────────────────────────────────────────────────	┘ 	│
└─────────────────────────────────────────────────────────────	┘


### 1.2 Capas del Sistema

| Capa 			| Descripción 					| Tecnologías 				|
|------			|-------------					|-------------				|
| **Core** 		| Lógica principal del negocio 	| Python puro 				|
| **Database** 	| Persistencia de datos 		| SQLite3 					|
| **UI** 		| Interfaz de usuario 			| CLI (línea de comandos) 	|
| **Utils** 	| Utilidades varias 			| PIL, NumPy, OpenCV 		|
| **Tests** 	| Pruebas unitarias 			| Pytest 					|

### 1.3 Flujo de Datos

[Fotos Alumnos] ──? [Extractor Descriptores] ──? [Base Datos]
│
[Fotos Clase] ──? [Extractor Descriptores] ──? [Comparador] ?─┘
│
[Reportes]
│
[CSV/Excel]

---

## 2. Configuración del Entorno de Desarrollo

### 2.1 Requisitos Previos

```bash
# Versiones mínimas
Python >= 3.8
Git >= 2.30
pip >= 21.0
```

/////////////////////////(WSL/Docker)////////////////////////////
### 2.1 Requisitos Previos (WSL/Docker)

```bash
# Versiones mínimas
- Python >= 3.8
+ Python >= 3.8 (probado en 3.10.12)
Git >= 2.30
pip >= 21.0
+
+ # Para WSL/Ubuntu (adicional)
+ sudo apt update
+ sudo apt install -y python3-venv python3-pip python3-dev
```
/////////////////////////(WSL/Docker)////////////////////////////


### 2.2 Clonar y Configurar

# Clonar repositorio
git clone https://github.com/tuusuario/FaceAttenDANCE
cd FaceAttenDANCE

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Verificar instalación
pytest --version
black --version
pylint --version


/////////////////////////(WSL/Docker)////////////////////////////
### 2.2 Clonar y Configurar

+ # IMPORTANTE: Todos los comandos deben ejecutarse dentro de WSL
+ 
# Clonar repositorio
git clone https://github.com/tuusuario/FaceAttenDANCE
cd FaceAttenDANCE

# Crear entorno virtual
- python -m venv venv
+ python3 -m venv venv --prompt=faceattend

# Activar entorno
# Windows:
venv\Scripts\activate
- # Mac/Linux:
+ # Mac/Linux/WSL:
source venv/bin/activate

+ # Verificar que el entorno está activado (debe aparecer (faceattend))
+ which python  # Debe apuntar a /home/usuario/.../venv/bin/python
+
# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Verificar instalación
pytest --version
black --version
pylint --version
/////////////////////////(WSL/Docker)////////////////////////////

### 2.3 Estructura de Carpetas para Desarrollo

FaceAttenDANCE/
├── src/                    	# Código fuente
│   ├── core/               	# Lógica principal
│   │   ├── __init__.py
│   │   ├── detector.py     	# Detección de rostros
│   │   ├── comparador.py   	# Comparación de descriptores
│   │   ├── asociador.py    	# Fases 1,2,3
│   │   └── modelos.py      	# Clases de datos
│   ├── database/           	# Capa de datos
│   │   ├── __init__.py
│   │   ├── conexion.py     	# Conexión SQLite
│   │   ├── repositorio_alumnos.py
│   │   └── repositorio_asistencias.py
│   ├── ui/                 	# Interfaces
│   │   ├── __init__.py
│   │   └── cli.py          	# Línea de comandos
│   └── utils/              	# Utilidades
│       ├── __init__.py
│       ├── image_processor.py  # Procesamiento imágenes
│       └── exporters.py        # CSV/JSON
├── tests/                  	# Tests
│   ├── unit/               	# Tests unitarios
│   ├── integration/        	# Tests de integración
│   └── fixtures/           	# Datos de prueba
├── docs/                    	# Documentación
├── scripts/                 	# Scripts útiles
├── notebooks/               	# Jupyter notebooks
├── examples/                	# Ejemplos
└── config/                  	# Configuración

/////////////////////////(WSL/Docker)////////////////////////////
### 2.4 Configuración específica para WSL/Ubuntu

Si estás desarrollando en WSL con Ubuntu, necesitas pasos adicionales:

# 1. Actualizar paquetes del sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar python3-venv (NO viene por defecto en Ubuntu)
sudo apt install -y python3-venv python3-pip python3-dev

# 3. Verificar instalación
python3 -m venv --help  # Debe mostrar ayuda, no error

# 4. Recién ahora crear entorno virtual
cd ~/projects/FaceAttenDANCE
python3 -m venv venv --prompt=faceattend
source venv/bin/activate

# 5. Verificar
pip list  # Debe mostrar lista de paquetes

Problema común: Si olvidas instalar python3-venv, obtendrás el error:
The virtual environment was not created successfully because ensurepip is not available.

### 2.5 Solución de problemas comunes en WSL
| Problema 								| Síntoma 						| Solución 										|
|----------								|---------						|----------										|
| **Error: ensurepip not available** 	| `python3 -m venv` falla 		| `sudo apt install -y python3-venv` 			|
| **Error: pip not found** 				| `pip: command not found` 		| `sudo apt install -y python3-pip` 			|
| **Error: Permission denied** 			| No se puede crear archivos 	| Verificar permisos: `ls -la ~/projects` 		|
| **Error: Package not found** 			| `pip install` falla 			| Actualizar pip: `pip install --upgrade pip` 	|
| **VS Code no conecta** 				| No aparece "WSL: Ubuntu" 		| Instalar extensión "Remote - WSL" 			|

/////////////////////////(WSL/Docker)////////////////////////////

## 3. Estructura de Código

### 2.3 3.1 Convenciones Generales

Archivos: snake_case.py

Clases: CamelCase

Funciones: snake_case

Constantes: UPPER_CASE

Variables: snake_case

### 2.3 3.2 Template de Módulo

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nombre del Módulo - Descripción breve

Este módulo proporciona funcionalidades para...
"""

import logging
from typing import List, Dict, Optional

# Configurar logging
logger = logging.getLogger(__name__)

class MiClase:
    """Descripción de la clase."""
    
    def __init__(self, parametro: str):
        """Inicializa la clase.
        
        Args:
            parametro: Descripción del parámetro
        """
        self.parametro = parametro
        logger.info(f"MiClase inicializada con {parametro}")
    
    def mi_funcion(self, x: int) -> bool:
        """Descripción de la función.
        
        Args:
            x: Número a procesar
            
        Returns:
            True si se cumplió la condición
            
        Raises:
            ValueError: Si x es negativo
        """
        if x < 0:
            raise ValueError("x no puede ser negativo")
        return x > 10


## 4. Módulo Core

### 4.1 Detector de Rostros (detector.py)

"""
Módulo para detección de rostros en imágenes.
Soporta múltiples backends: OpenCV, MTCNN (futuro)
"""

import cv2
import numpy as np
from pathlib import Path

class DetectorRostros:
    """Clase principal para detección de rostros."""
    
    def __init__(self, metodo: str = "opencv", tama?o: tuple = (32, 32)):
        """
        Args:
            metodo: 'opencv' (por ahora)
            tama?o: (ancho, alto) para redimensionar
        """
        self.metodo = metodo
        self.tama?o = tama?o
        self._inicializar_detector()
    
    def _inicializar_detector(self):
        """Inicializa el detector según el método elegido."""
        if self.metodo == "opencv":
            self.face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
    
    def detectar(self, imagen_path: Path) -> List[np.ndarray]:
        """Detecta rostros en una imagen.
        
        Args:
            imagen_path: Ruta a la imagen
            
        Returns:
            Lista de descriptores de rostros detectados
        """
        # Implementar detección
        pass

### 4.2 Comparador (comparador.py)

"""
Módulo para comparación de descriptores faciales.
"""

import numpy as np

class ComparadorDescriptores:
    """Clase para comparar descriptores usando diferentes métricas."""
    
    @staticmethod
    def diferencia_absoluta(desc1: np.ndarray, desc2: np.ndarray) -> float:
        """Compara usando diferencia absoluta media.
        
        Returns:
            float: Similitud entre 0 y 1
        """
        if desc1 is None or desc2 is None:
            return 0.0
        diff = np.mean(np.abs(desc1 - desc2))
        return max(0.0, min(1.0, 1.0 - diff))
    
    @staticmethod
    def correlacion(desc1: np.ndarray, desc2: np.ndarray) -> float:
        """Compara usando correlación de Pearson."""
        # Implementar correlación
        pass


### 4.3 Asociador (asociador.py) - Fase 1

# Primero, respaldar la versión actual por si acaso
cp src/core/asociador.py src/core/asociador.py.bak

# Ahora actualizar con la versión final
cat > src/core/asociador.py << 'EOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de asociación inteligente de alumnos.
Implementa las tres fases del sistema.
"""

from typing import List, Dict, Set, Tuple
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
        self.matriz_coocurrencias = defaultdict(lambda: defaultdict(int))
        self.apariciones = defaultdict(int)
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
    
    def sugerir_grupo(self, persona: str, min_confianza: float = None) -> List[Tuple[str, float]]:
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
    
    def descubrir_clases(self, min_confianza: float = None, min_miembros: int = 2) -> List[Set[str]]:
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
        suma_confianzas = 0
        
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
            "porcentaje_confiables": (pares_confiables / total_pares * 100) if total_pares > 0 else 0,
            "confianza_promedio": suma_confianzas / total_pares if total_pares > 0 else 0
        }
EOF

### 4.4 Asociador Fase 2 y 3 (Estructura)

class AsociadorFase2(AsociadorFase1):
    """
    Fase 2: A?ade análisis temporal.
    
    Incorpora información de días y horarios para mejorar
    la precisión de las asociaciones.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sesiones_por_fecha = defaultdict(list)
        self.patrones_horarios = defaultdict(lambda: defaultdict(int))
    
    def registrar_sesion_con_fecha(self, asistentes: List[str], fecha: str, hora: str = None):
        """Registra sesión con información temporal."""
        super().registrar_sesion(asistentes)
        # Implementar lógica temporal


class AsociadorFase3(AsociadorFase2):
    """
    Fase 3: A?ade aprendizaje activo.
    
    Permite al usuario confirmar o corregir las asociaciones,
    y el sistema aprende de ese feedback.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.feedback_usuario = defaultdict(dict)
        self.pesos_aprendidos = defaultdict(lambda: 0.5)
    
    def registrar_feedback(self, persona1: str, persona2: str, misma_clase: bool):
        """Registra feedback del usuario sobre una asociación."""
        # Implementar aprendizaje
        pass

/////////////////////////(WSL/Docker)////////////////////////////
### 4.5 Verificación del módulo core

Para verificar que el asociador funciona correctamente:

```bash
# Desde la raíz del proyecto, con entorno virtual activado
python -c "from src.core.asociador import AsociadorFase1; print('? Módulo core OK')"

# Ejecutar prueba rápida
cat > test_asociador_rapido.py << 'EOF'
from src.core.asociador import AsociadorFase1
a = AsociadorFase1()
a.registrar_sesion(["Alumno1", "Alumno2"])
print(f"Confianza: {a.calcular_confianza('Alumno1', 'Alumno2')}")
EOF
python test_asociador_rapido.py
```

Salida esperada:
? Módulo core OK
Confianza: 1.0
/////////////////////////(WSL/Docker)////////////////////////////

## 5. Base de Datos

### 5.1 Esquema SQLite

-- Tabla de alumnos
CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    foto_path TEXT NOT NULL,
    descriptor BLOB,
    fecha_registro TEXT NOT NULL,
    activo INTEGER DEFAULT 1,
    telefono TEXT,
    email TEXT,
    notas TEXT
);

-- Tabla de clases
CREATE TABLE clases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    descripcion TEXT,
    activa INTEGER DEFAULT 1
);

-- Tabla de asistencias
CREATE TABLE asistencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno_id INTEGER NOT NULL,
    clase_nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    similitud REAL,
    UNIQUE(alumno_id, clase_nombre, fecha),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);

-- Tabla de sesiones
CREATE TABLE sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clase_nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    carpeta TEXT,
    fotos TEXT,
    timestamp TEXT NOT NULL,
    UNIQUE(clase_nombre, fecha)
);

### 5.2 Repositorio Base

# database/repositorio_base.py

import sqlite3
from contextlib import contextmanager
from pathlib import Path

class RepositorioBase:
    """Clase base para repositorios."""
    
    def __init__(self, db_path: str = "asistencias.db"):
        self.db_path = Path(db_path)
    
    @contextmanager
    def conexion(self):
        """Context manager para conexiones a BD."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()


## 6. Tests

### 6.1 Configuración de Pytest
Archivo pytest.ini en la raíz:

[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers
markers =
    unit: Tests unitarios
    integration: Tests de integración
    slow: Tests lentos

### 6.2 Ejemplo de Test Unitario

# tests/unit/test_asociador.py

import pytest
from src.core.asociador import AsociadorFase1

class TestAsociadorFase1:
    """Tests para la Fase 1 del asociador."""
    
    def setup_method(self):
        """Configuración antes de cada test."""
        self.asociador = AsociadorFase1(umbral=0.6)
    
    def test_registrar_sesion(self):
        """Verifica que se registren correctamente las sesiones."""
        self.asociador.registrar_sesion(["Laura", "Ariel"])
        
        assert self.asociador.total_sesiones == 1
        assert self.asociador.apariciones["Laura"] == 1
        assert self.asociador.apariciones["Ariel"] == 1
        assert self.asociador.matriz_coocurrencias["Laura"]["Ariel"] == 1
    
    def test_calcular_confianza_minimo(self):
        """Prueba método mínimo de confianza."""
        self.asociador.metodo = "minimo"
        
        # Registrar varias sesiones
        for _ in range(5):
            self.asociador.registrar_sesion(["Laura", "Ariel"])
        
        for _ in range(3):
            self.asociador.registrar_sesion(["Laura"])
        
        confianza = self.asociador.calcular_confianza("Laura", "Ariel")
        
        # Laura aparece 8 veces, Ariel 5, juntos 5
        # Método mínimo: 5/8 = 0.625
        assert confianza == pytest.approx(0.625, rel=1e-2)
    
    def test_sugerir_grupo(self):
        """Prueba sugerencias de grupo."""
        # Registrar patrón de clase consistente
        clase_fija = ["Laura", "Ariel", "Claudia"]
        for _ in range(10):
            self.asociador.registrar_sesion(clase_fija)
        
        # A veces viene Mónica
        for _ in range(3):
            self.asociador.registrar_sesion(clase_fija + ["Mónica"])
        
        sugerencias = self.asociador.sugerir_grupo("Laura")
        
        assert len(sugerencias) >= 2
        assert sugerencias[0][0] in ["Ariel", "Claudia"]
        assert sugerencias[0][1] > 0.8
    
    def test_descubrir_clases(self):
        """Prueba descubrimiento automático de clases."""
        # Simular dos clases distintas
        clase_salsa = ["Laura", "Ariel", "Claudia"]
        clase_bachata = ["Mónica", "Carlos", "Ana"]
        
        for _ in range(10):
            self.asociador.registrar_sesion(clase_salsa)
            self.asociador.registrar_sesion(clase_bachata)
        
        clases = self.asociador.descubrir_clases(min_miembros=3)
        
        assert len(clases) == 2
        assert any("Laura" in c for c in clases)
        assert any("Mónica" in c for c in clases)


### 6.3 Ejemplo de Test de Integración

# tests/integration/test_flujo_completo.py

import pytest
import tempfile
import shutil
from pathlib import Path
from src.core.asociador import AsociadorFase1
from src.utils.image_processor import extraer_descriptor

class TestFlujoCompleto:
    """Prueba flujos completos del sistema."""
    
    @pytest.fixture
    def directorio_temporal(self):
        """Crea un directorio temporal para pruebas."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)
    
    def test_procesar_clase_completa(self, directorio_temporal):
        """Prueba el flujo completo de procesamiento."""
        # Crear estructura
        alumnos_dir = directorio_temporal / "alumnos"
        clase_dir = directorio_temporal / "clase_test"
        alumnos_dir.mkdir()
        clase_dir.mkdir()
        
        # Aquí irían las pruebas con imágenes reales
        # Por ahora, test estructural
        assert alumnos_dir.exists()
        assert clase_dir.exists()

## 7. Estilo de Código

### 7.1 Black - Formateo Automático

# Formatear todo el código
black src/ tests/

# Verificar sin modificar
black --check src/ tests/

# Configuración en pyproject.toml

### 7.2 Pylint - Análisis Estático

# Ejecutar pylint
pylint src/

# Ignorar ciertas reglas si es necesario
# pylint: disable=too-many-arguments

### 7.3 MyPy - Type Hints

# Verificar tipos
mypy src/

### 7.4 Pre-commit Hooks

Archivo .pre-commit-config.yaml:

repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/pylint
    rev: v2.17.0
    hooks:
      - id: pylint
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.991
    hooks:
      - id: mypy


Instalación:

pre-commit install


## 8. Flujo de Trabajo Git

### 8.1 Convención de Branches

main                 # Producción
├── develop          # Desarrollo principal
    ├── feature/*    # Nuevas características
    ├── fix/*        # Correcciones
    ├── docs/*       # Documentación
    └── test/*       # Tests


### 8.2 Convención de Commits

Usamos Conventional Commits:

feat: a?adir Fase 1 de asociación
fix: corregir error en detección de rostros
docs: actualizar manual de usuario
test: agregar tests para asociador
refactor: mejorar rendimiento del comparador
style: formatear código con black
chore: actualizar dependencias

### 8.3 Flujo de Trabajo

# 1. Actualizar develop
git checkout develop
git pull

# 2. Crear rama feature
git checkout -b feature/nueva-funcionalidad

# 3. Hacer cambios y commits
git add .
git commit -m "feat: implementar nueva funcionalidad"

# 4. Mantener rama actualizada
git fetch origin
git rebase origin/develop

# 5. Push y crear Pull Request
git push origin feature/nueva-funcionalidad

/////////////////////////(WSL/Docker)////////////////////////////
### 8.3 Configuración inicial de Git (PROCEDIMIENTO CORRECTO)
```bash
# 1. Inicializar repositorio
git init
git checkout -b develop

# 2. ?PRIMERO! Crear .gitignore ANTES de agregar archivos
cat > .gitignore << 'EOF'
# Python
venv/
env/
__pycache__/
*.py[cod]
*.so
.Python
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/

# Project data (NO versionar)
data/db/*.db
data/fotos_alumnos/
data/fotos_clase/
data/reportes/
*.log

# Tests
.coverage
htmlcov/
.pytest_cache/

# Jupyter
.ipynb_checkpoints
*.ipynb

# OS
.DS_Store
Thumbs.db
EOF

# 3. Verificar que venv/ está excluido
grep "venv/" .gitignore

# 4. AHORA agregar archivos (excluirá venv/ automáticamente)
git add .

# 5. Verificar que NO hay archivos no deseados
git status | grep venv || echo "? venv/ excluido correctamente"

# 6. Primer commit
git commit -m "feat: estructura inicial del proyecto"
```

### 8.5 Recuperación: Si ya agregaste venv/ por error

# 1. Crear .gitignore primero
cat > .gitignore << 'EOF'
# ... (mismo contenido que arriba)
EOF

# 2. Eliminar venv del índice (manteniendo archivos locales)
git rm -r --cached venv/

# 3. Agregar .gitignore
git add .gitignore
git commit -m "chore: excluir venv/ del repositorio"

# 4. Verificar que quedó limpio
git status
/////////////////////////(WSL/Docker)////////////////////////////


8.4 Template de Pull Request

## Descripción
[Descripción clara de los cambios]

## Tipo de cambio
- [ ] Nueva funcionalidad
- [ ] Corrección de bug
- [ ] Mejora de rendimiento
- [ ] Documentación
- [ ] Tests

## Cómo probar
1. Paso 1
2. Paso 2
3. Verificar que...

## Checklist
- [ ] Tests pasan localmente
- [ ] Código formateado con black
- [ ] Type hints agregados
- [ ] Documentación actualizada


## 9. Roadmap de Desarrollo

Fase 1: Co-ocurrencia Ponderada (Actual)

Módulo				Estado					Prioridad
Detector básico		? En desarrollo			Alta
Comparador			? En desarrollo			Alta
Asociador Fase 1	? En desarrollo			Alta
Tests unitarios		? En desarrollo			Media
Documentación		? Completado			Baja


Fase 2: Análisis Temporal (Próximo)

Agregar timestamp a sesiones
Detectar patrones por día/hora
Clases con horarios fijos
Visualización temporal

Fase 3: Aprendizaje Activo (Futuro)

Interfaz de confirmación
Feedback del usuario
Ajuste automático de pesos
Mejora continua

Mejoras Futuras

Interfaz gráfica (Tkinter/PyQt)
App móvil (Kivy)
API REST (Flask/FastAPI)
Reconocimiento en tiempo real

?? Referencias

Pillow Documentation
NumPy Documentation
OpenCV Python Tutorials
SQLite Python
Pytest Documentation
Conventional Commits

?? Contribuciones

Las contribuciones son bienvenidas. Por favor:

1.Fork el proyecto
2.Crear rama desde develop
3.Seguir convenciones de código
4.Agregar tests
5.Actualizar documentación
6.Crear Pull Request a develop






### Acceso a archivos desde Windows

**Ruta correcta para tí:**
- Explorador de archivos: `\\wsl$\Ubuntu-22.04`
- PowerShell: `explorer.exe \\wsl$\Ubuntu-22.04`
- Ruta a tu proyecto: `\\wsl$\Ubuntu-22.04\home\jjara\FaceAttenDANCE`

### Comandos WSL específicos

```powershell
# Ver distribución predeterminada
wsl -l -v

# Entrar a tu distribución (usa el nombre correcto)
wsl ~  # Si es la predeterminada
# O específicamente:
wsl -d Ubuntu-22.04

# Apagar WSL
wsl --shutdown

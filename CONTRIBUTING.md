# Gu铆a para Contribuir

隆Gracias por tu inter茅s en contribuir a FaceAttenDANCE! Este documento proporciona las pautas para contribuir al proyecto.

## 馃搵 Tabla de Contenidos

- [C贸digo de Conducta](#c贸digo-de-conducta)
- [C贸mo empezar](#c贸mo-empezar)
- [Reportar issues](#reportar-issues)
- [Proponer cambios](#proponer-cambios)
- [Gu铆a de desarrollo](#gu铆a-de-desarrollo)
- [Estilo de c贸digo](#estilo-de-c贸digo)
- [Tests](#tests)
- [Documentaci贸n](#documentaci贸n)

## C贸digo de Conducta

Este proyecto sigue un [C贸digo de Conducta](CODE_OF_CONDUCT.md). Al participar, se espera que mantengas este c贸digo.

## C贸mo empezar

1. Fork el repositorio
2. Clona tu fork: `git clone https://github.com/tuusuario/FaceAttenDANCE.git`
3. Crea una rama: `git checkout -b feature/tu-feature`
4. Instala dependencias: `pip install -r requirements-dev.txt`
5. Haz tus cambios
6. Ejecuta tests: `pytest tests/`
7. Formatea c贸digo: `black src/ tests/`
8. Commit y push
9. Abre un Pull Request

## Reportar issues

### Bugs
- Usa el template de bug report
- Incluye pasos para reproducir
- Incluye versi贸n de Python y sistema operativo
- Incluye mensaje de error completo

### Features
- Usa el template de feature request
- Explica el problema que resuelve
- Describe la soluci贸n propuesta

## Proponer cambios

### Pull Requests

1. Aseg煤rate de que los tests pasen
2. Actualiza la documentaci贸n si es necesario
3. Sigue el estilo de c贸digo
4. Incluye tests para nuevas funcionalidades
5. Mant茅n PRs peque帽os y enfocados

### Estructura de commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):


## Guía de desarrollo

### Entorno de desarrollo

```bash
# Clonar
git clone https://github.com/tuusuario/FaceAttenDANCE
cd FaceAttenDANCE

# Entorno virtual
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements-dev.txt

# Instalar pre-commit hooks
pre-commit install
```

##Comandos útiles

make test        # Ejecutar tests
make lint        # Ejecutar linter
make format      # Formatear código
make run         # Ejecutar programa
make clean       # Limpiar archivos temporales


## Estilo de código

Usamos Black con línea de 100 caracteres

Usamos isort para ordenar imports

Usamos pylint para linting

Usamos mypy para type hints

Type hints

Todas las funciones deben incluir type hints:


def procesar_clase(self, carpeta: str, fecha: Optional[str] = None) -> Dict[str, Any]:
    """Procesa las fotos de una clase."""
    pass


## Docstrings

Usamos formato Google:

def extraer_descriptor(ruta_imagen: str) -> Optional[np.ndarray]:
    """
    Extrae características de una imagen.

    Args:
        ruta_imagen: Ruta al archivo de imagen

    Returns:
        Descriptor facial o None si hay error

    Raises:
        FileNotFoundError: Si la imagen no existe
    """


## Tests

Los tests deben estar en tests/unit/ o tests/integration/

Usamos pytest

Mínimo 80% de cobertura

## Ejecutar tests

pytest tests/ -v

# Con cobertura

pytest tests/ --cov=src --cov-report=html


## Documentación

Actualiza README.md si cambia la instalación o uso

Actualiza docs/ para cambios en funcionalidad

Actualiza docs/API.md para cambios en la API

Documenta funciones con docstrings

?Dudas?
Si tienes preguntas, abre un issue o contacta a los mantenedores.

##?Gracias por contribuir! ??

# Fixtures para Tests

Esta carpeta contiene datos de ejemplo para ejecutar las pruebas del sistema.

## Estructura

fixtures/
[EMOJI] alumnos/ # Fotos de ejemplo de alumnos
[EMOJI] [EMOJI] Laura_Garcia.jpg
[EMOJI] [EMOJI] Ariel_Romero.jpg
[EMOJI] [EMOJI] ...
[EMOJI] clases/ # Fotos de ejemplo de clases
[EMOJI] [EMOJI] salsa_2026_02_20/
[EMOJI] [EMOJI] [EMOJI] foto1.jpg
[EMOJI] [EMOJI] [EMOJI] foto2.jpg
[EMOJI] [EMOJI] [EMOJI] ...
[EMOJI] [EMOJI] bachata_2026_02_21/
[EMOJI] [EMOJI] grupo1.jpg
[EMOJI] [EMOJI] grupo2.jpg
[EMOJI] data/ # Datos sinteticos
[EMOJI] alumnos.json
[EMOJI] clases.json
[EMOJI] inscripciones.json
[EMOJI] asistencias.json



## Uso en tests

```python
import pytest
from pathlib import Path

@pytest.fixture
def datos_prueba():
    """Carga datos de prueba."""
    ruta = Path(__file__).parent / "fixtures/data/alumnos.json"
    with open(ruta) as f:
        return json.load(f)

def test_con_datos_reales(datos_prueba):
    assert len(datos_prueba) > 0
```

## Generar nuevos fixtures

Puedes generar nuevos datos sinteticos con:

```python
python examples/generar_datos_prueba.py
```

Los archivos se crearan en data/ y luego puedes copiarlos a tests/fixtures/data/ si son utiles para tests.


---

### **4.4 Archivo: notebooks/analisis_resultados.ipynb** (Jupyter Notebook - version texto)

```markdown
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Analisis de Resultados - FaceAttenDANCE\n",
    "\n",
    "Este notebook analiza los resultados obtenidos en las pruebas del sistema."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "sys.path.append('..')\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from pathlib import Path\n",
    "from src.core.asociador import AsociadorFase1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Cargar datos de prueba"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Cargar asistencias generadas\n",
    "with open('../data/asistencias.json', 'r') as f:\n",
    "    asistencias = pd.read_json(f)\n",
    "\n",
    "print(f\"Asistencias cargadas: {len(asistencias)}\")\n",
    "asistencias.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Analisis de asistencia por alumno"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "asistencia_por_alumno = asistencias.groupby('alumno_nombre').size().sort_values(ascending=False)\n",
    "\n",
    "plt.figure(figsize=(12, 6))\n",
    "asistencia_por_alumno.head(15).plot(kind='bar')\n",
    "plt.title('Asistencias por Alumno (Top 15)')\n",
    "plt.xlabel('Alumno')\n",
    "plt.ylabel('Cantidad de asistencias')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Analisis de asistencia por clase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "asistencia_por_clase = asistencias.groupby('clase_nombre').size()\n",
    "\n",
    "plt.figure(figsize=(10, 5))\n",
    "asistencia_por_clase.plot(kind='bar', color='skyblue')\n",
    "plt.title('Asistencias por Clase')\n",
    "plt.xlabel('Clase')\n",
    "plt.ylabel('Cantidad de asistencias')\n",
    "plt.xticks(rotation=0)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Evolucion temporal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "asistencias['fecha'] = pd.to_datetime(asistencias['fecha'])\n",
    "asistencias_por_dia = asistencias.groupby(asistencias['fecha'].dt.date).size()\n",
    "\n",
    "plt.figure(figsize=(14, 5))\n",
    "asistencias_por_dia.plot(kind='line', marker='o')\n",
    "plt.title('Asistencias por Dia')\n",
    "plt.xlabel('Fecha')\n",
    "plt.ylabel('Cantidad de asistencias')\n",
    "plt.grid(True, alpha=0.3)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Simulacion del asociador"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crear asociador\n",
    "asociador = AsociadorFase1(umbral=0.6, metodo=\"ponderado\")\n",
    "\n",
    "# Agrupar asistencias por fecha para simular sesiones\n",
    "sesiones = asistencias.groupby('fecha')['alumno_nombre'].apply(list)\n",
    "\n",
    "# Registrar sesiones\n",
    "for fecha, asistentes in sesiones.items():\n",
    "    asociador.registrar_sesion(asistentes)\n",
    "    print(f\"Sesion {fecha}: {len(asistentes)} asistentes\")\n",
    "\n",
    "print(f\"\\nTotal sesiones registradas: {asociador.total_sesiones}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Ver asociaciones para un alumno\n",
    "alumno = \"Laura Garcia\"\n",
    "print(f\"\\n[BUSCAR] Sugerencias para {alumno}:\")\n",
    "sugerencias = asociador.sugerir_companeros(alumno, min_confianza=0.4)\n",
    "for compa, conf in sugerencias:\n",
    "    veces = asociador.matriz_coocurrencias[alumno].get(compa, 0)\n",
    "    print(f\"  - {compa:20} confianza: {conf:.1%} ({veces} veces juntos)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Conclusiones del analisis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*Resumir aqui los hallazgos principales...*"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}



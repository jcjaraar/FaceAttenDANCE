#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixtures compartidos para todos los tests.
"""

import pytest
import tempfile
import shutil
from pathlib import Path


@pytest.fixture
def directorio_temporal():
    """Crea un directorio temporal para pruebas."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


@pytest.fixture
def datos_asociador_basico():
    """Retorna datos básicos para probar asociador."""
    return {
        "clase_salsa": ["Laura", "Ariel", "Claudia"],
        "clase_bachata": ["Mónica", "Carlos", "Ana"],
        "alumno_estrella": "Laura",
    }

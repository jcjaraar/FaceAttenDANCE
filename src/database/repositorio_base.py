#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase base para repositorios de base de datos.
Maneja la conexión a SQLite y operaciones comunes.
"""

import logging
import sqlite3
from contextlib import contextmanager
from pathlib import Path

logger = logging.getLogger(__name__)


class RepositorioBase:
    """Clase base para repositorios."""

    def __init__(self, db_path: str = "data/db/faceattend.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._inicializar_bd()

    def _inicializar_bd(self):
        """Inicializa la base de datos con el esquema."""
        with self.conexion() as conn:
            # Ejecutar schema.sql si existe
            schema_path = Path("scripts/sql/schema.sql")
            if schema_path.exists():
                with open(schema_path, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
                logger.info("Base de datos inicializada")

    @contextmanager
    def conexion(self):
        """Context manager para conexiones a BD."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error("Error en BD: %s", e)
            raise
        finally:
            conn.close()

    def ejecutar_consulta(self, query: str, params: tuple = ()):
        """Ejecuta una consulta y retorna resultados."""
        with self.conexion() as conn:
            cursor = conn.execute(query, params)
            return cursor.fetchall()

-- Tabla de alumnos
CREATE TABLE IF NOT EXISTS alumnos (
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
CREATE TABLE IF NOT EXISTS clases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    descripcion TEXT,
    activa INTEGER DEFAULT 1
);

-- Tabla de asistencias
CREATE TABLE IF NOT EXISTS asistencias (
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
CREATE TABLE IF NOT EXISTS sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    clase_nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    carpeta TEXT,
    fotos TEXT,
    timestamp TEXT NOT NULL,
    UNIQUE(clase_nombre, fecha)
);

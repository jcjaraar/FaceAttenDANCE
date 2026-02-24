03_arquitectura.md

# Capitulo 3: Arquitectura Propuesta

---

## 3.1 Vision General del Sistema

FaceAttenDANCE es un sistema disenado con una arquitectura modular y escalable que permite el procesamiento local de imagenes para control de asistencia.

### 3.1.1 Diagrama de Bloques

[EMOJI]	[EMOJI]
[EMOJI] FaceAttenDANCE 														[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] 																		[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] 		[EMOJI]	[EMOJI] 		[EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] Entrada 		[EMOJI]	[EMOJI] Procesamiento	[EMOJI]	[EMOJI] Salida 		[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] 				[EMOJI] 		[EMOJI] 				[EMOJI] 		[EMOJI] 				[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] - Fotos 		[EMOJI] 		[EMOJI] - Deteccion 	[EMOJI] 		[EMOJI] - Reportes 	[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] - Alumnos 		[EMOJI] 		[EMOJI] - Extraccion 	[EMOJI] 		[EMOJI] - CSV/Excel 	[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] - Clases 		[EMOJI] 		[EMOJI] - Comparacion	[EMOJI] 		[EMOJI] - Estadisticas[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] 				[EMOJI] 		[EMOJI] - Asociacion 	[EMOJI] 		[EMOJI] 				[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] 		[EMOJI]	[EMOJI] 		[EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI] 																		[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] Base de Datos Local 											[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI] (SQLite - alumnos, asistencias) 								[EMOJI] 	[EMOJI]
[EMOJI] [EMOJI]	[EMOJI] 	[EMOJI]
[EMOJI] 																		[EMOJI]
[EMOJI]	[EMOJI]


### 3.1.2 Componentes Principales

| Componente 					| Responsabilidad 							| Tecnologia 		|
|------------					|-----------------							|------------		|
| **Modulo de Entrada** 		| Carga de imagenes, validacion de formatos | PIL, Pathlib 		|
| **Procesador de Imagenes** 	| Deteccion y extraccion de descriptores 	| PIL, NumPy 		|
| **Motor de Comparacion** 		| Calculo de similitud entre descriptores 	| NumPy 			|
| **Asociador** 				| Inferencia de pertenencia a clases 		| Python puro 		|
| **Base de Datos** 			| Almacenamiento persistente 				| SQLite3 			|
| **Generador de Reportes** 	| Exportacion a CSV/Excel 					| CSV, Pandas 		|
| **Interfaz de Usuario** 		| Interaccion por linea de comandos 		| Python argparse 	|

---

## 3.2 Arquitectura de Datos

### 3.2.1 Modelo Entidad-Relacion

[EMOJI]       [EMOJI]       [EMOJI]
[EMOJI]    alumnos      [EMOJI]       [EMOJI]   asistencias   [EMOJI]       [EMOJI]    clases       [EMOJI]
[EMOJI]       [EMOJI]       [EMOJI]
[EMOJI] PK: id          [EMOJI] PK: id          [EMOJI]       [EMOJI] PK: id          [EMOJI]
[EMOJI] nombre          [EMOJI]       [EMOJI] FK: alumno_id   [EMOJI] nombre          [EMOJI]
[EMOJI] foto_path       [EMOJI]       [EMOJI] clase_nombre    [EMOJI]       [EMOJI] descripcion     [EMOJI]
[EMOJI] descriptor      [EMOJI]       [EMOJI] fecha           [EMOJI]       [EMOJI] activa          [EMOJI]
[EMOJI] fecha_registro  [EMOJI]       [EMOJI] hora            [EMOJI]       [EMOJI]
[EMOJI] activo          [EMOJI]       [EMOJI] similitud       [EMOJI]
[EMOJI]       [EMOJI]
         [EMOJI]                         [EMOJI]
         [EMOJI]                         [EMOJI]
         [EMOJI]                         [EMOJI]
[EMOJI]       [EMOJI]
[EMOJI]    sesiones     [EMOJI]       [EMOJI]  coocurrencias  [EMOJI]
[EMOJI]       [EMOJI]
[EMOJI] PK: id          [EMOJI]       [EMOJI] PK: id          [EMOJI]
[EMOJI] clase_nombre    [EMOJI]       [EMOJI] persona_a       [EMOJI]
[EMOJI] fecha           [EMOJI]       [EMOJI] persona_b       [EMOJI]
[EMOJI] carpeta         [EMOJI]       [EMOJI] veces_juntos    [EMOJI]
[EMOJI] fotos           [EMOJI]       [EMOJI]
[EMOJI] timestamp       [EMOJI]
[EMOJI]


Relaciones Explicadas
alumnos → asistencias (1 a N)

Un alumno puede tener muchas asistencias

Cada asistencia pertenece a un solo alumno

clases → asistencias (1 a N)

Una clase puede tener muchas asistencias

Cada asistencia pertenece a una sola clase

alumnos → coocurrencias (N a M, autocorrelacion)

Tabla que relaciona alumnos con otros alumnos

Guarda cuantas veces aparecieron juntos en fotos

persona_a y persona_b son IDs de alumnos

clases → sesiones (1 a N)

Una clase puede tener muchas sesiones (dias de clase)

Cada sesion pertenece a una sola clase


Cardinalidades


alumnos [EMOJI]< asistencias >[EMOJI] clases
    1                N                1

alumnos [EMOJI]< coocurrencias >[EMOJI] alumnos
    1                M                1
   (a)                                (b)

clases [EMOJI]< sesiones >[EMOJI] (sin otra tabla)
    1                N


Tabla alumnos
[EMOJI]
[EMOJI] id [EMOJI] nombre          [EMOJI]
[EMOJI]
[EMOJI] 1  [EMOJI] Laura           [EMOJI]
[EMOJI] 2  [EMOJI] Ariel           [EMOJI]
[EMOJI] 3  [EMOJI] Claudia         [EMOJI]
[EMOJI]
       [EMOJI]                       Tabla coocurrencias
       [EMOJI]                       [EMOJI]
       [EMOJI]                       [EMOJI] id [EMOJI] pers_a  [EMOJI] pers_b  [EMOJI] veces_juntos [EMOJI]
       [EMOJI]
       [EMOJI] 1  [EMOJI] 1       [EMOJI] 2       [EMOJI] 15           [EMOJI]
                               [EMOJI] 2  [EMOJI] 1       [EMOJI] 3       [EMOJI] 12           [EMOJI]
                               [EMOJI] 3  [EMOJI] 2       [EMOJI] 3       [EMOJI] 10           [EMOJI]
                               [EMOJI]
Tabla coocurrencias en detalle
Esta tabla es especial porque relaciona alumnos con alumnos (autorreferencial):

Campo			Descripcion
id				Identificador unico del registro
persona_a		ID de un alumno (foreign key a alumnos.id)
persona_b		ID de otro alumno (foreign key a alumnos.id)
veces_juntos	Numero de sesiones donde aparecieron juntos

Ejemplo de consulta:

-- Encontrar companeros frecuentes de Laura (id=1)
SELECT a2.nombre, c.veces_juntos
FROM coocurrencias c
JOIN alumnos a1 ON c.persona_a = a1.id
JOIN alumnos a2 ON c.persona_b = a2.id
WHERE a1.nombre = 'Laura' AND c.veces_juntos > 10
ORDER BY c.veces_juntos DESC;


### 3.2.2 Flujo de Datos

Entrada Procesamiento Salida
[EMOJI]

Fotos Alumnos [EMOJI] Extraer Descriptor [EMOJI] Guardar en BD [EMOJI] Alumno registrado
(una vez por alumno)

Fotos Clase [EMOJI] Extraer Descriptor [EMOJI] Comparar con BD [EMOJI] Lista de detectados
(por cada foto)

Detectados [EMOJI] Registrar Sesion [EMOJI] Actualizar Matriz [EMOJI] Co-ocurrencias
de co-ocurrencias

Co-ocurrencias [EMOJI] Calcular confianzas [EMOJI] Sugerir grupos [EMOJI] Clases inferidas

Asistencias [EMOJI] Generar Reporte [EMOJI] Exportar CSV [EMOJI] Excel/Planilla


---

## 3.3 Modulo de Procesamiento de Imagenes

### 3.3.1 Pipeline de Procesamiento

Imagen original
		[EMOJI]
		[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] Convertir 	[EMOJI]
[EMOJI] a grises 		[EMOJI]
[EMOJI]	[EMOJI]
		[EMOJI]
		[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] Redimensionar	[EMOJI]
[EMOJI] a 32x32 		[EMOJI]
[EMOJI]	[EMOJI]
		[EMOJI]
		[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] Normalizar 	[EMOJI]
[EMOJI] (0 a 1) 		[EMOJI]
[EMOJI]	[EMOJI]
		[EMOJI]
		[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] Aplanar 		[EMOJI]
[EMOJI] (1024 dim) 	[EMOJI]
[EMOJI]	[EMOJI]
		[EMOJI]
		[EMOJI]
Descriptor final


### 3.3.2 Parametros de Configuracion

| Parametro 		| Valor 			| Justificacion 							|
|-----------		|-------			|---------------							|
| Tamano de imagen 	| 32x32 pixeles 	| Balance entre informacion y rendimiento	|
| Espacio de color 	| Escala de grises 	| Suficiente para patrones faciales 		|
| Normalizacion 	| [0, 1] 			| Consistencia en comparaciones 			|
| Dimensionalidad 	| 1024 				| Vector manejable computacionalmente 		|

**Rendimiento esperado:**

Operacion 				Tiempo (ms) [EMOJI] Escala
[EMOJI]
Carga de imagen 		5 ms [[EMOJI]] 20ms
Conversion a grises 	2 ms [[EMOJI]] 10ms
Redimensionamiento 		3 ms [[EMOJI]] 15ms
Normalizacion 			1 ms [[EMOJI]] 5ms
Aplanado 				1 ms [[EMOJI]] 5ms
[EMOJI]
Total 					12 ms [[EMOJI]] 60ms por imagen


---

## 3.4 Motor de Comparacion

### 3.4.1 Metodos Implementados

```python
def comparar_descriptores(desc1, desc2, metodo="ponderado"):
    """
    Compara dos descriptores segun el metodo elegido.
    """
    if metodo == "minimo":
        return min(confianza_ab, confianza_ba)
    elif metodo == "maximo":
        return max(confianza_ab, confianza_ba)
    elif metodo == "promedio":
        return (confianza_ab + confianza_ba) / 2
    elif metodo == "ponderado":
        peso_a = apariciones_a / (apariciones_a + apariciones_b)
        peso_b = apariciones_b / (apariciones_a + apariciones_b)
        return confianza_ab * peso_a + confianza_ba * peso_b

3.4.2 Matriz de Confusion

                     Realidad
                  Presente  Ausente
                [EMOJI]
   Detectado    [EMOJI]   TP   [EMOJI]   FP   [EMOJI]
                [EMOJI]
  No detectado  [EMOJI]   FN   [EMOJI]   TN   [EMOJI]
                [EMOJI]

TP: Verdadero Positivo (detectado correctamente)
FP: Falso Positivo  (detectado cuando no estaba)
FN: Falso Negativo  (no detectado cuando estaba)
TN: Verdadero Negativo (correctamente no detectado)


3.4.3 Metricas de Evaluacion

Metrica				Formula					Descripcion
Precision			TP / (TP + FP)			De los detectados, cuantos realmente estaban
Recall				TP / (TP + FN)			De los que estaban, cuantos fueron detectados
F1-Score			2 * (P*R)/(P+R)			Balance entre precision y recall
Exactitud			(TP+TN)/(TP+TN+FP+FN)	Aciertos totales


3.5 Algoritmo de Asociacion (Fase 1)

3.5.1 Pseudocodigo

Entrada: Lista de sesiones con asistentes
Salida: Grupos de alumnos (clases inferidas)

Inicializar matriz_coocurrencias = {}
Inicializar contador_apariciones = {}
Inicializar total_sesiones = 0

PARA CADA sesion EN sesiones:
    total_sesiones += 1

    PARA CADA persona EN sesion.asistentes:
        contador_apariciones[persona] += 1

    PARA CADA par (p1, p2) EN sesion.asistentes:
        matriz_coocurrencias[p1][p2] += 1
        matriz_coocurrencias[p2][p1] += 1

PARA CADA persona EN contador_apariciones:
    grupo = {persona}
    PARA CADA otra_persona EN contador_apariciones:
        SI persona != otra_persona:
            veces_juntos = matriz_coocurrencias[persona][otra_persona]
            confianza = calcular_confianza(veces_juntos,
                                          contador_apariciones[persona],
                                          contador_apariciones[otra_persona])
            SI confianza >= UMBRAL:
                grupo.agregar(otra_persona)

    SI tamano(grupo) >= MIN_MIEMBROS:
        clases.agregar(grupo)

RETORNAR clases

3.5.2 Complejidad Computacional

Operacion			Complejidad		Escala (n=100)
Registrar sesion	O(m²)			400 ops (m=20 asistentes)
Calcular confianza	O(1)			1 op
Descubrir clases	O(p²)			10,000 ops (p=100 personas)
Total				O(p²)			~10,000 ops/sesion


Rendimiento esperado:

Tiempo de procesamiento vs. Numero de alumnos:

Alumnos    Tiempo (ms)
[EMOJI]
10           5 ms     [[EMOJI]]
20          20 ms     [[EMOJI]]
50         125 ms     [[EMOJI]]
100        500 ms     [[EMOJI]]
200       2000 ms     [[EMOJI]]


3.6 Base de Datos
3.6.1 Esquema SQL

-- Tabla de alumnos
CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    foto_path TEXT NOT NULL,
    descriptor BLOB,
    fecha_registro TEXT NOT NULL,
    activo INTEGER DEFAULT 1
);

-- Tabla de asistencias
CREATE TABLE asistencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno_id INTEGER NOT NULL,
    clase_nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    similitud REAL,
    UNIQUE(alumno_id, clase_nombre, fecha)
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

-- Indices para optimizacion
CREATE INDEX idx_asistencias_fecha ON asistencias(fecha);
CREATE INDEX idx_asistencias_alumno ON asistencias(alumno_id);
CREATE INDEX idx_sesiones_clase ON sesiones(clase_nombre);


3.6.2 Tamano Estimado de la BD

Tabla			Registros	Tamano por registro	Total
alumnos			100			1 KB				100 KB
asistencias		10,000		100 B				1 MB
sesiones		500			200 B				100 KB
Total			~1.2 MB


3.7 Interfaz de Usuario

3.7.1 Estructura de Menus

[EMOJI]	[EMOJI]
[EMOJI]   FaceAttenDANCE v1.0               	[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] 1. Registrar alumnos                	[EMOJI]
[EMOJI] 2. Procesar clase                   	[EMOJI]
[EMOJI] 3. Ver reportes                      	[EMOJI]
[EMOJI] 4. Exportar asistencias              	[EMOJI]
[EMOJI] 5. Configuracion                     	[EMOJI]
[EMOJI] 6. Salir                             	[EMOJI]
[EMOJI]	[EMOJI]
[EMOJI] Seleccione una opcion: _             	[EMOJI]
[EMOJI]	[EMOJI]


3.7.2 Flujo de Trabajo Tipico

Dia 1: Configuracion inicial
  [EMOJI] Opcion 1: Registrar alumnos (unica vez)

Dia 2: Primera clase
  [EMOJI] Tomar fotos → Opcion 2: Procesar clase

Dia 15: Fin de mes
  [EMOJI] Opcion 3: Ver reporte mensual
  [EMOJI] Opcion 4: Exportar a Excel


3.8 Requisitos No Funcionales

3.8.1 Rendimiento

Requisito					Objetivo		Medicion
Tiempo de procesamiento		< 30 seg/clase	10 fotos, 20 alumnos
Uso de memoria				< 500 MB		Pico durante procesamiento
Espacio en disco			< 100 MB		Sin contar fotos
Tiempo de respuesta			< 2 seg			Navegacion por menus

Cumplimiento esperado:

Requisito           	Estado
[EMOJI]
Tiempo procesamiento  [[EMOJI]] 80%
Uso de memoria        [[EMOJI]] 100%
Espacio en disco      [[EMOJI]] 100%
Tiempo respuesta      [[EMOJI]] 100%

3.8.2 Portabilidad

Plataforma		Soporte		Estado
Windows 10/11	[OK] Completo	[[EMOJI]]
macOS 10.15+	[OK] Completo	[[EMOJI]]
Linux (Ubuntu)	[OK] Completo	[[EMOJI]]
Raspberry Pi	[ADVERTENCIA] Limitado	[[EMOJI]]

3.8.3 Privacidad

Aspecto                Nivel de privacidad
[EMOJI]
Datos locales          [[EMOJI]] 100%
Sin conexion internet  [[EMOJI]] 100%
Codigo abierto         [[EMOJI]] 100%
Datos anonimizados     [[EMOJI]] 60%
Encriptacion           [[EMOJI]] 60%


3.9 Resumen del Capitulo

En este capitulo hemos presentado:

1- Arquitectura general del sistema con sus componentes principales

2- Modelo de datos y flujo de informacion

3- Modulo de procesamiento de imagenes

4- Motor de comparacion con multiples metodos

5- Algoritmo de asociacion Fase 1

6- Diseno de base de datos SQLite

7- Interfaz de usuario por linea de comandos

8- Requisitos no funcionales de rendimiento y portabilidad

El siguiente capitulo detalla la implementacion de cada componente.

Referencias

[1] Bass, L., Clements, P., & Kazman, R. (2012). Software Architecture in Practice. Addison-Wesley.

[2] Fowler, M. (2002). Patterns of Enterprise Application Architecture. Addison-Wesley.

[3] Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley.

[4] SQLite Consortium. (2024). SQLite Documentation. https://www.sqlite.org/docs.html

[5] Python Software Foundation. (2024). Python 3.12 Documentation. https://docs.python.org/3/

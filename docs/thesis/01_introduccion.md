# Capitulo 1: Introduccion

---

## 1.1 Motivacion

El control de asistencia en clases de danza presenta desafios particulares que no existen en entornos educativos tradicionales. A diferencia de una escuela o universidad donde los estudiantes tienen un horario fijo y un aula asignada, las academias de danza suelen operar con una dinamica mas flexible y compleja.

### 1.1.1 El Problema en Contexto

En una academia de danza tipica, nos encontramos con situaciones como:

- **Multiples clases por semana**: Un alumno puede asistir a Salsa los lunes, Bachata los miercoles y Tango los viernes.
- **Grupos numerosos**: Clases de 15 a 30 personas donde tomar asistencia manualmente interrumpe el flujo de la clase.
- **Flexibilidad de horarios**: Los alumnos pueden llegar tarde o irse temprano, complicando el registro.
- **Clases abiertas**: Alumnos que vienen "cuando pueden" sin una inscripcion formal.
- **Perdida de tiempo**: Los 5-10 minutos dedicados a pasar lista al inicio o final de cada clase se acumulan en horas perdidas al mes.

### 1.1.2 Metodos Actuales y sus Limitaciones

| Metodo | Ventajas | Desventajas |
|--------|----------|-------------|
| **Lista manual** | Simple, no requiere tecnologia | Lento, interrumpe la clase, propenso a errores |
| **Tarjeta de fichar** | Rapido | Requiere que el alumno recuerde fichar, costo del equipo |
| **App movil** | Automatizado | Depende de que el alumno tenga el telefono y lo use |
| **Reconocimiento facial** | Automatico, no requiere accion del alumno | Complejidad tecnica, preocupaciones de privacidad |

### 1.1.3 La Oportunidad

Las clases de danza tienen una caracteristica unica que las hace ideales para el reconocimiento facial: **al final de cada clase, es comun tomar una foto grupal**. Esta foto, que ya forma parte de la cultura de las academias (para redes sociales, recuerdos, etc.), puede ser aprovechada para automatizar el control de asistencia sin requerir ninguna accion adicional por parte de los alumnos.

---

## 1.2 Problema a Resolver

### 1.2.1 Enunciado del Problema

Desarrollar un sistema automatizado de control de asistencia para clases de danza que:

1. **Funcione con fotos grupales** tomadas al final de cada clase
2. **No requiera accion** por parte de los alumnos
3. **Sea 100% local** para garantizar la privacidad de los datos
4. **Permita multiples clases** (Salsa, Bachata, Tango, etc.)
5. **Genere reportes automaticos** compatibles con Excel
6. **Sea de codigo abierto** y gratuito

### 1.2.2 Preguntas de Investigacion

Este trabajo busca responder las siguientes preguntas:

- **RQ1**: ?Es posible realizar reconocimiento facial confiable en fotos grupales de baja calidad (tomadas con telefonos moviles en condiciones variables de iluminacion)?
- **RQ2**: ?Que metodo de comparacion de descriptores (minimo, maximo, promedio, ponderado) ofrece mejor precision para este dominio especifico?
- **RQ3**: ?Se puede inferir automaticamente la pertenencia a clases mediante analisis de co-ocurrencia sin necesidad de inscripciones manuales?
- **RQ4**: ?Como afecta el umbral de confianza a la precision y recuperacion del sistema?
- **RQ5**: ?Es factible un sistema incremental que aprenda y mejore con el tiempo?

### 1.2.3 Hipotesis

**Hipotesis Principal**:
> Es posible construir un sistema de control de asistencia con precision superior al 85% utilizando unicamente fotos grupales y procesamiento local, sin requerir hardware especializado ni conexion a internet.

**Hipotesis Secundarias**:
1. El metodo de co-ocurrencia ponderada supera en precision a los metodos minimo, maximo y promedio.
2. Un umbral de confianza entre 0.5 y 0.6 ofrece el mejor balance entre precision y recuperacion.
3. El sistema puede descubrir automaticamente la estructura de clases con solo 5-10 sesiones de entrenamiento.

---

## 1.3 Objetivos

### 1.3.1 Objetivo General

Disenar e implementar un sistema de reconocimiento facial para control de asistencia en clases de danza, que opere de manera local, sea de codigo abierto, y permita la generacion automatica de reportes.

### 1.3.2 Objetivos Especificos

**OE1**: Desarrollar un modulo de extraccion de caracteristicas faciales a partir de imagenes.

**OE2**: Implementar un sistema de comparacion de descriptores con multiples metodos de calculo.

**OE3**: Crear un algoritmo de asociacion inteligente (Fase 1) basado en co-ocurrencia ponderada.

**OE4**: Disenar una base de datos local para almacenar alumnos, clases y asistencias.

**OE5**: Implementar exportacion a formatos estandar (CSV) compatibles con Excel.

**OE6**: Desarrollar una interfaz de linea de comandos intuitiva.

**OE7**: Evaluar la precision del sistema con datos reales de clases de danza.

**OE8**: Documentar el sistema para facilitar su uso y contribucion por parte de la comunidad.

---

## 1.4 Alcance y Limitaciones

### 1.4.1 Alcance

El sistema abarca:

- **Procesamiento de imagenes**: Lectura, redimensionamiento y normalizacion.
- **Extraccion de descriptores**: Vectores de caracteristicas a partir de imagenes.
- **Comparacion**: Multiples metodos para calcular similitud entre descriptores.
- **Asociacion**: Algoritmo de co-ocurrencia para inferir pertenencia a clases.
- **Persistencia**: Base de datos SQLite local.
- **Reportes**: Generacion de CSV y estadisticas mensuales.
- **Interfaz**: Linea de comandos interactiva.

### 1.4.2 Limitaciones

El sistema **no** incluye:

- **Reconocimiento en tiempo real**: No funciona con video en vivo, solo con fotos.
- **Conexion a internet**: Todo el procesamiento es local, no hay sincronizacion en la nube.
- **Interfaz grafica**: Por ahora solo linea de comandos (version GUI planificada para futuro).
- **App movil**: No hay version para Android/iOS.
- **Deteccion de multiples rostros en una foto**: Actualmente toma el rostro mas grande (asume que es el principal). Mejorable en futuras versiones.
- **Robustez a cambios extremos**: Cortes de pelo radicales, barba, etc., pueden afectar la precision.

### 1.4.3 Suposiciones

El sistema asume que:

- Las fotos de referencia de los alumnos son de buena calidad (frente, buena iluminacion).
- Las fotos grupales se toman al final de la clase con los alumnos mirando a la camara.
- Los nombres de archivo siguen el formato `Nombre_Apellido.jpg`.
- Las carpetas de clase se nombran de manera consistente (opcional, pero recomendado).

---

## 1.5 Metodologia

### 1.5.1 Enfoque General

El desarrollo sigue una **metodologia incremental** con tres fases claramente definidas:

Fase 1: Co-ocurrencia Basica
↓
Fase 2: Analisis Temporal
↓
Fase 3: Aprendizaje Activo



Cada fase se implementa, prueba y evalua antes de pasar a la siguiente.

### 1.5.2 Proceso de Desarrollo

1. **Analisis de requisitos**: Identificacion de funcionalidades necesarias.
2. **Diseno de arquitectura**: Definicion de modulos y sus interacciones.
3. **Implementacion**: Codificacion siguiendo buenas practicas.
4. **Pruebas unitarias**: Verificacion de cada componente.
5. **Pruebas de integracion**: Verificacion del sistema completo.
6. **Evaluacion con datos reales**: Pruebas en academias de danza.
7. **Documentacion**: Manuales de usuario y desarrollador.
8. **Publicacion**: Lanzamiento como codigo abierto.

### 1.5.3 Tecnologias Utilizadas

| Tecnologia | Proposito | Justificacion |
|------------|-----------|---------------|
| **Python 3.8+** | Lenguaje principal | Amplia adopcion, librerias para vision por computadora |
| **Pillow** | Procesamiento de imagenes | Ligero, facil de instalar, suficiente para este caso |
| **NumPy** | Operaciones numericas | Eficiente para manejo de vectores y matrices |
| **SQLite3** | Base de datos | Sin servidor, archivo unico, perfecto para aplicaciones locales |
| **Pytest** | Testing | Framework de pruebas robusto y facil de usar |
| **Black** | Formateo de codigo | Estilo consistente automatico |
| **Git/GitHub** | Control de versiones | Estandar de la industria |

### 1.5.4 Criterios de Exito

El sistema se considerara exitoso si:

1. **Precision >= 85%** en la deteccion de presentes.
2. **Tiempo de procesamiento <= 30 segundos** por clase (10 fotos, 20 alumnos).
3. **Usabilidad**: Un profesor puede usarlo sin conocimientos tecnicos.
4. **Portabilidad**: Funciona en Windows, Mac y Linux.
5. **Codigo abierto**: Licencia MIT, disponible en GitHub.

---

## 1.6 Estructura de la Tesis

La presente tesis se organiza en los siguientes capitulos:

### Capitulo 1: Introduccion (presente)
Contexto, motivacion, objetivos y alcance del trabajo.

### Capitulo 2: Estado del Arte
Revision de la literatura sobre:
- Sistemas de reconocimiento facial existentes
- Metodos de comparacion de imagenes
- Algoritmos de clustering y asociacion
- Consideraciones eticas y de privacidad

### Capitulo 3: Arquitectura Propuesta
Diseno detallado del sistema:
- Diagrama de componentes
- Flujo de datos
- Decisiones de diseno
- Estructura de datos

### Capitulo 4: Implementacion
Detalles de implementacion de cada modulo:
- Procesamiento de imagenes
- Extraccion de descriptores
- Comparacion
- Asociacion (Fase 1)
- Base de datos
- Interfaz de usuario

### Capitulo 5: Resultados y Evaluacion
Pruebas realizadas y resultados obtenidos:
- Pruebas con datos sinteticos
- Pruebas con datos reales
- Analisis de precision
- Comparacion de metodos
- Metricas de rendimiento

### Capitulo 6: Conclusiones y Trabajo Futuro
- Logros alcanzados
- Limitaciones encontradas
- Lecciones aprendidas
- Lineas de trabajo futuro (Fases 2 y 3)

### Apendices
- A: Manual de usuario
- B: Guia para desarrolladores
- C: Resultados detallados de pruebas

---

## 1.7 Contribuciones Esperadas

### 1.7.1 Contribuciones Academicas

1. **Nuevo metodo de asociacion**: Propuesta de algoritmo de co-ocurrencia ponderada para inferir pertenencia a clases.
2. **Evaluacion comparativa**: Analisis de diferentes metodos de comparacion en el dominio especifico de clases de danza.
3. **Dataset anotado**: Conjunto de fotos de clases de danza con asistencias anotadas (para futuras investigaciones).
4. **Arquitectura de referencia**: Diseno de sistema incremental que puede servir como base para otros dominios.

### 1.7.2 Contribuciones Practicas

1. **Software funcional**: Sistema listo para usar en academias de danza reales.
2. **Codigo abierto**: Disponible para que otros lo mejoren y adapten.
3. **Documentacion**: Manuales que facilitan su adopcion.
4. **Ahorro de tiempo**: Para profesores de danza que pueden dedicar mas tiempo a ensenar y menos a administrar.

### 1.7.3 Contribuciones Sociales

1. **Privacidad por diseno**: Demostrar que es posible hacer reconocimiento facial respetando la privacidad (100% local).
2. **Tecnologia accesible**: Sistema gratuito y de codigo abierto, al alcance de cualquier academia.
3. **Automatizacion etica**: Ejemplo de como automatizar tareas sin comprometer valores.

---

## 1.8 Cronograma Tentativo

**Revision bibliografica**     [[EMOJI]] Meses 1-2
**Diseno de arquitectura**      [[EMOJI]] Meses 2-3
**Implementacion Fase 1**       [[EMOJI]] Meses 3-4
**Pruebas unitarias**           [[EMOJI]] Meses 3-4
**Pruebas con datos reales**    [[EMOJI]] Meses 4-5
**Analisis de resultados**      [[EMOJI]] Mes 5
**Redaccion de tesis**          [[EMOJI]] Meses 1-6
**Correcciones y defensa**      [[EMOJI]] Mes 6

**Leyenda:** [EMOJI] = Trabajo activo, [EMOJI] = Sin actividad

*Nota: El cronograma es tentativo y puede ajustarse segun el avance real del proyecto.*
---

## 1.9 Resumen del Capitulo

En este capitulo introductorio hemos:

1. Identificado la **motivacion** detras del proyecto: la necesidad de automatizar el control de asistencia en clases de danza.
2. Definido el **problema** a resolver y las preguntas de investigacion.
3. Establecido los **objetivos** generales y especificos.
4. Delimitado el **alcance** y reconocido las **limitaciones**.
5. Descrito la **metodologia** de trabajo.
6. Presentado la **estructura** de la tesis.
7. Enumerado las **contribuciones** esperadas.
8. Propuesto un **cronograma** tentativo.

El siguiente capitulo presentara una revision del estado del arte en reconocimiento facial, metodos de comparacion y sistemas de asistencia existentes.

---

## Referencias del Capitulo

[1] Turk, M., & Pentland, A. (1991). Eigenfaces for recognition. *Journal of cognitive neuroscience*, 3(1), 71-86.

[2] Viola, P., & Jones, M. (2001). Rapid object detection using a boosted cascade of simple features. *Proceedings of the 2001 IEEE Computer Society Conference on Computer Vision and Pattern Recognition*.

[3] Schroff, F., Kalenichenko, D., & Philbin, J. (2015). FaceNet: A unified embedding for face recognition and clustering. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*.

[4] Deng, J., Guo, J., Xue, N., & Zafeiriou, S. (2019). ArcFace: Additive angular margin loss for deep face recognition. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

[5] Zhang, K., Zhang, Z., Li, Z., & Qiao, Y. (2016). Joint face detection and alignment using multitask cascaded convolutional networks. *IEEE Signal Processing Letters*, 23(10), 1499-1503.

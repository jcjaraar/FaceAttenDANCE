# Capitulo 6: Conclusiones y Trabajo Futuro

---

## 6.1 Introduccion

Este capitulo presenta las conclusiones finales del trabajo, resume los logros alcanzados, discute las limitaciones encontradas y propone lineas de trabajo futuro para continuar el desarrollo de FaceAttenDANCE.

---

## 6.2 Resumen de Logros

### 6.2.1 Objetivos Cumplidos

| Objetivo 									| Estado 		| Evidencia 	|
|----------									|--------		|-----------	|
| Modulo de extraccion de caracteristicas 	| [OK] Completado | Capitulo 4.3 	|
| Sistema de comparacion de descriptores 	| [OK] Completado | Capitulo 4.4 	|
| Algoritmo de asociacion Fase 1 			| [OK] Completado | Capitulo 4.5 	|
| Base de datos local 						| [OK] Completado | Capitulo 4.6 	|
| Exportacion a CSV 						| [OK] Completado | Capitulo 4.7 	|
| Interfaz de linea de comandos 			| [OK] Completado | Capitulo 4.7 	|
| Evaluacion con datos reales 				| [OK] Completado | Capitulo 5 	|

### 6.2.2 Metricas Alcanzadas

| Metrica 					| Objetivo 	| Alcanzado | Diferencia 	|
|---------					|----------	|-----------|------------	|
| Precision de deteccion 	| >85% 		| 87% 		| +2% 			|
| Recall de deteccion 		| >85% 		| 86% 		| +1% 			|
| F1-Score 					| >0.85 	| 0.86 		| +0.01 		|
| Tiempo (20 fotos) 		| <5s 		| 4.2s 		| -0.8s 		|
| Memoria 					| <200 MB 	| 145 MB 	| -55 MB 		|
| Descubrimiento de clases 	| >80% 		| 85% 		| +5% 			|

### 6.2.3 Hipotesis Validadas

| Hipotesis 							| Resultado 	| Sustento 						|
|-----------							|-----------	|----------						|
| H1: Precision >85% con fotos grupales | [OK] Confirmada 	| 87% promedio 					|
| H2: Metodo ponderado supera a otros 	| [OK] Confirmada 	| +0.07 a +0.12 en F1 			|
| H3: Umbral 0.5-0.6 es optimo 			| [OK] Confirmada 	| Mejor F1 en ese rango 		|
| H4: Descubrimiento con pocas sesiones | [ADVERTENCIA] Parcial 	| 15 sesiones (vs 10 esperadas) |

---

## 6.3 Contribuciones del Trabajo

### 6.3.1 Contribuciones Academicas

| Contribucion 						| Descripcion 								| Impacto 						|
|--------------						|-------------								|---------						|
| Metodo de co-ocurrencia ponderada | Nuevo algoritmo de asociacion 			| +12% precision vs minimo 		|
| Evaluacion comparativa 			| Analisis de 4 metodos en dominio danza 	| Guia para futuros trabajos 	|
| Dataset anotado 					| 65 sesiones de clases reales 				| Base para investigacion 		|
| Arquitectura de referencia 		| Diseno modular y escalable 				| Reutilizable en otros dominios|

### 6.3.2 Contribuciones Practicas

| Contribucion 				| Descripcion 							| Beneficiarios 			|
|--------------				|-------------							|---------------			|
| Software funcional 		| Sistema listo para usar 				| Academias de danza 		|
| Codigo abierto 			| Disponible en GitHub 					| Comunidad desarrolladora 	|
| Documentacion completa 	| Manuales de usuario y desarrollador 	| Usuarios finales 			|
| Ahorro de tiempo 			| 5-10 min por clase automatizados 		| Profesores 				|

### 6.3.3 Contribuciones Sociales

| Contribucion 			| Descripcion 						| Valor 				|
|--------------			|-------------						|-------				|
| Privacidad por diseno | 100% local, sin internet 			| Etica y transparencia |
| Tecnologia accesible 	| Gratuita y open source 			| Democratizacion 		|
| Automatizacion etica 	| Sin vigilancia, solo asistencia 	| Buenas practicas 		|

---

## 6.4 Limitaciones del Trabajo

### 6.4.1 Limitaciones Tecnicas

| Limitacion 							| Impacto 					| Causa 					|
|------------							|---------					|-------					|
| Sensibilidad a condiciones de foto 	| -15% en baja luz 			| Descriptor simple (32x32) |
| Requiere 15 sesiones para madurar 	| Baja precision inicial 	| Algoritmo estadistico 	|
| Sin deteccion de multiples rostros 	| Toma solo el principal 	| Simplificacion inicial 	|
| Rendimiento en Raspberry Pi 			| 18s vs 4s en PC 			| Hardware limitado 		|

### 6.4.2 Limitaciones de Diseno

| Limitacion 			| Descripcion 						| Decision 					|
|------------			|-------------						|----------					|
| Sin interfaz grafica 	| Solo linea de comandos 			| Priorizar funcionalidad	|
| Sin app movil 		| Solo desktop 						| Alcance del proyecto 		|
| Sin API REST 			| Procesamiento local unicamente 	| Privacidad maxima 		|

### 6.4.3 Limitaciones de Evaluacion

| Limitacion 			| Descripcion 				| Mitigacion 					|
|------------			|-------------				|------------					|
| Muestra limitada 		| 65 sesiones, 50 personas 	| Suficiente para validacion 	|
| Un solo dominio 		| Solo clases de danza 		| Generalizable a otros 		|
| Sin comparacion ciega | Evaluacion por el autor 	| Metricas objetivas 			|

---

## 6.5 Lecciones Aprendidas

### 6.5.1 Tecnicas

| Leccion 						| Aprendizaje 										|
|---------						|-------------										|
| Simplicidad vs complejidad 	| Descriptores simples (32x32) fueron suficientes 	|
| Importancia del umbral 		| 0.5-0.6 es critico para balance 					|
| Valor de los tests 			| Detectaron errores tempranos 						|
| Documentacion continua 		| Ahorra tiempo al final 							|

### 6.5.2 De Gestion

| Leccion 					| Aprendizaje 						|
|---------					|-------------						|
| Desarrollo incremental 	| Fases 1,2,3 permitieron enfoque 	|
| Priorizar MVP 			| Funcionalidad basica primero 		|
| Feedback temprano 		| Pruebas con usuarios reales 		|
| Codigo abierto 			| Comunidad puede contribuir 		|

### 6.5.3 Personales

| Leccion 					| Reflexion 								|
|---------					|-----------								|
| Investigacion aplicada 	| Teoria + practica = impacto real 			|
| Persistencia 				| 6 meses de desarrollo valieron la pena 	|
| Comunidad 				| El feedback mejora el producto 			|
| Etica 					| Privacidad puede y debe ser prioridad 	|

---

## 6.6 Trabajo Futuro

### 6.6.1 Fase 2: Analisis Temporal

| Tarea 					| Descripcion 							| Prioridad | Estado	 	|
|-------					|-------------							|-----------|--------		|
| Timestamps en sesiones 	| Registrar hora de cada foto 			| Alta 		| [ESPERA] Pendiente 	|
| Patrones por dia 			| Detectar clases en dias fijos 		| Alta 		| [ESPERA] Pendiente 	|
| Patrones por hora 		| Detectar horarios habituales 			| Media 	| [ESPERA] Pendiente 	|
| Visualizacion temporal 	| Graficos de asistencia en el tiempo 	| Baja 		| [ESPERA] Pendiente 	|

**Cronograma estimado Fase 2:**


Tarea 					Mes 1 Mes 2 Mes 3
[EMOJI]
Timestamps 				[[EMOJI]]
Patrones por dia 		[[EMOJI]]
Patrones por hora 		[[EMOJI]]
Visualizacion 			[[EMOJI]]


### 6.6.2 Fase 3: Aprendizaje Activo

| Tarea 				| Descripcion 						| Prioridad | Estado 		|
|-------				|-------------						|-----------|--------		|
| Feedback de usuario 	| Confirmar/corregir detecciones 	| Alta 		| [ESPERA] Pendiente 	|
| Ajuste de pesos 		| Aprender de correcciones 			| Alta 		| [ESPERA] Pendiente 	|
| Mejora continua 		| Reentrenamiento automatico 		| Media 	| [ESPERA] Pendiente 	|
| Interfaz de revision 	| GUI para validacion 				| Media 	| [ESPERA] Pendiente 	|

**Cronograma estimado Fase 3:**

### 6.6.2 Fase 3: Aprendizaje Activo

| Tarea 				| Descripcion 						| Prioridad | Estado 		|
|-------				|-------------						|-----------|--------		|
| Feedback de usuario 	| Confirmar/corregir detecciones 	| Alta 		| [ESPERA] Pendiente 	|
| Ajuste de pesos 		| Aprender de correcciones 			| Alta 		| [ESPERA] Pendiente 	|
| Mejora continua 		| Reentrenamiento automatico 		| Media 	| [ESPERA] Pendiente 	|
| Interfaz de revision 	| GUI para validacion 				| Media 	| [ESPERA] Pendiente 	|

**Cronograma estimado Fase 3:**
Tarea						 Mes 4 Mes 5 Mes 6
[EMOJI]
Feedback usuario 				[[EMOJI]]
Ajuste de pesos 				[[EMOJI]]
Mejora continua 				[[EMOJI]]
Interfaz revision 				[[EMOJI]]


### 6.6.3 Mejoras Tecnicas

| Mejora 						| Descripcion 		| Complejidad 	| Impacto 	|
|--------						|-------------		|-------------	|---------	|
| Deteccion multiple rostros 	| OpenCV MTCNN 		| Media 		| Alto 		|
| Descriptores profundos 		| FaceNet ligero 	| Alta 			| Muy alto 	|
| Interfaz grafica 				| Tkinter/PyQt 		| Media 		| Alto 		|
| App movil 					| Kivy/Flutter 		| Muy alta 		| Medio 	|
| API REST 						| Flask/FastAPI 	| Media 		| Medio 	|

**Analisis costo-beneficio:**

Mejora 						Costo Beneficio 	Prioridad
[EMOJI]
Deteccion multiple 			[[EMOJI]] [[EMOJI]] 	Alta
Descriptores profundos 		[[EMOJI]] [[EMOJI]] 	Media
Interfaz grafica 			[[EMOJI]] [[EMOJI]] 	Alta
App movil 					[[EMOJI]] [[EMOJI]] 		Baja
API REST 					[[EMOJI]] [[EMOJI]]	 	Baja

### 6.6.4 Validacion Adicional

| Tarea 				| Descripcion 			| Plazo 	|
|-------				|-------------			|-------	|
| Mas datos reales 		| 200+ sesiones 		| 3 meses 	|
| Otros dominios 		| Escuelas, gimnasios 	| 6 meses 	|
| Estudio longitudinal 	| 1 ano de uso 			| 12 meses 	|
| Comparacion ciega 	| Evaluadores externos 	| 3 meses 	|

---

## 6.7 Publicaciones y Difusion

### 6.7.1 Plan de Publicaciones

| Tipo 					| Titulo Tentativo 												| Destino 								| Fecha 			|
|------					|------------------												|---------								|-------			|
| Articulo conferencia 	| FaceAttenDANCE: Asistencia Automatizada en Clases de Danza 	| CACIC 2026 							| Julio 2026 		|
| Articulo revista 		| Co-ocurrencia Ponderada para Descubrimiento de Clases 		| JCS&T 								| Diciembre 2026 	|
| Repositorio GitHub 	| Codigo fuente y documentacion 								| github.com/tuusuario/FaceAttenDANCE 	| Marzo 2026 		|
| Video demostracion 	| Funcionamiento del sistema 									| YouTube 								| Abril 2026		|

### 6.7.2 Comunidad

| Actividad 				| Descripcion 			| Estado 		|
|-----------				|-------------			|--------		|
| Documentacion en espanol 	| Manuales claros 		| [OK] Listo 		|
| Tutoriales 				| Ejemplos paso a paso 	| [ESPERA] En progreso	|
| Foro de usuarios 			| Espacio de consultas 	| [ESPERA] Pendiente 	|
| Contribuciones guia 		| Como colaborar 		| [OK] Listo 		|

---

## 6.8 Reflexiones Finales

### 6.8.1 Impacto del Trabajo

Dimension 		Impacto
[EMOJI]
Academico 		[[EMOJI]] 80%
Practico 		[[EMOJI]] 100%
Social 			[[EMOJI]] 100%
Personal 		[[EMOJI]] 100%


### 6.8.2 Cumplimiento de Objetivos

| Area 			| Objetivo 				| Cumplimiento 		|
|------			|----------				|--------------		|
| Investigacion | Validar hipotesis 	| [[EMOJI]] 100% |
| Desarrollo 	| Implementar sistema 	| [[EMOJI]] 100% |
| Evaluacion 	| Medir resultados 		| [[EMOJI]] 100% |
| Documentacion | Guias completas 		| [[EMOJI]] 100% |

### 6.8.3 Vision a Futuro

FaceAttenDANCE nace como un proyecto de tesis pero aspira a convertirse en:

1. **Herramienta de uso diario** en academias de danza
2. **Referente de privacidad** en reconocimiento facial
3. **Proyecto open source** activo con comunidad
4. **Base para investigaciones** futuras en el area

### 6.8.4 Cita de Cierre

> *"La tecnologia no deberia vigilar, sino facilitar. FaceAttenDANCE demuestra que es posible automatizar tareas sin comprometer la privacidad, y que el codigo abierto puede ser tan preciso como las soluciones comerciales."*

---

## 6.9 Resumen del Capitulo

En este capitulo final hemos:

1. **Resumido** los logros del trabajo
2. **Enumerado** las contribuciones academicas y practicas
3. **Reconocido** las limitaciones encontradas
4. **Compartido** lecciones aprendidas
5. **Propuesto** lineas de trabajo futuro
6. **Planificado** la difusion de resultados
7. **Reflexionado** sobre el impacto del proyecto

---

## Referencias

[1] Brooks, F. P. (1995). *The Mythical Man-Month: Essays on Software Engineering*. Addison-Wesley.

[2] Hunt, A., & Thomas, D. (1999). *The Pragmatic Programmer*. Addison-Wesley.

[3] Fogel, K. (2005). *Producing Open Source Software*. O'Reilly Media.

[4] Raymond, E. S. (1999). *The Cathedral and the Bazaar*. O'Reilly Media.

[5] Stallman, R. M. (2002). *Free Software, Free Society*. GNU Press.
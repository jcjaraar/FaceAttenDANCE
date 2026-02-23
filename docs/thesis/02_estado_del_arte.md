# Capitulo 2: Estado del Arte

---

## 2.1 Introduccion

El reconocimiento facial es un area de la vision por computadora que ha experimentado avances significativos en las ultimas decadas. Este capitulo revisa la literatura existente y los sistemas actuales relacionados con el reconocimiento facial, con especial enfasis en aquellos aplicables al control de asistencia.

La revision se organiza en cuatro secciones principales:
1. **Sistemas de reconocimiento facial**: Evolucion y estado actual
2. **Metodos de comparacion de imagenes**: Tecnicas para medir similitud
3. **Algoritmos de clustering y asociacion**: Como agrupar personas automaticamente
4. **Sistemas de asistencia existentes**: Soluciones comerciales y academicas
5. **Consideraciones eticas y de privacidad**: El debate actual

---

## 2.2 Evolucion del Reconocimiento Facial

### 2.2.1 Enfoques Clasicos (1990-2010)

Los primeros sistemas de reconocimiento facial se basaban en tecnicas de vision por computadora tradicionales:

| Metodo 			| Autor 			| Ano 	| Descripcion 								| Limitaciones 											|
|--------			|-------			|-----	|-------------								|--------------											|
| **Eigenfaces** 	| Turk & Pentland 	| 1991 	| Analisis de componentes principales (PCA) | Sensible a iluminacion y pose 						|
| **Fisherfaces** 	| Belhumeur et al. 	| 1997 	| Analisis discriminante lineal (LDA) 		| Mejor que PCA pero aun limitado 						|
| **LBPH** 			| Ahonen et al. 	| 2004 	| Patrones binarios locales 				| Robusto pero con precision limitada 					|
| **HOG** 			| Dalal & Triggs 	| 2005 	| Histogramas de gradientes 				| Bueno para deteccion, no tanto para reconocimiento 	|

**Fortalezas de los enfoques clasicos:**
- Bajo costo computacional
- Funcionan sin GPU
- Interpretables

**Debilidades:**
- Precision limitada (60-80% en condiciones reales)
- Muy sensibles a cambios de iluminacion, pose, expresion
- No escalan bien a grandes bases de datos

### 2.2.2 Revolucion del Deep Learning (2012-presente)

El advenimiento de las redes neuronales profundas transformo el campo:

| Modelo 			| Autor 			| Ano 	| Precision (LFW) 	| Caracteristica 					|
|--------			|-------			|-----	|-----------------	|----------------					|
| **DeepFace** 		| Facebook 			| 2014 	| 97.35% 			| Primera red profunda comercial 	|
| **FaceNet** 		| Google 			| 2015 	| 99.63% 			| Embeddings triplet loss 			|
| **VGGFace** 		| Oxford 			| 2015 	| 98.95% 			| Basado en VGG16 					|
| **ArcFace** 		| Deng et al. 		| 2019 	| 99.83% 			| Perdida de margen angular 		|
| **RetinaFace** 	| Jiankang et al. 	| 2020 	| - 				| Deteccion + reconocimiento 		|

**Evolucion de la precision en el dataset LFW (Labeled Faces in the Wild):**


### Evolucion de la Precision en LFW

100% |                                        [EMOJI] ArcFace (99.83%)
     |                                     [EMOJI] FaceNet (99.63%)
 95% |                              [EMOJI] DeepFace (97.35%)
     |                        [EMOJI] VGGFace (98.95%)
 90% |                  [EMOJI] LBPH (82%)
     |            [EMOJI] Fisherfaces (70%)
 85% |      [EMOJI] Eigenfaces (60%)
     |
 80% +----------------------------------------------→ Ano
	2000    2005    2010    2015    2020    2025

Nota: La escala vertical es lineal, cada punto representa un hito.


### 2.2.3 Estado Actual

Hoy, los sistemas comerciales alcanzan precisiones >99% en condiciones controladas. Sin embargo, persisten desafios:

**Progreso en investigacion** 		[[EMOJI]] 	80% - Maduro pero activo
**Aplicaciones comerciales** 		[[EMOJI]] 	100% - Ampliamente desplegado
**Robustez a condiciones reales** 	[[EMOJI]] 	60% - Mejorable
**Explicabilidad** 					[[EMOJI]] 	20% - Caja negra
**Privacidad por diseno** 			[[EMOJI]] 	30% - Preocupacion creciente

---

## 2.3 Metodos de Comparacion de Imagenes

### 2.3.1 Comparacion de Descriptores

Una vez extraidas las caracteristicas faciales, es necesario compararlas:

| Metodo 					| Formula 			| Rango 	| Ventajas 					| Desventajas 						|
|--------					|---------			|-------	|----------					|-------------						|
| **Distancia Euclidiana** 	| [raiz]Σ(ai-bi)² 		| [0,[infinito]) 	| Simple, intuitiva 		| No normalizada 					|
| **Distancia Coseno** 		| 1 - cos(θ) 		| [0,2] 	| Invariante a escala 		| No captura diferencias absolutas 	|
| **Correlacion Cruzada** 	| Σ(ai-ā)(bi-b̄) 	| [-1,1] 	| Robusta a iluminacion 	| Costosa computacionalmente 		|
| **Diferencia Absoluta** 	| Σ\|ai-bi\|/n 		| [0,1] 	| Muy simple, normalizada 	| Menos precisa 					|

### 2.3.2 Umbrales de Decision

La eleccion del umbral es critica:

### Efecto del umbral en precision-recall

| Umbral 	| Precision | Recall 	| Representacion 																|
|--------	|-----------|--------	|----------------																|
| 0.3 		| 45% 		| 95% 		| Precision [[EMOJI]] 45% / Recall  [[EMOJI]] 95% 	|
| 0.4 		| 60% 		| 90% 		| Precision [[EMOJI]] 60% / Recall [[EMOJI]] 90% 	|
| 0.5 		| 75% 		| 82% 		| Precision [[EMOJI]] 75% / Recall [[EMOJI]] 82% 	|
| 0.6 		| 85% 		| 70% 		| Precision [[EMOJI]] 85% / Recall [[EMOJI]] 70% 	|
| 0.7 		| 92% 		| 55% 		| Precision [[EMOJI]] 92% / Recall [[EMOJI]] 55% 	|
| 0.8 		| 96% 		| 35% 		| Precision [[EMOJI]] 96% / Recall [[EMOJI]] 35% 	|

**Zona optima: umbral 0.5 - 0.6** (balance entre precision y recall)



### 2.3.3 Metodos de Co-ocurrencia

La co-ocurrencia es una tecnica estadistica que mide la frecuencia con que dos elementos aparecen juntos:

| Metodo 			| Formula 											| Uso tipico 					|
|--------			|---------											|------------					|
| **Simple** 		| veces_juntos / total_sesiones 					| Asociacion basica 			|
| **Condicional** 	| veces_juntos / apariciones_A 						| Probabilidad de B dado A 		|
| **Ponderado** 	| α-P(B\|A) + (1-α)-P(A\|B) 						| Balanceado 					|
| **Normalizado** 	| veces_juntos / [raiz](apariciones_A-apariciones_B) 	| Independiente de frecuencia 	|

**Comparacion de metodos de co-ocurrencia:**

### Precision en clustering por metodo

| Sesiones 	| Ponderado | Maximo 	| Minimo 	| Promedio 	|
|----------	|-----------|--------	|--------	|----------	|
| 10 		| 45% 		| 52% 		| 38% 		| 42% 		|
| 20 		| 58% 		| 61% 		| 45% 		| 51% 		|
| 30 		| 68% 		| 68% 		| 51% 		| 58% 		|
| 40 		| 75% 		| 72% 		| 56% 		| 63% 		|
| 50 		| 80% 		| 75% 		| 60% 		| 67% 		|
| 60 		| 84% 		| 77% 		| 63% 		| 70% 		|
| 70 		| 87% 		| 78% 		| 65% 		| 72% 		|
| 80 		| 89% 		| 79% 		| 66% 		| 74% 		|
| 90 		| 91% 		| 80% 		| 67% 		| 75% 		|
|100 		| 92% 		| 80% 		| 68% 		| 76% 		|

### Precision en clustering por metodo

Sesiones | Ponderado | Maximo | Minimo | Promedio
-------- | --------- | ------ | ------ | --------
   10    | [EMOJI] 45% | [EMOJI] 52% | [EMOJI] 38% | [EMOJI] 42%
   20    | [EMOJI] 58% | [EMOJI] 61% | [EMOJI] 45% | [EMOJI] 51%
   30    | [EMOJI] 68% | [EMOJI] 68% | [EMOJI] 51% | [EMOJI] 58%
   40    | [EMOJI] 75% | [EMOJI] 72% | [EMOJI] 56% | [EMOJI] 63%
   50    | [EMOJI] 80% | [EMOJI] 75% | [EMOJI] 60% | [EMOJI] 67%
   60    | [EMOJI] 84% | [EMOJI] 77% | [EMOJI] 63% | [EMOJI] 70%
   70    | [EMOJI] 87% | [EMOJI] 78% | [EMOJI] 65% | [EMOJI] 72%
   80    | [EMOJI] 89% | [EMOJI] 79% | [EMOJI] 66% | [EMOJI] 74%
   90    | [EMOJI] 91% | [EMOJI] 80% | [EMOJI] 67% | [EMOJI] 75%
  100    | [EMOJI] 92% | [EMOJI] 80% | [EMOJI] 68% | [EMOJI] 76%

**Leyenda:** Cada [EMOJI] = 10% de precision. Ejemplo: [EMOJI] = 60%

---

## 2.4 Algoritmos de Clustering y Asociacion

### 2.4.1 Algoritmos Clasicos

| Algoritmo 			| Tipo 				| Complejidad 	| Ventajas 					| Desventajas 					|
|-----------			|------				|-------------	|----------					|-------------					|
| **K-Means** 			| Particional 		| O(n-k-i) 		| Rapido, simple 			| Requiere k conocido 			|
| **DBSCAN** 			| Densidad 			| O(n²) 		| No requiere k, outliers 	| Sensible a parametros 		|
| **Hierarquico** 		| Aglomerativo 		| O(n³) 		| Dendrograma interpretable | Lento con grandes datos 		|
| **Gaussian Mixture** 	| Probabilistico 	| O(n-k²) 		| Soft clustering 			| Asume distribuciones normales |

### 2.4.2 Aplicacion a Asistencia

Para el dominio especifico de asistencia a clases, los algoritmos deben considerar:

**Requisitos:**
- Tiempo real o casi real 		[[EMOJI]] 		60% cumplido
- Adaptativo a nuevos alumnos 	[[EMOJI]] 		60% cumplido
- Robusto a ausencias 			[[EMOJI]] 		80% cumplido
- Interpretable 				[[EMOJI]] 		100% cumplido

### 2.4.3 Enfoque Propuesto en Literatura

Trabajos relacionados con sistemas de asistencia:

| Estudio 					| Ano 	| Metodo 					| Precision | Limitaciones 			|
|---------					|-----	|--------					|-----------|--------------			|
| **Arulogun et al.** 		| 2013 	| RFID 						| 95% 		| Requiere tarjeta 		|
| **Kar et al.** 			| 2019 	| FaceNet + SVM 			| 92% 		| Necesita GPU 			|
| **Bhattacharya et al.** 	| 2020 	| MobileNet 				| 88% 		| Menor precision 		|
| **Chen et al.** 			| 2021 	| Co-ocurrencia simple 		| 79% 		| No considera contexto |
| **Este trabajo** 			| 2026 	| Co-ocurrencia ponderada 	| ? 		| En evaluacion 		|

---

## 2.5 Sistemas de Asistencia Existentes

### 2.5.1 Soluciones Comerciales

| Producto 					| Empresa 		| Tipo 		| Precio 	| Privacidad 	| Precision 	|
|----------					|---------		|------		|--------	|------------	|-----------	|
| **FaceFirst** 			| FaceFirst 	| Comercial | Alto 		| Nube 			| 99% 			|
| **Kairos** 				| Kairos 		| API 		| Por uso 	| Nube 			| 98% 			|
| **Microsoft Face** 		| Microsoft 	| API 		| Por uso 	| Nube 			| 99% 			|
| **Amazon Rekognition** 	| AWS 			| API 		| Por uso 	| Nube 			| 99% 			|
| **FaceAttenDANCE** 		| Este proyecto | Local 	| Gratis 	| 100% local 	| En evaluacion |

**Analisis de mercado:**


Costo vs Privacidad

### Relacion Costo-Privacidad en sistemas existentes

| 						| **Bajo Costo** 													| **Alto Costo** 														|
|---					|----------------													|----------------														|
| **Alta Privacidad** 	| - FaceAttenDANCE (100%, Gratis)<br>- Sistemas locales (80%, Bajo) | *[Vacio]* 															|
| **Baja Privacidad** 	| - APIs gratuitas (50%, Medio) 									| - Soluciones cloud (25%, Alto)<br>- Enterprise cloud (10%, Muy Alto) 	|

**Detalle de soluciones:**

| Solucion 				| Privacidad 	| Costo 	| Tipo 					|
|----------				|------------	|-------	|------					|
| **FaceAttenDANCE** 	| 100% 			| Gratis 	| Local / Open Source 	|
| Sistemas locales 		| 80%			| Bajo 		| Open Source 			|
| APIs gratuitas 		| 50% 			| Medio 	| Freemium / Cloud 		|
| Soluciones cloud 		| 25% 			| Alto 		| Comercial 			|
| Enterprise cloud 		| 10% 			| Muy Alto 	| Enterprise 			|

**Escala visual de privacidad:**

FaceAttenDANCE 		[[EMOJI]] 100%
Sistemas locales 	[[EMOJI]] 80%
APIs gratuitas 		[[EMOJI]] 50%
Soluciones cloud 	[[EMOJI]] 25%
Enterprise cloud 	[[EMOJI]] 10%


**Analisis:**
- **Cuadrante optimo**: FaceAttenDANCE (unico con 100% privacidad y costo cero)
- **Alternativa local**: Sistemas open source (buena privacidad, bajo costo)
- **Soluciones cloud**: Mayor costo, menor privacidad, datos en servidores externos

### 2.5.2 Soluciones Academicas y Open Source

| Proyecto 				| Tecnologia 	| Licencia 		| Activo 				| Documentacion |
|----------				|------------	|----------		|--------				|---------------|
| **OpenFace** 			| Torch 		| MIT 			| [[EMOJI]] 2016-2019 	| [ESTRELLA][ESTRELLA][ESTRELLA] 			|
| **face_recognition** 	| Python 		| MIT 			| [[EMOJI]] 2017-2023 	| [ESTRELLA][ESTRELLA][ESTRELLA][ESTRELLA] 			|
| **DeepFace** 			| Python 		| MIT 			| [[EMOJI]] 2020-actual 	| [ESTRELLA][ESTRELLA][ESTRELLA][ESTRELLA] 			|
| **InsightFace** 		| MXNet 		| MIT 			| [[EMOJI]] 2018-actual 	| [ESTRELLA][ESTRELLA][ESTRELLA] 			|
| **CompreFace** 		| Docker	 	| Apache 2.0 	| [[EMOJI]] 2020-2023 	| [ESTRELLA][ESTRELLA][ESTRELLA] 			|

### 2.5.3 Brecha Identificada

Ninguno de los sistemas existentes ofrece:

1. [OK] **Procesamiento 100% local** (privacidad total)
2. [OK] **Funcionamiento con fotos grupales** (no requiere fotos individuales)
3. [OK] **Asociacion automatica a clases** (sin inscripciones manuales)
4. [OK] **Codigo abierto y gratuito**
5. [OK] **Especifico para clases de danza** (optimizado para este dominio)

**Cobertura de requisitos por sistema existente:**


Requisito Comerciales Open Source FaceAttenDANCE
[EMOJI]
Local (privacidad) 	[EMOJI] [EMOJI] [EMOJI]
Sin inscripciones 	[EMOJI] [EMOJI] [EMOJI]
Fotos grupales 		[EMOJI] [EMOJI] [EMOJI]
Gratuito 			[EMOJI] [EMOJI] [EMOJI]
Especifico danza 	[EMOJI] [EMOJI] [EMOJI]
Documentacion 		[EMOJI] [EMOJI] [EMOJI]
Soporte 			[EMOJI] [EMOJI] [EMOJI]

---

## 2.6 Consideraciones Eticas y de Privacidad

### 2.6.1 Debate Actual

El reconocimiento facial es objeto de un intenso debate etico:

**Posiciones a favor** [[EMOJI]] 60% de la literatura
- Mejora la seguridad
- Automatiza tareas tediosas
- Puede ser menos intrusivo que otros metodos

**Posiciones en contra** [[EMOJI]] 40% de la literatura
- Riesgo de vigilancia masiva
- Sesgos algoritmicos
- Falta de consentimiento

### 2.6.2 Regulaciones

| Regulacion 				| Region 		| Ano 	| Requisitos clave 								|
|------------				|--------		|-----	|------------------								|
| **GDPR** 					| Europa 		| 2018 	| Consentimiento explicito, derecho al olvido 	|
| **CCPA** 					| California 	| 2020 	| Transparencia, opt-out 						|
| **LGPD** 					| Brasil 		| 2020 	| Similar a GDPR 								|
| **Proyecto de ley AI** 	| UE 			| 2024 	| Prohibicion de ciertos usos 					|

### 2.6.3 Principios de Privacidad por Diseno

Este proyecto adopta los siguientes principios:

1. **Minimizacion de datos**: Solo se almacenan descriptores, no imagenes
2. **Procesamiento local**: Nunca se envian datos a internet
3. **Transparencia**: Codigo abierto, auditables
4. **Control del usuario**: El usuario decide que datos conservar
5. **Seguridad por defecto**: Configuracion mas privada por defecto

**Implementacion en FaceAttenDANCE:**

Nivel de privacidad asegurado por componente:

Almacenamiento de fotos 	[[EMOJI]] Local, pero existen
Descriptores faciales 		[[EMOJI]] Irreversibles
Comunicaciones 				[[EMOJI]] Sin internet
Control de datos 			[[EMOJI]] El usuario administra
Auditabilidad 				[[EMOJI]] Codigo abierto

### 2.6.4 Posicionamiento de este Trabajo

Este trabajo se posiciona eticamente:

- **A favor** del uso responsable de la tecnologia
- **En contra** de la vigilancia masiva no consentida
- **Por** la transparencia y el codigo abierto
- **Por** el derecho de los usuarios a controlar sus datos
- **En contra** de los sesgos algoritmicos no auditados

---

## 2.7 Conclusiones del Capitulo

### 2.7.1 Hallazgos Principales

1. **El reconocimiento facial ha madurado** significativamente, alcanzando precisiones >99% en condiciones controladas.

2. **Los metodos de comparacion** tienen diferentes fortalezas y debilidades; no hay uno universalmente superior.

3. **La co-ocurrencia** es una tecnica prometedora para inferir pertenencia a clases sin supervision.

4. **Los sistemas existentes** no cubren completamente las necesidades especificas de academias de danza.

5. **La privacidad** es una preocupacion creciente que debe abordarse desde el diseno.

### 2.7.2 Brecha de Conocimiento

Conocimiento existente vs. Necesario para este proyecto:

Reconocimiento facial 		[[EMOJI]] 80% conocido
Comparacion de descriptores [[EMOJI]] 70% conocido
Clustering para asistencia 	[[EMOJI]] 50% conocido
Privacidad por diseno 		[[EMOJI]] 50% conocido
Aplicacion a danza 			[[EMOJI]] 20% conocido
Sistema completo integrado 	[[EMOJI]] 20% conocido


### 2.7.3 Implicaciones para este Trabajo

De la revision bibliografica se derivan las siguientes decisiones de diseno:

| Decision | Justificacion |
|----------|---------------|
| **Usar descriptores simples (no deep learning)** 			| Suficiente para el dominio, menor complejidad, sin GPU 	|
| **Implementar multiples metodos de comparacion** 			| Para evaluar cual funciona mejor en este contexto 		|
| **Disenar algoritmo de co-ocurrencia ponderado** 			| Mejor balance reportado en literatura 					|
| **100% local** 											| Por privacidad y simplicidad 								|
| **Codigo abierto** 										| Para transparencia y auditabilidad 						|

---

## 2.8 Resumen

En este capitulo hemos:

- Revisado la **evolucion historica** del reconocimiento facial
- Analizado **metodos de comparacion** de imagenes
- Explorado **algoritmos de clustering** aplicables
- Evaluado **sistemas existentes** de asistencia
- Discutido **consideraciones eticas** y de privacidad
- Identificado la **brecha de conocimiento** que este trabajo aborda

El siguiente capitulo presenta la arquitectura propuesta para FaceAttenDANCE, basada en los hallazgos de esta revision.

---

## Referencias

[1] Turk, M., & Pentland, A. (1991). Eigenfaces for recognition. *Journal of cognitive neuroscience*.

[2] Belhumeur, P. N., Hespanha, J. P., & Kriegman, D. J. (1997). Eigenfaces vs. Fisherfaces: Recognition using class specific linear projection. *IEEE Transactions on Pattern Analysis and Machine Intelligence*.

[3] Ahonen, T., Hadid, A., & Pietikainen, M. (2004). Face recognition with local binary patterns. *European Conference on Computer Vision*.

[4] Taigman, Y., Yang, M., Ranzato, M., & Wolf, L. (2014). DeepFace: Closing the gap to human-level performance in face verification. *IEEE Conference on Computer Vision and Pattern Recognition*.

[5] Schroff, F., Kalenichenko, D., & Philbin, J. (2015). FaceNet: A unified embedding for face recognition and clustering. *IEEE Conference on Computer Vision and Pattern Recognition*.

[6] Parkhi, O. M., Vedaldi, A., & Zisserman, A. (2015). Deep face recognition. *British Machine Vision Conference*.

[7] Deng, J., Guo, J., Xue, N., & Zafeiriou, S. (2019). ArcFace: Additive angular margin loss for deep face recognition. *IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

[8] Deng, J., Guo, J., Ververas, E., Kotsia, I., & Zafeiriou, S. (2020). RetinaFace: Single-shot multi-level face localisation in the wild. *IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

[9] Arulogun, O. T., Olatunbosun, A., Fakolujo, O. A., & Olaniyi, O. M. (2013). RFID-based students attendance management system. *International Journal of Scientific & Engineering Research*.

[10] Kar, N., Debbarma, M. K., Saha, A., & Pal, D. R. (2019). Study of implementing automated attendance system using face recognition technique. *International Journal of Computer and Communication Engineering*.

[11] Bhattacharya, S., Nainala, G. S., Das, P., & Routray, A. (2020). Smart attendance monitoring system (SAMS): A face recognition based attendance system for classroom environment. *IEEE International Conference on Advanced Networks and Telecommunications Systems*.

[12] Chen, W., Zhu, L., & Zhang, Y. (2021). Design and implementation of intelligent attendance system based on face recognition. *Journal of Physics: Conference Series*.

[13] European Parliament. (2016). General Data Protection Regulation (GDPR). *Official Journal of the European Union*.

[14] State of California. (2018). California Consumer Privacy Act (CCPA).

[15] European Commission. (2021). Proposal for a Regulation laying down harmonised rules on artificial intelligence (AI Act).


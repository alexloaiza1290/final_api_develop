# Ejecución del proyecto:
1. Instalar lo necesario del requirements.txt

`pip install -r requirements.txt`

2. Ejecutar la aplicacion

`ruvicorn main:app --reload`

3. Probar del swagger

`http://0.0.0.0:8000/docs`

# Parte téorica del examen final

## 1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente

Python es una herramienta fundamental en el ecosistema de la ciencia de datos y el análisis de datos debido a su sintaxis clara y la gran cantidad de bibliotecas especializadas.

**5 casos de uso:**

- **Análisis Exploratorio de Datos (EDA):** Utilizando bibliotecas como `Pandas` y `NumPy`, los científicos de datos pueden cargar, limpiar, transformar y explorar conjuntos de datos para entender patrones, valores atípicos y relaciones entre variables.
- **Visualización de Datos:** Con librerías como `Matplotlib` y `Seaborn`, es posible crear una amplia gama de gráficos (histogramas, dispersiones, heatmaps) para comunicar hallazgos de manera efectiva y comprensible.
- **Aprendizaje Automático (Machine Learning):** `Scikit-learn` proporciona algoritmos listos para usar (clasificación, regresión, clustering) para construir modelos predictivos a partir de datos históricos.
- **Procesamiento de Lenguaje Natural (NLP):** Librerías como `NLTK` y `spaCy` permiten a los programas entender, interpretar y manipular lenguaje humano escrito, útil para análisis de sentimientos o chatbots.
- **Big Data:** Frameworks como `PySpark` permiten trabajar con conjuntos de datos masivos que no caben en la memoria de una sola computadora, distribuyendo el procesamiento en un clúster.



## 2. ¿Cómo se diferencian Flask de Django? Argumentar.

Flask y Django son ambos frameworks web para Python, pero siguen filosofías de diseño diferentes, lo que los hace adecuados para distintos tipos de proyectos.

**Django:**
- **Enfoque:** "Baterías incluidas". Es un framework *full-stack* y de *alta opinión*.
- **Características:** Proporciona una gran cantidad de componentes preconstruidos (ORM, sistema de autenticación, panel de administración, routing, sistema de plantillas) de forma integrada.
- **Ventaja:** Ideal para aplicaciones web complejas y tradicionales que requieren muchas funcionalidades estándar (como sitios de noticias, e-commerce, sistemas de gestión) desde el inicio, ya que acelera el desarrollo al evitar decisiones sobre herramientas.
- **Desventaja:** Puede ser menos flexible y tener una curva de aprendizaje más pronunciada para proyectos muy simples o que requieren componentes altamente personalizados.

**Flask:**
- **Enfoque:** *Microframework* y *minimalista*. Es de *baja opinión*.
- **Características:** Proporciona solo lo esencial (enrutamiento, plantillas Jinja2, servidor de desarrollo). El desarrollador elige e integra las extensiones que necesita (como ORMs, autenticación) de forma manual.
- **Ventaja:** Máxima flexibilidad y control. Perfecto para crear APIs RESTful simples, microservicios, prototipos rápidos o aplicaciones donde se necesite un stack tecnológico muy específico.
- **Desventaja:** Requiere más configuración y decisiones iniciales por parte del desarrollador para proyectos grandes, pudiendo ser más lento que Django al inicio.

**Conclusión:** Django es como un "todo incluido" para construir rápido, mientras que Flask es un "kit de herramientas" para construir con total libertad y minimalismo.



## 3. ¿Qué es un API? Explicar en sus propias palabras

Un API (Interfaz de Programación de Aplicaciones) es como un **menú en un restaurante**.

Imaginemos que el restaurante es un servicio o sistema (por ejemplo, Google Maps). Como cliente (o aplicación), quisieramos usar sus servicios (como obtener direcciones). No podemos entrar a la cocina (la base de datos o lógica interna de Google Maps) y preparar el plato tú mismo. En su lugar, miras el **menú (el API)**, que te lista los platos (funcionalidades) disponibles que podemos pedir, como "obtener ruta entre punto A y B".

Luego, se  hace el **pedido (una solicitud)** al mesero siguiendo un formato específico descrito en el menú. El mesero (el API) lleva el pedido a la cocina, donde se prepara, y luego te trae la **comida (la respuesta o datos)** que solicitaste.

En resumen, un API es un conjunto de reglas y protocolos que permite que dos aplicaciones de software se **comuniquen e intercambien datos** de manera estructurada y segura, sin que una necesite conocer los detalles internos de cómo funciona la otra.


## 4. ¿Cuál es la principal diferencia entre REST y WebSockets?

La diferencia principal radica en el **modelo de comunicación** entre el cliente y el servidor.

- **REST (Representational State Transfer):**
    - Sigue un modelo de comunicación **sin estado (stateless)** y **solicitud-respuesta (request-response)**.
    - El cliente *siempre* debe iniciar la comunicación enviando una solicitud HTTP (GET, POST, etc.) al servidor.
    - El servidor procesa la solicitud y devuelve una respuesta. Luego, la conexión se considera cerrada conceptualmente.
    - Es ideal para operaciones donde el cliente necesita *solicitar* datos específicos de forma puntual (como cargar una página, obtener un perfil de usuario, enviar un formulario).

- **WebSockets:**
    - Establece un **canal de comunicación bidireccional, persistente y en tiempo real** entre el cliente y el servidor.
    - Una vez que se establece la conexión inicial (con un "apretón de manos" HTTP), permanece abierta.
    - Tanto el servidor como el cliente pueden **enviar mensajes** al otro de forma independiente y en cualquier momento, sin necesidad de que el cliente envíe una solicitud primero.
    - Es ideal para aplicaciones que requieren actualizaciones instantáneas y continuas, como chats en vivo, tableros de trading financiero, juegos multijugador online o herramientas de colaboración.

**Analogía:** REST es como hacer una llamada telefónica (llamas, hablas, cuelgas). WebSockets es como una videollamada abierta donde cualquiera puede hablar en cualquier momento sin "marcar" de nuevo.


## 5. Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos en el curso.

**Ejemplo: API de Stripe (Pasarela de Pagos)**

**Descripción:** Stripe ofrece un conjunto de APIs que permiten a los negocios integrar la capacidad de recibir pagos online en sus sitios web o aplicaciones móviles de manera segura, sin tener que construir y certificar su propio sistema de procesamiento de pagos desde cero.

**¿Cómo funciona?**

1.  **Integración del Frontend (Cliente):**
    - El desarrollador integra la biblioteca JavaScript de Stripe (`Stripe.js`) o un SDK móvil en la aplicación.
    - Cuando un usuario introduce los datos de su tarjeta de crédito en el formulario de pago, esta información **nunca toca el servidor del comerciante**. En su lugar, se envía de forma segura directamente a los servidores de Stripe.

2.  **Tokenización:**
    - Stripe recibe los datos sensibles de la tarjeta y, a cambio, devuelve al frontend un **token** único que representa de forma segura esos datos de pago. El token no tiene valor por sí mismo y no puede ser revertido para obtener el número de tarjeta original.

3.  **Procesamiento en el Backend (Servidor):**
    - El frontend envía este token al servidor backend del comerciante.
    - El servidor del comerciante, utilizando una de las bibliotecas del servidor de Stripe (por ejemplo, `stripe` para Python), realiza una solicitud a la **API de Stripe**.
    - Esta solicitud incluye el token, la clave secreta de la API del comerciante (para autenticarse) y los detalles del cargo.

4.  **Ejecución del Pago:**
    - Stripe recibe la solicitud, verifica la autenticidad con la clave secreta, "cambia" el token por los datos reales de la tarjeta y procede a realizar la transacción con la red de pagos (bancos adquirentes, etc.).
    - Stripe luego envía una respuesta al backend del comerciante indicando si el pago fue exitoso o falló.

5.  **Respuesta al Usuario:**
    - Finalmente, el backend del comerciante informa al frontend el resultado, mostrando al usuario un mensaje de "Pago Exitoso" o "Error en el Pago".

**Ventaja para el comerciante:** Se delega toda la complejidad, seguridad (cumplimiento de PCI DSS) y lógica de procesamiento de pagos a Stripe, permitiéndole al comerciante enfocarse en su negocio principal.

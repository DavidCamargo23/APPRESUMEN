# APPRESUMEN
Repositorio de la app para realizar resumenes con python usando una API de OPENAI

Para la aplicación se compone de dos carpetas necesariamente: la primera son los "requirements" o requerimientos que son utilizados para que funcione la aplicación en python
La Otra carpeta es la llamada "app" tiene carpetas importantes:
  una vez archivo inicial "__INIT__" de python y otro es el "resumen" es donde se procede a funcionar toda la lógica con la API de openAI 
  una carpeta de "templates" Dónde está un archivo html y podemos interactuar con el usuario, para que digite su texto y selccione el idioma a traducir el texto.

COMO FUNCIONA:
Para comenzar a usar esta aplicación tenemos que crear nuestro entorno virtual (.VENV) en algunos procesadores de python con esto iniciamos el ambiente y damos inicio __init__ y después a  la aplicación, está nos llevará a un Host local, en donde podremos digitar el texto que queremos resumir y seleccionar el idioma al cual queremos Traducir.
El procesamiento del texto va de acuerdo a la API de OpeanAI, para esto es necesario usar nuestra clave virtual con esto dar la funcionalidad al programa. esto se puede hacer con un archivo .env 
Usando el siguiente codigo:

OPENAI_API_KEY = "sk-proj-XXXXXXX XXXXXXXXO" (digitado la clave dentro de estas comillas)

Con eso la aplicación ya puede funcionar adecuadamente.


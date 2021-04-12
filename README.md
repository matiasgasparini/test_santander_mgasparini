# test_santander_mgasparini
El código está hecho en python 2.7.
Para ejecutar el archivo test_santander.py, se puede hacer sin argumentos y buscará el archivo 'tsv' dentro de la carpeta contenedora. Otra manera de hacerlo es ejecutar el script pasándole como parámetros los path y nombres de archivos origen y destino. Ejemplo:

py test_santander.py C:/Path/al/archivo/datos_data_engineer.tsv C:/Path/al/archivo/datos_data_engineer.csv

En caso de estar ausente el segundo parámetro, el 'csv' se escribirá en la carpeta contendora del script.

Nota:

Algunos campos de la columna 'account_number' tenían caracteres especiales como guiones medios y barras. Como no aclara nada al respecto, asumí que tenía que dejarlos.

CONSIGNA ORIGINAL:

# Data Engineer Programming Test

### Python 
(Para hacerlo interesante, usar Python 2.7)

Se deberá escribir un script que transforme el archivo datos_data_engineer.tsv en un archivo CSV que pueda ser insertado en una base de datos, y/o interpretado por cualquier parser estándar de archivos delimitados, de la manera más sencilla posible.

El archivo resultante debe tener las siguientes características:
* Cada row contiene la misma cantidad de campos
* Los campos se separan con un pipe |
* Se deben poder leer correctamente los caracteres especiales que estén presentes en los campos actuales del archivo. 
* El encoding del archivo final debe ser UTF-8 (datos_de_santander.tsv es un archivo UTF-16LE)

Preguntas
* En qué requerimiento implementarías una cola de mensajes en una solución orientada a datos?  Que lenguaje utilizarías y porque?
* Que experiencia posees sobre py spark o spark scala? Contar breves experiencias, en caso de contar experiencia con otro framework de procesamiento distribuido, dar detalles también.
* Qué funcionalidad podrías expandir desde el area de ingeniería de datos con una API y arquitectónicamente como lo modelarías?

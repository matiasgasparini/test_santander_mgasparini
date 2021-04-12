import io, re, os, sys
# coding=utf-8

# Agregado para recibir argumentos

# Chequeo existencia de argumentos 

if(len(sys.argv)>1):
    archivo_original = sys.argv[1]
    print("El archivo original ingresado es: " + archivo_original)
else:
    archivo_original = os.path.join(str(sys.path[0]), "datos_data_engineer.tsv")
    print("No se ingresó un path para el archivo a tratar. Se utiliza por defecto: " + archivo_original)

if(len(sys.argv)>2):
    archivo_destino = sys.argv[2]
    print("El archivo destino ingresado es: " + archivo_destino)
else:
    archivo_destino = os.path.join(sys.path[0], "datos_data_engineer.csv")
    print("No se ingresó un path para el destino. Se utiliza por defecto: " + archivo_destino)


## PARSER

# Abro archivo con encoding requerido
archivo_a_tratar = io.open( file = archivo_original, mode = "r", encoding = "UTF-16LE")
print("Fichero leido")

# Obtengo nro de columnas para posterior regex
columnas = archivo_a_tratar.readline().strip().split("\t")
nro_columnas=len(columnas)-2

# Vuelvo al principio del archivo
archivo_a_tratar.seek(0, os.SEEK_SET)

# Sustituyo mediante regex los saltos de línea entre columnas
print("Aplicando sustituciones por REGEX")
archivo_parseado = re.sub(r'(\n)(\t)', r'\2', archivo_a_tratar.read(),flags = re.M)
archivo_parseado = re.sub(r'(\t)(\n)', r'\1', archivo_parseado,flags = re.M)

# Creo regex para eliminar saltos de línea que aparecen en medio de valores de columnas y sustituyo
regex_final = "(\n((\S+)\t){1,"+str(nro_columnas)+"}\S+)(\n)"
archivo_parseado = re.sub(regex_final, r' \1 ', archivo_parseado,flags = re.M)

print("Escribiendo " + archivo_destino + "...")
# Escribo archivo final en UTF-8

with io.open( file = archivo_destino, mode = "w", encoding = "UTF-8") as salida:
    for line in archivo_parseado:
        campos = line.split("\t")
        salida.write("|".join(campos))

print("Realizado!")
 
# Cierro archivo abierto previamente
archivo_a_tratar.close()

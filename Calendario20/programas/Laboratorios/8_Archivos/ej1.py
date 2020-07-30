ruta="nombreArchivo.txt"
archivo=open(ruta,"w+")
contenido="esta es una prueba del archivo"
archivo.write(contenido)
archivo.seek(0)
print(archivo.read())
archivo.close()
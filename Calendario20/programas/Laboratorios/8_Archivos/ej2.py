print("Agregando otra cadena","\n")
cadena="esta es otra linea para el archivo"
archivo.write('\n'+cadena)
archivo.seek(0)
print(archivo.read())

archivo.close()

ruta=str(input("Introduce el nombre del archivo: "))
archivo=open(ruta,"w+")
resp='s'
while resp!='n':
    linea=str(input("Introduce un texto para el archivo: "))
    archivo.write(linea + '\n')
    resp=str(input("¿Quieres introducir una línea de texto para el archivo s/n?"))
archivo.seek(0)
print(archivo.read())
archivo.close()




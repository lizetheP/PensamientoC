file = open("prueba.txt", "r+")
lineas = ["Hola a todos\n", "Hasta luego\n"] 
file.writelines(lineas)
file.seek(0)
contenido = file.readline()
print(contenido)
contenido = file.readline()
print(contenido)
file.close()


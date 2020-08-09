file = open("prueba.txt", "r+")
lineas = ["Hola a todos\n", "Hasta luego\n"] 
file.writelines(lineas)
file.seek(0)
contenido = file.read()
file.close()
print(contenido)

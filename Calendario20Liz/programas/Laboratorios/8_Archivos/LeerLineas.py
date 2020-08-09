file = open("prueba.txt", "r+")
lineas = ["Hola a todos\n", "Hasta luego\n"] 
file.writelines(lineas)
file.seek(0)
contenido = file.readlines()
print(contenido)
file.close()



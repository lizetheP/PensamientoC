file = open("prueba.txt", "r+")
file.write("Hola")
file.seek(0)
contenido = file.read(1)
file.close()
print(contenido)


file = open ("dir.txt", "r")
file.seek(0)
nombre = str(input("Introduce tu apellido: "))
linea = file.readline()
while linea != "":
    if nombre in linea:
        print("%s" % linea, end='')
    linea = file.readline()
file.close()

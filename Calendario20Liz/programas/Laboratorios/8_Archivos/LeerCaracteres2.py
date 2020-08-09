def leerCaracteres(ruta):
    file = open(ruta, "r")
    while True:
        letra = file.read(1)
        if not letra:
            print("Fin de archivo")
            break
        print(letra, end='')
    file.close()

ruta = str(input("Introduce el nombre del archivo: "))
leerCaracteres(ruta)
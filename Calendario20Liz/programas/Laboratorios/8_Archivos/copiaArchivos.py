def copiaArchivos(origen, destino):
    file1 = open(origen, "r")
    file2 = open(destino, "w")
    while True:
        letra = file1.read(1)
        letra = letra.upper()
        file2.write(letra)
        if not letra:
            break
    file1.close()
    file2.close()

nombre = str(input("Introduce el nombre del archivo origen: "))
nombre2 = str(input("Introduce el nombre del archivo destino: "))
copiaArchivos(nombre, nombre2)
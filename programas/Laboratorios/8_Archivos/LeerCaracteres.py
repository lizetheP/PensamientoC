def leerCaracteres(ruta):
    file = open(ruta, "r")
    while True:
        letra = file.read(1)
        if not letra:
            print("End of file")
            break
        print("Caracter obtenido:", letra)
    file.close()
    
leerCaracteres("prueba2.txt")
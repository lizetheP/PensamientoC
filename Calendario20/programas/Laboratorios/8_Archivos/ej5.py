def leeLineas(ruta):
    archivo = open(ruta, "r")
    lineas =archivo.readlines()
    print(lineas)
    for i in range(0, len(lineas)):
        print(lineas[i])

leeLineas("prueba2.txt")

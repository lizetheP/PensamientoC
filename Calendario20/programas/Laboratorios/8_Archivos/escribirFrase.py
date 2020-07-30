def escribirCadena(ruta, cadena):
    file = open(ruta, "w")
    for i in range(0, len(cadena)):
        file.write(cadena[i])
    file.close()

ruta = str(input("Introduce el nombre del archivo: "))
cadena = str(input("Introduce una frase: "))
escribirCadena(ruta, cadena)
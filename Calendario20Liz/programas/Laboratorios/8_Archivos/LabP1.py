def muestraContenido(ruta):
    archivo = open(ruta, "r")
    print(archivo.read())


ruta = str(input("Introduce el nombre de un archivo: "))
muestraContenido(ruta)
def copiaArchivo(rutaO, rutaD):
    archivo1 = open(rutaO, "r")
    archivo2 = open(rutaD, "w+")
    archivo2.write(archivo1.read())
    archivo1.close()
    archivo2.close()

ruta1 = str(input("Introduce el nombre de un archivo1: "))
ruta2 = str(input("Introduce el nombre de un archivo2: "))
copiaArchivo(ruta1, ruta2)
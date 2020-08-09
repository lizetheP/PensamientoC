def abrirArchivo(ruta, modo):
    archivo=open(ruta,modo)
    return archivo


def leerArchivo(archivo):
    contenido=archivo.read()
    return contenido

def escribirArchivo(archivo,texto):
    archivo.write(texto+'\n')


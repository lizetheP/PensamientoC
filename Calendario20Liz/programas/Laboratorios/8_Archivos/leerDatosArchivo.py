def leerDatosArchivo(nombre):
    file=open(nombre,"r")
    contenido = file.read()
    print(contenido)
    file.close()
 
nombre = str(input("Introduce el nombre del archivo: "))
leerDatosArchivo(nombre)
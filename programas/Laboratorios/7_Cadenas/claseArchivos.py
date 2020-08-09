def leerCaracteres(nombre):
    file = open(nombre, "r")
    while True:
        letra = file.read(1)
        if not letra:
            print("Fin de archivo")
            break
        print(letra, end='')
    file.close()

def escribirCadena(nombre, cadena):
    file = open(ruta, "w")
    for i in range(0, len(cadena)):
        file.write(cadena[i])
    file.close()

def escribe5frases(nombre):
    file=open(nombre,"w+")
    i = 1
    while i<=5:
        frase = str(input("Introduce una frase: "))
        file.write(frase+"\n")
        i = i+1
    file.close()

def menu():
    print("1. Leer caracteres")
    print("2. Escribir cadena")
    print("3. Escribir 5 frases")
    print("4. Salir")
    
continua = True
while continua:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        nombre = str(input("Introduce el nombre del archivo: "))
        leerCaracteres(nombre)
    elif opcion == 2:
        nombre = str(input("Introduce el nombre del archivo: "))
        cadena = str(input("Introduce una frase: "))
        escribirCadena(nombre, cadena)
    elif opcion == 3:
        nombre = str(input("Introduce el nombre del archivo: "))
        escribe5frases(nombre)
    elif opcion == 4:
        continua = False
        print("Adios")
    else:
        continua = False
        print("Opción inválida")
            
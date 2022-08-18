def cuenta_consonantes(nombre):
    file = open(nombre, "r")
    cont = 0
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    letra = file.read(1)
    while letra != "":
        if letra in consonantes:
            cont = cont + 1
        letra = file.read(1)
    file.close()
    return cont

def cuenta_digitos(nombre):
    digitos ="0123456789"
    file = open(nombre, "r")
    cont = 0
    continua = True
    letra = file.read(1)
    while letra != "":
        if letra in digitos:
            cont = cont + 1
        letra = file.read(1)
    file.close()
    return cont

def copia_archivo(nombreO, nombreD):
    fileO = open(nombreO, "r")
    fileD = open(nombreD, "w+")
    contenido = fileO.read()
    print(contenido)
    fileD.write(contenido.upper())
    fileO.close()
    fileD.close()

def captura_alumnos(n):
    file=open("alumnos.txt","w+")
    for i in range(n):
        print("\nAlumno %i" % (i+1))
        nombre = str(input("Introduce nombre: "))
        apellido1 = str(input("Introduce apellido 1: "))
        apellido2 = str(input("Introduce apellido 2: "))
        completo = nombre + ' ' + apellido1 + ' ' + apellido2 + '\n'
        file.write(completo)
    file.close()

def busca_apellido(apellido):
    file = open ("alumnos.txt", "r")
    #file.seek(0)
    linea = file.readline()
    while linea != '': #Mientras línea sea diferente de vacío
        if apellido in linea:
            print("%s" % linea, end='')
        linea = file.readline()
    file.close()

def menu():
    print("1. Cuenta consonantes")
    print("2. Copia archivo")
    print("3. Captura alumnos")
    print("4. Busca apellido")
    print("5. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            name = str(input("Introduce el nombre del archivo: "))
            res = cuenta_consonantes(name)
            print("Hay %i caracteres en el archivo" % res)
        elif opcion == 2:
            nameO = str(input("Introduce el nombre del archivo origen: "))
            nameD = str(input("Introduce el nombre del archivo destino: "))
            copia_archivo(nameO, nameD)
        elif opcion == 3:
            n = int(input("Introduce el numero de alumnos: "))
            captura_alumnos(n)
        elif opcion == 4:
            apellido = str(input("Introduce el apellido a buscar: "))
            busca_apellido(apellido)
        elif opcion == 5:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")

main()

# Andrés Doniz
# Mariana
# Mariana
# Emiliano
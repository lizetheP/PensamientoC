def esconde_en_archivo():
    frase = str(input("Dame una frase: "))
    file = open("secreto.txt", "w")
    for i in range(len(frase)):
        num = ord(frase[i])
        if (num >= 97 and num <= 122) or (num >= 65 and num <= 90):
            if num == 122:
                file.write('a')
            elif num == 90:
                file.write('A')
            else:
                num = ord(frase[i]) + 1
                letra = chr(num)
                file.write(letra)
        else:
            file.write(frase[i])
    file.close()
    
def cuenta_consonantes(nombre):
    file = open(nombre, "r")
    cont = 0
    continua = True
    while continua == True:
        letra = file.read(1)
        if not letra:
            continua = False
        else:
            letra = letra.lower()
            num = ord(letra)
            if (num >= 97 and num <= 122) and (letra != 'a' and letra != 'e'
                and letra != 'i' and letra != 'o' and letra != 'u'):
                cont = cont + 1
    file.close()
    return cont



def cuenta_digitos2(nombre):
    digitos ="0123456789"
    file = open(nombre, "r")
    cont = 0
    continua = True
    while continua == True:
        letra = file.read(1)
        if not letra:
            continua = False
        else:
            if letra in digitos:
                cont = cont + 1
    file.close()
    return cont

def copia_archivo(nombreO, nombreD):
    fileO = open(nombreO, "r")
    fileD = open(nombreD, "w+")
    continua = True
    while continua == True:
        letra = fileO.read(1)
        if not letra:
            continua = False
        else:
            letra = letra.upper()
            fileD.write(letra)
    fileD.seek(0)
    archD = fileD.read()
    print(archD)
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
    file.seek(0)
    linea = file.readline()
    continua = True
    while continua == True:
        if not linea:
            continua = False
        elif apellido in linea:
            print("%s" % linea, end='')
        linea = file.readline()
    file.close()
    
def menu():
    print("1. Esconde en archivo")
    print("2. Cuenta consonantes")
    print("3. Copia archivo")
    print("4. Captura alumnos")
    print("5. Busca apellido")
    print("6. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            esconde_en_archivo()
        elif opcion == 2:
            name = str(input("Introduce el nombre del archivo: "))
            res = cuenta_consonantes(name)
            print("Hay %i caracteres en el archivo" % res)
        elif opcion == 3:
            nameO = str(input("Introduce el nombre del archivo origen: "))
            nameD = str(input("Introduce el nombre del archivo destino: "))
            copia_archivo(nameO, nameD)
        elif opcion == 4:
            n = int(input("Introduce el numero de alumnos: "))
            captura_alumnos(n)
        elif opcion == 5:
            apellido = str(input("Introduce el apellido a buscar: "))
            busca_apellido(apellido)
        elif opcion == 6:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")

main()

# Andrés Doniz
# Mariana
# Mariana
# Emiliano
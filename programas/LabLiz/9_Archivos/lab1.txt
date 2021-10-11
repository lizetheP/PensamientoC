def escribir_en_archivo(nombre):
    file = open(nombre, "w")
    for i in range(3):
        frase = str(input("Dame una frase: "))
        file.write(frase)
        file.write("\n")
    file.close()

def cuenta_caracteres(nombre):
    file = open(nombre, "r")
    cont = 0
    continua = True
    while continua == True:
        letra = file.read(1)
        if not letra:
            continua = False
        else:
            if letra != "\n" and letra != ' ':
                cont = cont + 1
    file.close()
    return cont

def cuenta_digitos(nombre):
    file = open(nombre, "r")
    cont = 0
    continua = True
    while continua == True:
        letra = file.read(1)
        if not letra:
            continua = False
        else:
            if letra == '1' or letra == '2' or letra == '3' or \
               letra == '4' or letra == '5' or letra == '6' or \
               letra == '7' or letra == '8' or letra == '9' or letra == '0':
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
            letra = letra.lower()
            fileD.write(letra)
    fileD.seek(0)
    archD = fileD.read()
    print(archD)
    fileO.close()
    fileD.close()

def imprime_archivo(nombre):
    file = open(nombre, "r")
    arch = file.read()
    print(arch)
    file.close()
    
def menu():
    print("1. Escribir en archivo")
    print("2. Cuenta caracteres")
    print("3. Cuenta digitos")
    print("4. Copia archivo")
    print("5. Imprime archivo")
    print("6. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            name = str(input("Introduce el nombre del archivo: "))
            escribir_en_archivo(name)
        elif opcion == 2:
            name = str(input("Introduce el nombre del archivo: "))
            res = cuenta_caracteres(name)
            print("Hay %i caracteres en el archivo" % res)
        elif opcion == 3:
            name = str(input("Introduce el nombre del archivo: "))
            res = cuenta_digitos2(name)
            print("Hay %i digitos en el archivo" % res)
        elif opcion == 4:
            nameO = str(input("Introduce el nombre del archivo origen: "))
            nameD = str(input("Introduce el nombre del archivo destino: "))
            copia_archivo(nameO, nameD)
        elif opcion == 5:
            name = str(input("Introduce el nombre del archivo: "))
            imprime_archivo(name)
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
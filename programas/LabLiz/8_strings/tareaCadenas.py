def cuenta_ocurrencias(cadena, letra):
    cont = 0
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower():
            cont = cont + 1
    return cont

def imprime_pos_espacios(cadena):
    for i in range(len(cadena)):
        if cadena[i] == " ":
            print(i, end=" ")

def cadena_mayusculas(cadena):
    return cadena.upper()

def cuenta_vocales(cadena):
    cont = 0
    for i in range(len(cadena)):
        if cadena[i].lower() == 'a' or cadena[i].lower() == 'e'  or cadena[i].lower() == 'i' or cadena[i].lower() == 'o'  or cadena[i].lower() == 'u':
            cont = cont + 1
    return cont

def deletrea_cadena(cadena):
    for i in range(len(cadena)):
        if i == len(cadena)- 1:
            print(cadena[i])
        else:
            print(cadena[i], end="-")
            
def menu():
    print()
    print("1. Cuenta ocurrencias")
    print("2. Imprime posición espacios")
    print("3. Cadena mayúsculas")
    print("4. Cuenta vocales")
    print("5. Deletrea cadena")
    print("6. Salir")
       
def main():
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        frase = str(input("Introduce una frase: "))
        letra = str(input("Introduce una letra: "))
        res = cuenta_ocurrencias(frase, letra)
        print(res)
    elif opcion == 2:
        frase = str(input("Introduce una frase: "))
        imprime_pos_espacios(frase)
    elif opcion == 3:
        frase = str(input("Introduce una frase: "))
        frasef = cadena_mayusculas(frase)
        print(frasef)
    elif opcion == 4:
        frase = str(input("Introduce una frase: "))
        res = cuenta_vocales(frase)
        print(res)
    elif opcion == 5:
        cadena = str(input("Introduce la cadena: "))
        deletrea_cadena(cadena)
    elif opcion == 6:
        print("Adios")
        continua = False
    else:
        print("Opcion_invalida")

main()

"""
Introduce una opcion: 1
Introduce una frase: Hola esta es una PRUEBA
Introduce una letra: a
4

Introduce una opcion: 2
Introduce una frase: El sol y la luna
2 6 8 11

Introduce una opcion: 3
Introduce una frase: La luna
LA LUNA

Introduce una opcion: 4
Introduce una frase: El sol y la LUNA
5

"""
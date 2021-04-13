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
    #menu()
    opcion = int(input())
    if opcion == 1:
        cadena = str(input())
        letra = str(input())
        res = cuenta_ocurrencias(cadena, letra)
        print(res)
    elif opcion == 2:
        cadena = str(input())
        letra1 = str(input())
        letra2 = str(input())
        reemplaza_letra(cadena, letra1, letra2)
    elif opcion == 3:
        cadena = str(input())
        cadenaf = obten_nombre_completo(cadena)
        print(cadenam)
    elif opcion == 4:
        # COMPLETAR ESTAS INSTRUCCIONES
    elif opcion == 5:
        # COMPLETAR ESTAS INSTRUCCIONES
    elif opcion == 7:
        print("Adios")
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
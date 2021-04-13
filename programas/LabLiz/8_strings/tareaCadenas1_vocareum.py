def cuenta_ocurrencias(cadena, letra):
    cont = 0
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower():
            cont = cont + 1
    return cont

def reemplaza_letra(cadena, letra1, letra2):
    cadena2 = cadena.replace(letra1, letra2)
    return cadena2

def imprime_pos_guiones(cadena):
    for i in range(len(cadena)):
        if cadena[i] == '-':
            print(i, end=" ")

def obten_nombre_completo(n, ap, am):
    cadena2 = n + " " + ap + " " + am
    return cadena2

def cuenta_consonantes(cadena):
    cont = 0
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in range(len(cadena)):
        if cadena[i] in consonantes:
            cont = cont + 1
    return cont

def deletrea_cadena(cadena):
    for i in range(len(cadena)):
        if i == len(cadena)- 1:
            print(cadena[i])
        elif cadena[i] == ' ':
            print(cadena[i], end="")   
        else:
            print(cadena[i], end="_")
            
def menu():
    print()
    print("1. Cuenta ocurrencias")
    print("2. Reemplaza letra")
    print("3. Imprime posición guiones")
    print("4. Obten nombre completo")
    print("5. Cuenta consonantes")
    print("6. Deletrea cadena")
    print("7. Salir")
       
def main():
    #menu()
    opcion = int(input())
    if opcion == 1:
        frase = str(input())
        letra = str(input())
        res = cuenta_ocurrencias(frase, letra)
        print(res)
    elif opcion == 2:
        frase = str(input())
        l1 = str(input())
        l2 = str(input())
        frasef =reemplaza_letra(frase, l1, l2)
        print(frasef)
    elif opcion == 3:
        frase = str(input())
        imprime_pos_guiones(frase)
    elif opcion == 4:
        n = str(input())
        ap = str(input())
        am = str(input())
        nombre = obten_nombre_completo(n, ap, am)
        print(nombre)
    elif opcion == 5:
        frase = str(input())
        res = cuenta_consonantes(frase)
        print(res)
    elif opcion == 6:
        cadena = str(input())
        deletrea_cadena(cadena)
    elif opcion == 7:
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
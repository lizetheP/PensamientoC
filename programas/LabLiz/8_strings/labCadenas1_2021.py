def inserta_html(cadena):
    fin = "<html><body>" + cadena + "</body></html>"
    return fin

def inserta_saltos(cadena):
    fin = cadena.replace("\\n", "<br>")
    return fin
        
def formato_web(cadena):
    fin = inserta_saltos(inserta_html(cadena))
    return fin

def limpia_abecedario(abecedario, cadena):
    cadena2 = ""
    for i in range(0, len(cadena)):
        if (cadena[i] in abecedario):
            cadena2 = cadena2 + cadena[i]
    return cadena2
      
def invierte_cadena(cadena):
    ultimo = len(cadena)-1
    cadena2 = ""
    for i in range (ultimo, -1, -1):
        cadena2 = cadena2 + cadena[i]
    return cadena2

def elimina_espacios (cadena):
    cadena2 = ""
    for i in range (len(cadena)):
        if cadena[i] != ' ':
            cadena2 = cadena2 + cadena[i]
    return cadena2

def es_palindromo(cadena):
    invertida = invierte_cadena(cadena)
    invertida = elimina_espacios(invertida)
    cadena = elimina_espacios(cadena)
    print(invertida)
    print(cadena)
    for i in range (len(cadena)):
        if cadena[i] != invertida[i]:
            return False
    return True

def imprime_sin_caracter(cadena, caracter):
    for i in range(len(cadena)):
        if (cadena[i].lower() != caracter.lower()):
            print(cadena[i], end="")

def menu():
    print()
    print("1. Inserta html")
    print("2. Inserta saltos")
    print("3. Formato web")
    print("4. Limpia_abecedario")
    print("5. Invierte cadena")
    print("6. Elimina espacios")
    print("7. Es palíndromo")
    print("8. Imprime sin caracter")
    print("9. Salir")
       
def main():
    continua = True
    abecedario = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑáéíóú0123456789"
    while continua:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            frase = str(input("Introduce una frase: "))
            frasef = inserta_html(frase)
            print(frasef)
        elif opcion == 2:
            frase = str(input("Introduce una frase: "))
            frasef = inserta_saltos(frase)
            print(frasef)
        elif opcion == 3:
            frase = str(input("Introduce una frase: "))
            frasef = formato_web(frase)
            print(frasef)
        elif opcion == 4:
            cadena = str(input("Introduce una cadena: "))
            cadenaf = limpia_abecedario(abecedario, cadena)
            print(cadenaf)
        elif opcion == 5:
            cadena = str(input("Introduce la cadena: "))
            cadenaf = invierte_cadena(cadena)
            print(cadenaf)
        elif opcion == 6:
            cadena = str(input("Introduce la cadena: "))
            cadenaf = elimina_espacios(cadena)
            print(cadenaf)
        elif opcion == 7:
            cadena = str(input("Introduce la cadena: "))
            res = es_palindromo(cadena)
            print(res)
        elif opcion == 8:
            cadena = str(input("Introduce la cadena: "))
            caracter = str(input("Introduce el caracter: "))
            imprime_sin_caracter(cadena, caracter)
        elif opcion == 9:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")

main()
def inserta_html(cadena):
    fin = "<html><body>" + cadena + "</body></html>"
    return fin

def inserta_saltos(cadena):
    fin = cadena.replace("\\n", "<br>")
    return fin
        
def formato_web(cadena):
    fin = inserta_saltos(inserta_html(cadena))
    return fin

def limpia_cadena(caracteresSeguros, cadena):
    cadena2 = ""
    for i in range(0, len(cadena)):
        if (cadena[i] in caracteresSeguros):
            cadena2 = cadena2 + cadena[i]
    return cadena2

def cromosomas_x(cadena):
    cont = 0
    for i in range(0, len(cadena)):
        if ('x'== cadena[i] or 'X'== cadena[i]):
            cont = cont + 1
    return cont

def cromosomas_y(cadena):
    cont = 0
    for i in range(0, len(cadena)):
        if ('y'== cadena[i] or 'Y'== cadena[i]):
            cont = cont + 1
    return cont

def determina_sexo(cadena):
    x = cromosomas_x(cadena)
    y = cromosomas_y(cadena)
    if x > y:
        print("Femenino")
    elif y > x:
        print("Masculino")
    else:
        print("Indefinido")

def imprime_limpio(cadena):
    for i in range(len(cadena)):
        if (cadena[i] != ' '):
            print(cadena[i], end="")
            
def escribe_asteriscos(cadena, letra):
    cadena2 = ""
    for i in range(0, len(cadena)):
        if (cadena[i] == letra):
            cadena2 = cadena2 + cadena[i]
        elif (cadena[i] == ' '):
            cadena2 = cadena2 + ' '
        else:
            cadena2 = cadena2 + "*"
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

def menu():
    print()
    print("1. Inserta html")
    print("2. Inserta saltos")
    print("3. Formato web")
    print("4. Limpia_cadena")
    print("5. Determina sexo")
    print("6. Imprimir sin espacios")
    print("7. Escribe asteriscos")
    print("8. Invierte cadena")
    print("9. Es palíndromo")
    print("0. Elimina espacios")
       
def main():
    continua = True
    caracteres_seguros = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑáéíóú0123456789"
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
            cadenaf = limpia_cadena(caracteres_seguros, cadena)
            print(cadenaf)
        elif opcion == 5:
            cadena = str(input("Introduce la cadena de cromosomas: "))
            determina_sexo(cadena)
        elif opcion == 6:
            cadena = str(input("Introduce la cadena: "))
            imprime_limpio(cadena)
        elif opcion == 7:
            cadena = str(input("Introduce la cadena: "))
            letra = str(input("Introduce una letra: "))
            cadenaf = escribe_asteriscos(cadena, letra)
            print(cadenaf)
        elif opcion == 8:
            cadena = str(input("Introduce la cadena: "))
            cadenaf = invierte_cadena(cadena)
            print(cadenaf)
        elif opcion == 9:
            cadena = str(input("Introduce la cadena: "))
            res = es_palindromo(cadena)
            print(res)
        elif opcion == 0:
            cadena = str(input("Introduce la cadena: "))
            cadenaf = elimina_espacios(cadena)
            print(cadenaf)
        elif opcion == 'A':
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")

main()
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
            
def menu():
    print()
    print("1. Inserta html")
    print("2. Inserta saltos")
    print("3. Formato web")
    print("4. Limpia_cadena")
    print("5. Determina sexo")
    print("6. Imprimir sin espacios")
    print("7. Salir")
       
def main():
    continua = True
    while continua:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:

        elif opcion == 2:
        
        elif opcion == 3:
    
        elif opcion == 4:
        
        elif opcion == 5:
        
        elif opcion == 6:
        
        elif opcion == 7:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")

main()
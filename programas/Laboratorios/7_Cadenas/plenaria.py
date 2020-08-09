def cuentaVocales(cadena):
    cad = cadena.lower()
    cont = 0
    for i in range(0, len(cad)):
        if ('a'== cad[i] or 'e'== cad[i] or 'i'== cad[i] or 'o'== cad[i] or 'u' == cad[i]):
            cont = cont + 1
    return cont        
        
def insertaHtml(cadena):
    fin = "<html><body>" + cadena + "</body></html>"
    return fin

def insertaSaltos(cadena):
    print(cadena)
    fin = cadena.replace("\\n", "<br>")
    return fin
        
def formatoWeb(cadena):
    fin = insertaSaltos(insertaHtml(cadena))
    return fin

def esPalindromo(cadena):
    cadena2 = ""
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    ultimo = len(cadena) - 1
    while ultimo >= 0:
        letra = cadena[ultimo]
        cadena2 = cadena2 + letra 
        ultimo = ultimo - 1
    if cadena == cadena2:
        return True
    else:
        return False

def menu():
    print("\n1. Cuenta vocales")
    print("2. Inserta html")
    print("3. Inserta saltos")
    print("4. Formato web")
    print("5. Es palindromo")
    print("6. Salir")
       
continua = True
while continua:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        frase = str(input("Introduce una frase: "))
        total = cuentaVocales(frase)
        print("La frase tiene ", total, "vocales")
    elif opcion == 2:
        frase = str(input("Introduce una frase: "))
        frase2 = insertaHtml(frase)
        print("La nueva frase es: ", frase2)
    elif opcion == 3:
        frase = str(input("Introduce una frase: "))
        frase2 = insertaSaltos(frase)
        print("La nueva frase es: ", frase2)
    elif opcion == 4:
        frase = str(input("Introduce una frase: "))
        frase2 = formatoWeb(frase)
        print("La nueva frase es: ", frase2)
    elif opcion == 5:
        frase = str(input("Introduce una frase: "))
        print("Es palindromo: ", esPalindromo(frase))
    elif opcion == 6:
        print("\n Adios")
        continua = False
    else:
        print("\n ERROR OPCION INVALIDA")
        continua = False
"""
total = cuentaVocales(frase)
print("La frase tiene ", total, "vocales")
"""
"""print(esPalindromo(frase))

total = formatoWeb(frase)
print(total)"""

#devuelve "Hola a todos<br> mi nombre es Goku!". 
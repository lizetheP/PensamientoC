def imprime_caracteres(cadena):
    cont = 0
    for i in range(0, len(cadena)):
       print("%c" % cadena[i], end="*")

def main():
    frase = str(input("Introduce una frase: "))
    imprime_caracteres(frase)

main()

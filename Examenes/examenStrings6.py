def imprime_letra(cadena, letra):
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower():
            print("%c" % cadena[i], end="")
        else:
            print("x", end="")
    print()

def main():
    cadena = str(input())
    letra = str(input())
    imprime_letra(cadena, letra)
    
main()
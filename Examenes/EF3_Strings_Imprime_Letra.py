def imprime_letra_espacios(cadena, letra):
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower() or cadena[i]== ' ':
            print("%c" % cadena[i], end="")
        else:
            print("x", end="")
    print()

def main():
    cadena = str(input("Dame una cadena: "))
    letra = str(input("Dame una letra: "))
    imprime_letra_espacios(cadena, letra)
    
main()
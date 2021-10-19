def imprime_letra(cadena, letra):
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower():
            print("%c" % cadena[i], end="")
        else:
            print("x", end="")

def main():
    cadena = str(input("Introduce una cadena: "))
    letra = str(input("Introduce la letra : "))
    imprime_letra(cadena, letra)
    
main()
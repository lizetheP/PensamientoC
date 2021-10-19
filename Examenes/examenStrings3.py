def posicion_caracter(cadena, letra):
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower():
            print("%i" % i)

def main():
    cadena = str(input("Introduce una cadena: "))
    letra = str(input("Introduce la letra : "))
    posicion_caracter(cadena, letra)
    
main()
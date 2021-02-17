def reemplaza_caracter(cadena, letra1, letra2):
    cadena2 = ""
    for i in range(len(cadena)):
        if cadena[i].lower() == letra1.lower():
            cadena2 = cadena2 + letra2
        else:
            cadena2 = cadena2 + cadena[i]
    return cadena2

def reemplaza_caracter2(cadena, letra1, letra2):
    cadena2 = ""
    for i in range(len(cadena)):
        if cadena[i] == letra1:
            cadena2 = cadena2 + letra2
        else:
            cadena2 = cadena2 + cadena[i]
    return cadena2

def main():
    cadena = str(input("Introduce una cadena: "))
    letra1 = str(input("Introduce la letra 1: "))
    letra2 = str(input("Introduce la letra 2: "))
    cadenaf = reemplaza_caracter2(cadena, letra1, letra2)
    print(cadenaf)
    
main()
    
def cuantas_repeticiones(cadena, letra):
    cont = 0
    for i in range(0, len(cadena)):
        if (letra== cadena[i]):       
            cont = cont+1
    return cont

def main():
    frase = str(input("Introduce una cadena: "))
    letra = str(input("Introduce una letra: "))
    res = cuantas_repeticiones(frase, letra)
    print("La frase tiene %i caracteres %c" %(res, letra))

main()

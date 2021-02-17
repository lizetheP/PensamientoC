def cuenta_caracter_espacios(cadena, letra):
    cont  = 0
    for i in range(len(cadena)):
        if cadena[i].lower() == letra.lower() or cadena[i] == ' ':
            cont = cont + 1
    return cont

def main():
    cadena = str(input("Introduce una cadena: "))
    letra = str(input("Introduce la letra : "))
    res = cuenta_caracter_espacios(cadena, letra)
    print(res)
    
main()
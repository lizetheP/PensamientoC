





def imprime_caracteres(cadena):
    for i in range(0, len(cadena)):
        print("%c"%cadena[i], end="")
      
def cuantas_repeticiones(cadena, letra):
    cont = 0
    for i in range(0, len(cadena)):
        if cadena[i].upper() == letra.upper():
            cont = cont + 1
    return cont
      
def main():
    cadena = str(input("Introduce una cadena: "))
    caracter = str(input("Introduce una letra: "))
    res = cuantas_repeticiones(cadena, caracter)
    print(res)

#imprime_caracteres(cadena)
    
main()



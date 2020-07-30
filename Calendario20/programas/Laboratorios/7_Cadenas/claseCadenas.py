"""cadena = "HOLa A TODOS"
for i in range(0, len(cadena)):
   print(cadena[i], end='')


def cuantosCaracteres(cadena):
    cont = 0
    for i in range(0, len(cadena)):
       cont = cont+1
    return cont

frase = str(input("Introduce una frase: "))
res = cuantosCaracteres(frase)
print("La frase tiene", res, "caracteres")
"""
def cuantasRepeticiones(cadena, letra):
    cont = 0
    for i in range(0, len(cadena)):
        if (letra.lower() == cadena[i].lower()):       
            cont = cont+1
    return cont

frase = str(input("Introduce una frase: "))
letra = str(input("Introduce una letra: "))
res = cuantasRepeticiones(frase, letra)
print("La frase tiene", res, "caracteres", letra)

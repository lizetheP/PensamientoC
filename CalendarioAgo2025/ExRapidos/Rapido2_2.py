import math
def evaluaY(y):
    if y >= 1:
        return y + 3
    else:
        return y / 8

def menu():
    print("1. EvaluaY")
    print("2. Salir")
    
def main():
    menu()
    opcion = int(input("Dame una opción: "))
    if opcion == 1:
        y = float(input("Dame y: "))
        r = evaluaY(y)
        print("El resultado es: %.2f" % r)
    elif opcion == 2:
        print("Adiós")
    else:
        print("ERROR OPCIÓN INVÁLIDA")
main()
print()
main()
print()
main()
print()
main()
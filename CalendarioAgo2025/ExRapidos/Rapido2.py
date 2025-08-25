import math
def evaluaX(x):
    if x > 0:
        return x**2
    else:
        return x*4

def menu():
    print("1. EvaluaX")
    print("2. Salir")
    
def main():
    menu()
    opcion = int(input("Dame una opción: "))
    if opcion == 1:
        x = float(input("Dame x: "))
        r = evaluaX(x)
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

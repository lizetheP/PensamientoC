def evaluaY(y):
    if y >= 1:
        return y+3
    else:
        return y/8
    
def evaluaY(y):
    if y >= 1:
        res = y+3
    else:
        res = y/8
    return res

def evaluaY(y):
    if y >= 1:
        res = y+3
        return res
    else:
        res = y/8
        return res

def menu():
    print("1. EvaluaY")
    print("2. Salir")

def main():
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        num = float(input("Introduce un numero:"))
        res = evaluaY(num)
        print("%.2f" % res)
    elif opcion == 2:
        print("Adios")
    else:
        print("ERROR OPCION INVALIDA")

main()


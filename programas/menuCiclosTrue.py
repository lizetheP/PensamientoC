def menu():
    print("\nMENU")
    print("1. Imprime mensaje")
    print("2. Salir")
    
def main():
    continua = True
    while continua:
        menu()
        opcion = int (input("Introduce una opcion: "))
        if opcion == 1:
            print("Hola a todos")
        elif opcion == 2:
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")
            continua = False
    
main()

def menu():
    print("1. Imprime Mensaje")
    print("2. Salir")
    
def main():    
    continua = True
    while continua:
        print("\n")
        menu()
        opcion = int (input("Introduce una opcion: "))
        if opcion == 1:

        elif opcion == 2:
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")

main()


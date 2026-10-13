def menu():
    print("1. Imprime Mensaje")
    print("2. Salir")
    
def main():    
    continua = True
    while continua == True:
        print()
        menu()
        opcion = int (input("Introduce una opcion: "))
        if opcion == 1:
            print("Hola")
        elif opcion == 2:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")

main()


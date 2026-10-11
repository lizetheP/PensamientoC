def menu():
    print("MENU")
    
def main():
    continua = True
    while continua == True:
        print() # Imprime un salto de línea
        menu()
        opcion = int (input("Introduce una opción: "))
        if opcion == 1:

        elif opcion == 2:
            pass
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()




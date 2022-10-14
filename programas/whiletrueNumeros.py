def menu():
    print()
    print("1. Imprime Mensaje")
    print("2. Salir")

def estadistica_descriptiva(tablero):
    pass

def grafica1(tablero):
    pass

def grafica2(tablero):
    pass

def comprueba_clave(password):
    pass

def main():    
    continua = True
    password = "12345"
    comprueba_clave(password)
    while continua == True:
        menu()
        opcion = int (input("Introduce una opcion: "))
        if opcion == 1:
            print("Hola a todos")
        elif opcion == 2:
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")

main()


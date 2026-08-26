def checaClave(password):
    clave = input("Introduce tu clave de acceso: ")
    while clave != password:
        clave = str(input("Intente nuevamente, introduce tu clave de acceso: "))
    print("Bienvenido")
        
def menu():
    print()
    print("a. Imprime Mensaje")
    print("s. Salir")
    
def main():
    # Carga la información del archivo de Excel en un DataFrame.
    continua = True
    while continua == True:
        menu()
        opcion = input("Introduce una opcion: ")
        if opcion == 1:

        elif opcion == 2:
        
        elif opcion == 3:
        
        elif opcion == 4:
            print("Adios")
            continua = False
        else:
            print("Opción inválida")

main()



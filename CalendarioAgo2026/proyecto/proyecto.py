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
    continua = True
    # Crear Dataframe del archivo de Excel
    password = "Xmen24*" # Definir un password de entrada
    comprueba_clave(password)
    while continua == True:
        menu()
        opcion = input("Introduce una opcion: ")
        if opcion == 1:
            print("Hola a todos")
        elif opcion == 's':
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")

main()


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
    password = "Juanito"
    while continua == True:
        menu()
        checaClave(password)
        opcion = input("Introduce una opcion: ")
        opcion = opcion.lower()
        if opcion == 'a':
            print("Hola a todos")
        elif opcion == 's':
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")

main()


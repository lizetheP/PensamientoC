continua = True
while continua:
    print("\nMENU\n")
    print("a) Imprime Mensaje")
    print("s) Salir")
    opcion = str(input("Introduce una opcion: "))
    if opcion == 'a':
        print("\nHola a todos")
    elif opcion == 's':
        print("\nAdios")
        continua = False
    else:
        print("\nERROR OPCION INVALIDA")
        continua = False
        
        
        
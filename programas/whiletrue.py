continua = True
while continua:
    print("\nMENU\n")
    print("1) Imprime Mensaje")
    print("2) Salir")
    opcion = int (input("Introduce una opcion: "))
    if opcion == 1:
        print("\nHola a todos")
    elif opcion == 2:
        print("\nAdios")
        continua = False
    else:
        print("\n ERROR OPCION INVALIDA")
        continua = False
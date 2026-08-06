def menu():
    print("1. Imprime Mensaje")
    print("2. Salir")
    
def main():    
    continua = True
    while continua == True:
        print("\n")
        menu()
        opcion = int (input("Introduce una opcion: "))
        if opcion == 1:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            print(lista)
        elif opcion == 2:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            inicializa_lista(lista)
            print(lista)
        elif opcion == 3:
            t = int(input("Introduce el tamaño de la lista: "))
            lista = crea_lista(t)
            res = media(lista)
            print("La media es %.2f" % res)
        elif opcion == 4:
            
        elif opcion == 5:
            
        elif opcion == 6:
            
        elif opcion == 7:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")

main()


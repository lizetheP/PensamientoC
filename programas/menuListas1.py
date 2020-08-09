def menu():
    print("\n1.HOla")
    print("2.HOla")
    print("3.HOla")
    
def creaLista(t):
    lista = []
    for i in range(0, t):
        lista.insert(i, i)
    return lista

def main():
    t = int(input("Introduce el tamaño de la lista: "))
    A = creaLista(t)
    continua = True
    while continua:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            print("HOla")   
        elif opcion == 2:
            print("HOla")
        elif opcion == 3:
            print("HOla")
        elif opcion == 4:
            print("Adios")
            continua = False
        else:
            print("ERROR OPCION INVALIDA")
            continua = False
        
main()      
        
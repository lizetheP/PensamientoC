import random

def crea_matriz(renglones, columnas):
    matriz = []
    for i in range(renglones): #numero de listas
        matriz.insert(i, [])
        for j in range(columnas): #número de elementos de cada lista
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def imprime_matriz(matriz):
    for i in range(len(matriz)): #numero de listas de la matriz
        for j in range(len(matriz[i])): #número de elementos de cada lista
            print("%5i" % matriz[i][j], end="")
        print()

def llena_matriz(matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            matriz[i][j]= random.randint(-10,10)
            
    

def menu():
    print("1. Imprime matriz")
    print("2. Llena matriz")
    print("3. Suma positivos")
    print("4. Multiplica renglón")
    print("5. Suma diagonal inversa")
    print("6. Modifica celda")
    print("7. Intercambia renglones")
    print("8. Encuentra grupo")
    print("9. Salir")
    
def main():
    continua = True
    r = int(input("Introduce el número de renglones: "))
    c = int(input("Introduce el número de columnas: "))
    m = crea_matriz(r, c)
    while continua == True:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
           
        elif opcion == 2:
           
        elif opcion == 8:
            print("Adiós")
            continua = False
        else:
            print("Error opción inválida")
            
main()

# Diego iturbe
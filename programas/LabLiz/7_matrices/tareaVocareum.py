import random

def crea_matriz(renglones, columnas):
    matriz = []
    for i in range(renglones):
        matriz.insert(i, [] )
        for j in range(columnas):
            valor = int(input())
            matriz[i].insert(j, valor)
    return matriz

def imprime_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("%2i" % m[i][j], end= ' ')
        print()

def promedio_matriz(m):
    sum = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            sum = sum + m[i][j]
    return sum/(len(m)*len(m[i]))

def mayor_matriz(m):
    may = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > may:
                may = m[i][j]
    return may
 
def posicion_pares(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if m[i][j]%2==0:
                print("El valor %i esta en %i, %i"%(m[i][j], i, j))
                
def suma_diagonal(m):
    suma = 0
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if i == j:
                suma = suma + m[i][j]
    return suma

def menu():
    print()
    print("1. Crea matriz")
    print("2. Imprime matriz")
    print("3. Promedio matriz")
    print("4. Mayor matriz")
    print("5. Posición pares")
    print("6. Suma diagonal")
    print("7. Salir")
    
def main():
    #menu() 
    opcion = int(input()) 
    if opcion == 1:
        ren = int(input())
        col = int(input())
        m = crea_matriz(ren, col)
        print(m)
    elif opcion == 2:
        ren = int(input())
        col = int(input())
        m = crea_matriz(ren, col)
        imprime_matriz(m)
    elif opcion == 3:
        ren = int(input())
        col = int(input())
        m = crea_matriz(ren, col)
        res = promedio_matriz(m)
        print("%.1f" % res)
    elif opcion == 4:
        ren = int(input())
        col = int(input())
        m = crea_matriz(ren, col)
        res = mayor_matriz(m)
        print("%i" % res)
    elif opcion == 5:
        ren = int(input())
        col = int(input())
        m = crea_matriz(ren, col)
        posicion_pares(m)
    elif opcion == 6:
        ren = int(input())
        col = int(input())
        m = crea_matriz(ren, col)
        res = suma_diagonal(m)
        print("%i" % res)
    elif opcion == 7:
        print("Adios")
        continua = False
    else: 
        print("Opcion_invalida") 

main()

"""
1
3
3
3
4
5
6
7
8
9
10
11
[[3, 4, 5], [6, 7, 8], [9, 10, 11]]

2
3
3
3
4
5
6
7
8
9
10
11
 3  4  5 
 6  7  8 
 9 10 11 

3
3
3
3
4
5
6
7
8
9
10
11
7.0

4
3
3
3
4
5
6
7
8
9
10
11
11

5
3
3
3
4
5
6
7
8
9
10
11
El valor 4 esta en 0, 1
El valor 6 esta en 1, 0
El valor 8 esta en 1, 2
El valor 10 esta en 2, 1

6
3
3
3
4
5
6
7
8
9
10
11
21
"""
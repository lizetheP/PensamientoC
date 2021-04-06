import random

def crea_matriz(renglones, columnas):
    matriz = []
    for i in range(renglones):
        matriz.insert(i, [] )
        for j in range(columnas):
            valor = int(input("Introduce un valor: "))
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

def suma_positivos(m):
    acum = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > 0:
                acum = acum + m[i][j]
    return acum

def mayor_matriz(m):
    may = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > may:
                may = m[i][j]
    return may
def modifica_celda(matriz, renglon, columna, valor):
    matriz[renglon][columna] = valor
    
def suma_diagonal_inversa(m):
    acum = 0
    columna = len(m[0])-1
    for i in range(len(m)):
        acum = acum + m[i][columna]
        columna = columna-1
    return acum

def multiplica_renglon(m, renglon, num):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == renglon:
                m[i][j] = m[i][j] * num

def intercambia_renglones(m, r1, r2):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == r1:
                temp = m[r1][j]
                m[r1][j] = m[r2][j]
                m[r2][j] = temp
                
def encuentraGrupo(matriz, cadena):
    acum = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if cadena == matriz[i][j]:
                return matriz[i]
                break
    return "el nombre no es epico"

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

"""def promedio(m):
    acum = 0
    for i in range(0, len(m)):
        columnas = len(m[i])
        for j in range(0, len(m[i])):
            acum = acum + m[i][j]
    return acum/ (len(m)*columnas)

def multiplicaColumna(m, columna, num):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if j == columna:
                m[i][j] = m[i][j] * num
                
def posicionPares(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if m[i][j]%2==0:
                print("El valor %i está en la posición %i, %i"%(m[i][j], i, j))
"""
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
    menu() 
    opcion = int(input("Introduce una opcion: ")) 
    if opcion == 1:
        ren = int(input("Introduce el número de renglones: "))
        col = int(input("Introduce el número de columnas: "))
        m = crea_matriz(ren, col)
        print(m)
    elif opcion == 2:
        ren = int(input("Introduce el número de renglones: "))
        col = int(input("Introduce el número de columnas: "))
        m = crea_matriz(ren, col)
        imprime_matriz(m)
    elif opcion == 3:
        ren = int(input("Introduce el número de renglones: "))
        col = int(input("Introduce el número de columnas: "))
        m = crea_matriz(ren, col)
        res = promedio_matriz(m)
        print("El promedio es: %.1f" % res)
    elif opcion == 4:
        ren = int(input("Introduce el número de renglones: "))
        col = int(input("Introduce el número de columnas: "))
        m = crea_matriz(ren, col)
        res = mayor_matriz(m)
        print("El mayor es: %i" % res)
    elif opcion == 5:
        ren = int(input("Introduce el número de renglones: "))
        col = int(input("Introduce el número de columnas: "))
        m = crea_matriz(ren, col)
        posicion_pares(m)
    elif opcion == 6:
        ren = int(input("Introduce el número de renglones: "))
        col = int(input("Introduce el número de columnas: "))
        m = crea_matriz(ren, col)
        res = suma_diagonal(m)
        print("La suma de la diagonal es: %i" % res)
    elif opcion == 7:
        imprime_matriz(M)
        r = int(input("Introduce el número de renglón: "))
        num = int(input("Introduce el número: "))
        multiplica_renglon(M, r, num)
        imprime_matriz(M)
    elif opcion == 8:
        imprime_matriz(M)
        r1 = int(input("Introduce el renglón 1: "))
        r2 = int(input("Introduce el renglón 2: "))
        intercambia_renglones(M, r1, r2)
        imprime_matriz(M)
    elif opcion == 9:
        cadena = str(input("Introduce un nombre épico: "))
        lista = encuentraGrupo(nombresEpicos, cadena)
        print(lista)
    elif opcion == 9:
        print("Adios")
        continua = False
    else: 
        print("Opcion_invalida") 

main()
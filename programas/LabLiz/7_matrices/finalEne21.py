import random

def crea_matriz(renglones, columnas):
    matriz = []
    for i in range(renglones):
        matriz.insert(i, [] )
        for j in range(columnas):
            valor = int(input())
            matriz[i].insert(j, valor)
    return matriz

def suma_renglon(m, r):
    acum = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == r:
                acum = acum + m[i][j]
    return acum

def main():
    ren = int(input())
    col = int(input())
    m = crea_matriz(ren, col)
    r = int(input())
    res = suma_renglon(m, r)
    print(res)
    
main()
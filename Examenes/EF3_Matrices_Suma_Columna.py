def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def suma_columna(matriz, c):
    acum = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == c:
                acum = acum + matriz[i][j]
    return acum

def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    c = int(input("Introduce la columna: "))
    res = suma_columna(matriz, c)
    print("La suma es", res)
    
main()
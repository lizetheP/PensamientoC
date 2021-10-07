def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def multiplica_columna(matriz, c, n):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == c:
                matriz[i][j] = matriz[i][j] * n

def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    c = int(input("Introduce la columna: "))
    n = int(input("Introduce n: "))
    multiplica_columna(matriz, c, n)
    print(matriz)
    
main()
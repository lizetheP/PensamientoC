def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def intercambia_columnas(matriz, c1, c2):
    for i in range(len(matriz)):
        temp = matriz[i][c1]
        matriz[i][c1] = matriz[i][c2]
        matriz[i][c2] = temp
        
def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    c1 = int(input("Introduce la columna 1: "))
    c2 = int(input("Introduce la columna 2: "))
    intercambia_columnas(matriz, c1, c2)
    print(matriz)
    
main()
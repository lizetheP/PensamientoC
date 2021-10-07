def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def menor_matriz(matriz):
    menor = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return menor

def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    res =menor_matriz(matriz)
    print("El menor es: ", res)
    
main()
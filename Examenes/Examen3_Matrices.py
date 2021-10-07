def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def promedio_matriz(matriz, n):
    acum = 0
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % n == 0:
                acum = acum + matriz[i][j]
                cont = cont + 1
    return acum/cont

def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    n = int(input("Introduce un valor: "))
    res = promedio_matriz(matriz, n)
    print("El promedio es: %.2f" % res)
    
main()

#Reemplaza por x e imprime la posición

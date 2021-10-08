def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def reemplaza_matriz(matriz, n):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                matriz[i][j] = n
   
def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    n = int(input("Introduce un valor: "))
    reemplaza_matriz(matriz, n)
    print(matriz)
        
main()

#Reemplaza por x e imprime la posición

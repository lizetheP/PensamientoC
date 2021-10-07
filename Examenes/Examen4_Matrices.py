def crea_matriz(r, c):
    matriz = []
    for i in range(r):
        matriz.insert(i, [])
        for j in range(c):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def posicion_multiplos(matriz, n):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % n == 0:
                print("El valor %i esta en %i, %i" % (matriz[i][j], i, j))
   
def main():
    r = int(input("Introduce los renglones: "))
    c = int(input("Introduce las columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    n = int(input("Introduce un valor: "))
    posicion_multiplos(matriz, n)
        
main()

#Reemplaza por x e imprime la posición


def crea_matriz(renglones, columnas):
    matriz = []
    for i in range(renglones):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(5)
    return matriz

def crea_matriz2(renglones, columnas):
    matriz = []
    for i in range(renglones):
        matriz.insert(i, [])
        for j in range(columnas):
            matriz[i].insert(j, 5)
    return matriz

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
        
def inicia_matriz(matriz):
    cont = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = cont
            cont = cont + 1
    
def suma_matrices(m1, m2, m3):
    cont = 1
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m3[i][j] = m1[i][j] + m2[i][j]
            
def main():
    r = int(input("Introduce renglones: "))
    c = int(input("Introduce columnas: "))
    m = crea_matriz2(r, c)
    imprime_matriz(m)
    
    print()
    m2 = crea_matriz2(r, c)
    inicia_matriz(m2)
    imprime_matriz(m2)
    
    print()
    m3 = crea_matriz2(r, c)
    suma_matrices(m, m2, m3)
    imprime_matriz(m3)
    
main()
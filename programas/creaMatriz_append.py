def crea_matriz(renglones, columnas):
    matriz = []
    for i in range(0, renglones):
        matriz.append([])
        for j in range(0, columnas):
            matriz[i].append(5)  
    return matriz

def main():
    r = int(input("Introduce el número de renglones: "))
    c = int(input("Introduce el número de columnas: "))
    matriz = crea_matriz(r, c)
    print(matriz)
    
main()


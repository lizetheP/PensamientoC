def posicion_vocales(cadena):
    vocales = 'aeiou'
    for i in range(len(cadena)):
        if cadena[i].lower() in vocales: 
            print(i)

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
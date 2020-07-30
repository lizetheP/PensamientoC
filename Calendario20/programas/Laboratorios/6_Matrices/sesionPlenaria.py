def imprimeMatriz(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            print(m[i][j], end= ' ')
        print()

def promedio(m):
    acum = 0
    for i in range(0, len(m)):
        columnas = len(m[i])
        for j in range(0, len(m[i])):
            acum = acum + m[i][j]
    return acum/ (len(m)*columnas)

def multiplicaColumna(m, columna, num):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if j == columna:
                m[i][j] = m[i][j] * num
                
def posicionPares(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if m[i][j]%2==0:
                print("El valor %i está en la posición %i, %i"%(m[i][j], i, j))

def menu():
    print()
    print("1. Promedio matriz")
    print("2. Multiplica columna")
    print("3. Posicion pares")
    

#M = [ [1,2,3,4], [2,1,2,2], [3,2,1,2], [4,2,2,1] ] # Declarar una matriz
M = [ [2,5,6,4], [3,4,5,1], [7,8,5,6], [9,7,1,5] ] # Declarar una matriz

while True: 
    menu() 
    opcion = int(input("Introduce una opcion: ")) 
    if opcion == 1:
        imprimeMatriz(M)
        res = promedio(M)
        print("El promedio es: ", res)
    elif opcion == 2: 
        imprimeMatriz(M)
        c = int(input("Introduce el número de columna: "))
        num = int(input("Introduce el número: "))
        multiplicaColumna(M, c, num)
        imprimeMatriz(M)
    elif opcion == 3:
        imprimeMatriz(M)
        posicionPares(M)
    else: 
         print("Opción inválida") 
         break

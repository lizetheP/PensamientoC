def crea_matriz(renglones,columnas): 
    matriz=[]
    for i in range(0,renglones):
        matriz.insert(i,[])
        for j in range(0,columnas):
            valor= int(input())
            matriz[i].insert(j,valor)
    return matriz

def imprime_matriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            print("%2i" % m[i][j], end= ' ')
        print()
            
def promedio_matriz(matriz):
    acum=0
    prom=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            acum=acum + matriz[i][j]
    prom=acum/(len(matriz)*len(matriz[0]))
    return prom

def mayor_matriz(matriz):
    m=matriz[0][0]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz [i][j] >m:
                m=matriz[i][j]
    return m

def posicion_pares(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if (matriz[i][j]%2==0):
                print("El valor %i esta en %i,%i" %(matriz[i][j],i,j))
                
def suma_diagonal(matriz):
    acum=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i]== matriz[j]:
                acum=acum+matriz[i][j]
    return acum
                            
                   
def menu():
    print("1. Crea matriz")
    print("2. Imprime matriz")
    print("3. Promedio matriz")
    print("4. Mayor matriz")
    print("5. Posición pares")
    print("6. Suma diagonal")
    print("7. Salir")
            

def main():
    #menu()
    opcion=int(input())
    if opcion==1:
        renglones=int(input())
        columnas=int(input())
        matriz= crea_matriz(renglones,columnas)       
        print(matriz)
    elif opcion==2:
        renglones=int(input())
        columnas=int(input())
        matriz= crea_matriz(renglones,columnas)        
        imprime_matriz(matriz)
    elif opcion==3:
        renglones=int(input())
        columnas=int(input())
        matriz= crea_matriz(renglones,columnas) 
        res=promedio_matriz(matriz)
        print("%0.1f"%res)
    elif opcion==4:
        renglones=int(input())
        columnas=int(input())
        matriz= crea_matriz(renglones,columnas) 
        res=mayor_matriz(matriz)
        print("%i"%res)
    elif opcion==5:
        renglones=int(input())
        columnas=int(input())
        matriz= crea_matriz(renglones,columnas)        
        posicion_pares(matriz)
    elif opcion==6:
        renglones=int(input())
        columnas=int(input())
        matriz= crea_matriz(renglones,columnas)        
        res=suma_diagonal(matriz)
        print("%i"%res)
    elif opcion==7:
        print("Adios")
    else:
        print("Opcion_invalida")
            
main() 

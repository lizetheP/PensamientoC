import numpy as np

def imprime_multiplos(A, x):
    for i in range(A.size):
        if A[i] % x == 0:
            print("A[%i] = %i" % (i, A[i]))

def promedio_multiplos(A, x):
    acum = 0
    cont = 0
    for i in range(A.size):
        if A[i] % x == 0:
            acum = acum + A[i]
            cont = cont + 1
    return acum / cont

def menu():
    print()
    print("1. Imprime múltiplos")
    print("2. Promedio múltiplos")
    print("3. Salir")
    
def main():
    continua = True
    arreglo = np.array([1, 3, 5, 10, -3, 12, 5, 9, 9, -5])
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            x = int(input("Dame x: "))
            imprime_multiplos(arreglo, x)
        elif opcion == 2:
            x = int(input("Dame x: "))
            if arreglo.size > 0:
                res = promedio_multiplos(arreglo, x)
                print("El promedio del arreglo es: %.2f" % res)
            else:
                print("Error el arreglo está vacio")
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()
"""
def main():
    lista = np.array([2.8, 8.3, 5.4, 6.0, 5.2, 1.5, 6.4, 12, 7.1, 3.6], float)
    a = np.array([1, 3, 5, 10, -3, 12, 5, 9, 9, -5])
    print(a)
    print(lista)
    prom = lista.mean()
    print("El promedio con la función mean es %.2f" % prom)
    prom = promedio(lista)
    print("El promedio con iterador es %.2f" % prom) 
    arr = np.array([12, 7, 6, 11, 2, 9, 15, 5, 14])
    p = np.mean(arr) # Se obtiene 9.0
    varianza = np.var(arr) # Se obtiene 9.0
    desviacion = np.std(arr) # Se obtiene 9.0
    print("Promedio", p)
    print("Varianza", varianza)
    print("Desviación", desviacion)
    

main()
    
"""
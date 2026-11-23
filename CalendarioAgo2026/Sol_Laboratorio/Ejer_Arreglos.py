import numpy as np

def promedio(A):
    acum = 0
    for i in range(A.size):
        acum = acum + A[i]
    return acum / A.size

def sumaDos(A):
    for i in range(A.size):
        A[i] = A[i] + 2
    return A

def imprime(A):
    for i in range(A.size):
        print("A[%i] = %.1f" % (i, A[i]))
    
def menu():
    print()
    print("1. Promedio")
    print("2. Suma dos")
    print("3. Imprime")
    print("4. Salir")
    
def main():
    continua = True
    arreglo = np.array([2.8, 8.3, 5.4, 6.0, 5.2, 1.5, 6.4, 12, 7.1, 3.6])
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            print(arreglo)
            if arreglo.size > 0:
                res = promedio(arreglo)
                print("El promedio del arreglo es: %.2f" % res)
                res2 = np.mean(arreglo)
                print("El promedio del arreglo es: %.2f" % res2)
            else:
                print("Error el arreglo está vacio")
        elif opcion == 2:
            print(arreglo)
            arreglo2 = sumaDos(arreglo)
            print(arreglo2)
        elif opcion == 3:
            print(arreglo)
            imprime(arreglo)
        elif opcion == 4:
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
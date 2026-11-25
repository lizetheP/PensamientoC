import numpy as np
def atributos(matriz):
    print("Dimensiones (ndim):", matriz.ndim)
    print("Renglones y columnas (shape):", matriz.shape)
    print("Total de elementos (size):", matriz.size)

def operaciones1():
    print("\nSUMA DE MATRICES")
    X = np.array([[1, 2, 3], [4, 5, 6]]) 
    Y = np.array([[6, 5, 4], [3, 2, 1]])
    Z = X + Y
    print(Z)
    
    print("\nRESTA DE MATRICES")
    A = np.array([[10, 20], [30, 40], [50, 60]]) 
    B = np.array([[1, 2], [3, 4], [5, 6]]) 
    C = np.subtract(A, B)
    print(C)
    
    print("\nMULTIPLICA MATRICES")
    P = np.array([[2, 4], [6, 8]]) 
    Q = np.array([[1, 3], [5, 7]]) 
    M1 = P * Q
    print(M1)
    M2 = np.multiply(P, Q)
    print(M2)
    
    print("\nDIVIDE MATRICES")
    numeradores = np.array([[20, 40],
                            [60, 80]])
    denominadores = np.array([[2, 4],
                              [5, 8]])
    division = np.divide(numeradores, denominadores)
    print(division)
    
    print("\nPOTENCIA")
    base = np.array([[2, 3],
                     [4, 5]])
    exponente = np.array([[3, 2],
                          [2, 1]])
    potencia = np.power(base, exponente)
    print(potencia)

def operaciones2():
    print("\nCALIFICACIONES FINALES")
    calificaciones = np.array([[60, 75, 80], [85, 70, 90], [65, 88, 72]])
    final = calificaciones + 5
    print(final)
    
    print("\nAJUSTE PORCENTUAL")
    sueldos = np.array([[10000, 12000, 15000], [18000, 20000, 25000]])
    sueldos_aumento = sueldos * 1.10
    print(sueldos_aumento)
    
def operaciones3():
    print("\nSUMA DIAGONAL")
    M = np.array([[12, 4, 7],
                  [3, 9, 1],
                  [8, 2, 5]])
    diagonal = np.trace(M)
    print(M)
    print("La suma de la diagonal es:", diagonal)
    print("\nTRANSPUESTA")
    M = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
    print(M)
    transpuesta = np.transpose(M)
    print(transpuesta)
    
    print("\nDETERMINANTE")
    M = np.array([[6, 4],
                  [2, 5]])
    determinante = np.linalg.det(M)
    print(M)
    print("La determinante es: %.2f" % determinante)
    
def menu():
    print()
    print("1. Atributos")
    print("2. Operaciones aritméticas")
    print("3. Operaciones con un escalar")
    print("4. Operaciones de álgebra lineal")
    print("5. Salir")
    
def main():
    continua = True
    arreglo = np.array([2.8, 8.3, 5.4, 6.0, 5.2, 1.5, 6.4, 12, 7.1, 3.6])
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            B = np.array([[10, 11, 12, 13],
                          [14, 15, 16, 17],
                          [18, 19, 20, 21]])
            atributos(B)
        elif opcion == 2:
            operaciones1()
        elif opcion == 3:
            operaciones2()
        elif opcion == 4:
            operaciones3()
        elif opcion == 5:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()
"""
import numpy as np

def atributos(matriz):
    # Completa el codigo
    
def operaciones1():
    print("\nSUMA DE MATRICES")
    X = np.array([[1, 2, 3], [4, 5, 6]]) 
    Y = np.array([[6, 5, 4], [3, 2, 1]])
    # COMPLETAR CÓDIGO
    
    print("\nRESTA DE MATRICES")
    A = np.array([[10, 20], [30, 40], [50, 60]]) 
    B = np.array([[1, 2], [3, 4], [5, 6]]) 
    # COMPLETAR CÓDIGO
    
    print("\nMULTIPLICA MATRICES")
    P = np.array([[2, 4], [6, 8]]) 
    Q = np.array([[1, 3], [5, 7]]) 
    # COMPLETAR CÓDIGO
    
    print("\nDIVIDE MATRICES")
    numeradores = np.array([[20, 40],
                            [60, 80]])
    denominadores = np.array([[2, 4],
                              [5, 8]])
    # COMPLETAR CÓDIGO
    
    print("\nPOTENCIA")
    base = np.array([[2, 3],
                     [4, 5]])
    exponente = np.array([[3, 2],
                          [2, 1]])
    # COMPLETAR CÓDIGO

def operaciones2():
    print("\nCALIFICACIONES FINALES")
    calificaciones = np.array([[60, 75, 80], [85, 70, 90], [65, 88, 72]])
    # COMPLETAR CÓDIGO
    
    print("\nAJUSTE PORCENTUAL")
    sueldos = np.array([[10000, 12000, 15000], [18000, 20000, 25000]])
    # COMPLETAR CÓDIGO
    
def operaciones3():
    print("\nSUMA DIAGONAL")
    M = np.array([[12, 4, 7],
                  [3, 9, 1],
                  [8, 2, 5]])
    # COMPLETAR CÓDIGO
    
    print("\nTRANSPUESTA")
    M = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
    # COMPLETAR CÓDIGO
    
    print("\nDETERMINANTE")
    M = np.array([[6, 4],
                  [2, 5]])
    # COMPLETAR CÓDIGO
    
def menu():
    print()
    print("1. Atributos")
    print("2. Operaciones aritméticas")
    print("3. Operaciones con un escalar")
    print("4. Operaciones de álgebra lineal")
    print("5. Salir")
    
def main():
    continua = True
    arreglo = np.array([2.8, 8.3, 5.4, 6.0, 5.2, 1.5, 6.4, 12, 7.1, 3.6])
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            B = np.array([[10, 11, 12, 13],
                          [14, 15, 16, 17],
                          [18, 19, 20, 21]])
            atributos(B)
        elif opcion == 2:
            operaciones1()
        elif opcion == 3:
            operaciones2()
        elif opcion == 4:
            operaciones3()
        elif opcion == 5:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()
"""
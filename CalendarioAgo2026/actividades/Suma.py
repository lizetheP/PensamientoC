import numpy as np
arreglo1 = np.array([1, 7, 6, 3, 1, 8, 5, 2, 9])
arreglo2 = np.array([3, 6, 8, 4, 2, 9, 1, 5, 4])

#Opción 1: Usando el operador + 
arreglo_operador = arreglo1 + arreglo2
print("Resultado con '+':", arreglo_operador)

#Opción 2: Usando la función explícita np.add()
arreglo_funcion = np.add(arreglo1, arreglo2)
print("Resultado con 'np.add()':", arreglo_funcion)


arreglo1 = np.array([50, 45, 40, 35, 30, 25, 20, 15, 10, 5])
arreglo2 = np.array([5, 5, 10, 10, 15, 15, 20, 20, 25, 25])
#Opción 1: Usando el operador - 
arreglo_operador = arreglo1 - arreglo2
print("Resultado con '-':", arreglo_operador)
#Se obtiene: [ 4 13 14  7  3 17  6  7 13]
#Opción 2: Usando la función explícita np.subtract()
arreglo_funcion = np.subtract(arreglo1, arreglo2)
print("Resultado con ‘np.subtract()':", arreglo_funcion)
#Se obtiene: [ 4 13 14  7  3 17  6  7 13]

# Matriz de 2 filas x 3 columnas
matriz_2x3 = np.array([[1, 2, 3],
                       [4, 5, 6]])

# Transpuesta
transpuesta = np.transpose(matriz_2x3)

print("Original (2x3):\n", matriz_2x3)
print("Transpuesta (3x2):\n", transpuesta)


matriz = np.array([[5, 2, 9], [1, 8, 4], [3, 7, 6]]) 
#Calcular la traza 
traza = np.trace(matriz) 
print("Matriz:\n", matriz) 
print("\nTraza de la matriz:", traza)


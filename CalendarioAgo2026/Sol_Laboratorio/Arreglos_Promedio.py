import numpy as np

def promedio(arreglo):
    acum = 0
    for i in range(arreglo.size):
        acum = acum + arreglo[i]
    return acum / arreglo.size
    
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
    

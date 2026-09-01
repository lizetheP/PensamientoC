import pandas as pd
import numpy as np

def estadistica_descriptiva (tablero):
    salarios = tablero["SALARIO"]
    lista = list(salarios)
    print(lista)
    arreglo = np.array(salarios)
    print(arreglo)
    print("Mínimo: ", np.min(arreglo))
    print("Máximo: ", np.max(arreglo))
    print("Promedio: ", np.mean(arreglo))
    print("Mediana: ", np.median(arreglo))
    print("Varianza: ", np.var(arreglo))
    print("Desviación estándar: ", np.std(arreglo))

def main():
    tabla = pd.read_excel("vendedores.xlsx")
    estadistica_descriptiva (tabla)
    
main()
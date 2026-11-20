import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

def estadistica_descriptiva(lista):
    maximo = np.max(lista)
    minimo = np.min(lista)
    promedio = np.mean(lista)
    mediana = np.median(lista)
    moda = statistics.mode(lista)
    desviacion = statistics.stdev(lista)
    print("Máximo = %.2f" % maximo)
    print("Mínimo = %.2f" % minimo)
    print("Promedio = %.2f" % promedio)
    print("Mediana = %.2f" % mediana)
    print("Moda = %.2f" % moda)
    print("Desviación estándar = %.2f" % desviacion)
    
def unidades_vendedor(reporte):
    #groupby("COLUMNA").get_group("valor")
    reporteEste = reporte.groupby("REGION").get_group("ESTE")
    print(reporteEste)
    nombres = reporteEste["NOMBRE"]
    print(nombres)
    unidades = reporteEste["UNIDADES VENDIDAS"]
    print(unidades)
    plt.bar(nombres, unidades)
    plt.title("Unidades vendidas por vendedor en la región ESTE")
    plt.xlabel("Vendedores")
    plt.ylabel("Unidades vendidas")
    plt.xticks(rotation = 50)
    plt.show()
 
def promedio_salarioxregion(reporte):
    regiones = ["SUR", "NORTE", "ESTE", "OESTE"]
    promedio_salarios = []
    for region in regiones:
        print()
        print(region)
        reportexRegion = reporte.groupby("REGION").get_group(region)
        print(reportexRegion)
        salarios = reportexRegion["SALARIO"]
        print(salarios)
        promedio = salarios.mean()
        promedio_salarios.append(promedio)
    print(promedio_salarios)
    barlist = plt.bar(regiones, promedio_salarios)
    barlist[0].set_color('r')
    barlist[1].set_color('g')
    barlist[2].set_color('b')
    barlist[3].set_color('c')
    plt.title("Promedio de salario por region")
    plt.xlabel("Regiones")
    plt.ylabel("Promedio de salario")
    plt.show()
    
def promedio_ventas_region(reporte):
    regiones = ["SUR", "NORTE", "ESTE", "OESTE"]
    suma_ventas = []
    for region in regiones:
        reportexRegion = reporte.groupby("REGION").get_group(region)
        ventasxRegion = reportexRegion["VENTAS TOTALES"]
        suma = ventasxRegion.sum()
        suma_ventas.append(suma)
    print(suma_ventas)
    barlist = plt.bar(regiones, promedio_ventas)
    barlist[0].set_color('r')
    barlist[1].set_color('g')
    barlist[2].set_color('b')
    barlist[3].set_color('c')
    plt.title("Total de ventas por region")
    plt.xlabel("Regiones")
    plt.ylabel("Suma de ventas")
    plt.show()

def promedio_ventas_region2(reporte):
    #Por región, calcula el promedio de las ventas totales
    grupo = (reporte.groupby("REGION")["VENTAS TOTALES"]
                                  .mean()
                                  .sort_values())
    #Por región, calcula la suma de las ventas totales
    grupo2 = reporte.groupby("REGION")["VENTAS TOTALES"].sum()
    print(grupo)
    regiones = grupo.index
    promedio_ventas = grupo.values
    barlist = plt.bar(regiones, promedio_ventas)
    barlist[0].set_color('r')
    barlist[1].set_color('g')
    barlist[2].set_color('b')
    barlist[3].set_color('c')
    plt.title("Promedio de ventas por region")
    plt.xlabel("Regiones")
    plt.ylabel("Promedio de ventas")
    plt.show()
      
def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Promedio de salario por región")
    print("2. Total de ventas por región")
    print("3. Salir")
    
def main():
    reporte = pd.read_excel("vendedores.xlsx")
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            lista = reporte["SALARIO"]
            print(lista)
            estadistica_descriptiva(lista)
        elif opcion == 2:
            promedio_salarioxregion(reporte)
        elif opcion == 3:
            promedio_ventas_region(reporte)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()

"""
    print(arreglo)
    maximo = arreglo.max()
    minimo = arreglo.min()
    promedio = arreglo.mean()
    #mediana = arreglo.median()
    #moda = arreglo.mode()
    varianza = arreglo.var()
    desviacion = arreglo.std()
"""
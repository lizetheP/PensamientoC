import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

def estadistica_descriptiva(lista):
    arreglo = np.array(lista)
    print(arreglo)
    maximo = arreglo.max()
    minimo = arreglo.min()
    suma = arreglo.sum()
    promedio = arreglo.mean()
    varianza = arreglo.var()
    desviacion = arreglo.std()
    
    print("Máximo = %.2f" % maximo)
    print("Mínimo = %.2f" % minimo)
    print("Suma = %.2f" % suma)
    print("Promedio = %.2f" % promedio)
    print("Varianza = %.2f" % varianza)
    print("Desviación estándar = %.2f" % desviacion)
    
def operaciones(arreglo1, arreglo2):
    totalVentas = reporte.groupby("REGION")["VENTAS TOTALES"].sum()
    print(totalVentas)
    plt.bar(totalVentas.index, totalVentas.values, color=['r', 'g', 'b', 'c'])
    plt.show()

def promedio_salarioxregion(reporte):
    promedioSalario = reporte.groupby("REGION")["SALARIO"].mean()
    print(promedioSalario)
    plt.bar(promedioSalario.index, promedioSalario.values, color=['r', 'g', 'b', 'c'])
    plt.show()

def suma_ventasxregion2(reporte):
    totalVentas = reporte.groupby("REGION")["VENTAS TOTALES"].sum()
    print(totalVentas)
    plt.plot(totalVentas.index, totalVentas.values, "r*--")
    plt.show()

def promedio_salarioxregion2(reporte):
    promedioSalario = reporte.groupby("REGION")["SALARIO"].mean()
    print(promedioSalario)
    plt.plot(promedioSalario.index, promedioSalario.values, "cD:")
    plt.show()
    
"""    
def promedio_salarioxregion(reporte):
    regiones = ["SUR", "NORTE", "ESTE", "OESTE"]
    promedios = reporte.groupby("REGION")["VENTAS TOTALES"].mean()
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
"""
def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Promedio de salario por región en barras")
    print("3. Total de ventas por región en barras")
    print("4. Promedio de salario por región en línea")
    print("5. Total de ventas por región en línea")
    print("6. Salir")
    
def main():
    reporte = pd.read_excel("vendedores.xlsx")
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            lista = reporte["SALARIO"]
            print(lista)
            print("\nSALARIOS")
            estadistica_descriptiva(lista)
        elif opcion == 2:
            print()
            print("PROMEDIO DE SALARIOS POR REGIÓN")
            promedio_salarioxregion(reporte)
        elif opcion == 3:
            print()
            print("SUMA DE VENTAS POR REGIÓN")
            suma_ventasxregion(reporte)
        elif opcion == 4:
            print()
            print("PROMEDIO DE SALARIOS POR REGIÓN")
            promedio_salarioxregion2(reporte)
        elif opcion == 5:
            print()
            print("SUMA DE VENTAS POR REGIÓN")
            suma_ventasxregion2(reporte)
        elif opcion == 6:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()


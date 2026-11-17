import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

def cantidad_productos(reporte):
    #groupby("COLUMNA").get_group("valor")
    reporteCondimentos = reporte.groupby("categoria").get_group("Condimento")
    #print(reporteCondimentos)
    nombres = reporteCondimentos["nombre"]
    #print(nombres)
    cantidad = reporteCondimentos["cantidadExistencia"]
    #print(cantidad)
    plt.bar(nombres, cantidad)
    plt.title("Cantidad de productos en existencia de la categoría de Condimentos")
    plt.xlabel("Productos")
    plt.ylabel("Cantidad")
    plt.xticks(rotation = 90)
    plt.show()
    
def precios_productos(reporte):
    #groupby("COLUMNA").get_group("valor")
    reporteFrascos = reporte.groupby("envase").get_group("Frasco")
    #print(reporteFrascos)
    nombres = reporteFrascos["nombre"]
    #print(nombres)
    precios = reporteFrascos["precioMenudeo"]
    #print(precios)
    plt.plot(nombres, precios, "rD-.")
    plt.title("Precios de los productos del tipo de envase Frasco")
    plt.xlabel("Productos")
    plt.ylabel("Precios de menudeo")
    plt.xticks(rotation = 90)
    plt.show()
       
def menu():
    print()
    print("1. Cantidad de productos")
    print("2. Precio de productos")
    print("3. Salir")
    
def main():
    reporte = pd.read_excel("inventario.xlsx")
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            cantidad_productos(reporte)
        elif opcion == 2:
            precios_productos(reporte)
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()
"""
def main():
    reporte = pd.read_excel("inventario.xlsx")
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:

        elif opcion == 2:

        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
"""
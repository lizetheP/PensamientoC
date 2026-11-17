import pandas as pd
import matplotlib.pyplot as plt
#import openpyxl

def ventas_pan(reporte):
    reportePan = reporte.groupby("Subcategoria").get_group("Pan Dulce")
    print(reportePan)
    sucursales = reportePan["Sucursal"]
    ventas = reportePan["Ventas"]
    plt.bar(sucursales, ventas)
    plt.title("Ventas de pan dulce por sucursal")
    plt.xlabel("Sucursales")
    plt.ylabel("Ventas")
    plt.xticks(rotation = 15)
    plt.show()

def ganancias_condesa(reporte):
    reporteCondesa = reporte.groupby("Sucursal").get_group("Condesa")
    print(reporteCondesa)      
    subcategorias = reporteCondesa["Subcategoria"]
    ganancias = reporteCondesa["Ganancia"]
    print(ganancias)
    plt.plot(subcategorias, ganancias, "mH:")
    plt.title("Ganancias por subcategoría en la Condesa")
    plt.xlabel("Subcategorias")
    plt.ylabel("Ganancias")
    plt.xticks(rotation = 20)
    plt.show()
    
def menu():
    print()
    print("1. Ventas de pan dulce")
    print("2. Ganancias en la Condesa")
    print("3. Salir")
    
def main():
    continua = True
    reporte = pd.read_excel("Cielito.xlsx")
    print(reporte)
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            ventas_pan(reporte)
        elif opcion == 2:
            ganancias_condesa(reporte)
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")

main()

"""
def main():
    continua = True
    reporte = pd.read_excel("Cielito.xlsx")
    print(reporte)
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:

        elif opcion == 2:
            pass
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")

main()


def main():
    continua = True
    reporte = pd.read_excel("Cielito.xlsx")
    print(reporte)
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:

        elif opcion == 2:
            pass
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")


    barras = plt.bar(tiendas, ventas)

    # Colocando colores a las barras
    barras[0].set_color('b')
    barras[1].set_color('g')
    barras[2].set_color('r')
    barras[3].set_color('c')
    barras[4].set_color('m')
"""  
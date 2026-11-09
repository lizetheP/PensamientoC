import numpy as np
import matplotlib.pyplot as plt
import statistics

# -------------------------------------------------------------------
# --------- Estadística descriptiva ---------------------------------
# -------------------------------------------------------------------

def estadistica_descriptiva(calificaciones):
    print()
    print("ESTADÍSTICA DESCRIPTIVA")
    print()
    print("Calificaciones:", calificaciones)
    maximo = np.max(calificaciones)
    minimo = np.min(calificaciones)
    promedio = np.mean(calificaciones)
    mediana = np.median(calificaciones)
    moda = statistics.mode(calificaciones)
    desviacion = statistics.stdev(calificaciones)
    num_90 = calificaciones.count(90)
    print("Máximo = %i" % maximo)
    print("Mínimo = %i" % minimo)
    print("Promedio = %.2f" % promedio)
    print("Mediana = %.2f" % mediana)
    print("Moda = %.2f" % moda)
    print("Desviación estándar = %.2f" % desviacion)
    print("Número de 90s =", num_90)
    
def ventas_productos1(productos, ventas1, ventas2):
    plt.subplot(121)
    plt.title("Ventas de septiembre")
    plt.xlabel("Productos")
    plt.ylabel("Ventas")
    barras = plt.bar(productos, ventas1)
    # Colocando colores a las barras
    barras[0].set_color('b')
    barras[1].set_color('g')
    barras[2].set_color('r')
    barras[3].set_color('c')
    barras[4].set_color('m')
    
    plt.subplot(122)
    plt.title("Ventas de octubre")
    plt.xlabel("Productos")
    plt.ylabel("Ventas")
    barras = plt.bar(productos, ventas2)
    # Colocando colores a las barras
    barras[0].set_color('b')
    barras[1].set_color('g')
    barras[2].set_color('r')
    barras[3].set_color('c')
    barras[4].set_color('m')
    plt.show()
    
    
def ventas_productos2(productos, ventas1, ventas2):
    plt.title("Ventas de productos")
    plt.xlabel("Productos")
    plt.ylabel("Ventas")
    # Graficando
    plt.plot(productos, ventas1, "r*-.", productos, ventas2, "g>-") 
    plt.legend(["Septiembre", "Octubre"])
    # Mostrando el gráfico
    plt.show()

def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Gráfica de ventas con barras")
    print("3. Gráfica de ventas con líneas")
    print("4. Salir")
    
def main():
    continua = True
    calificaciones = [100, 90, 84, 63, 95, 98, 90, 75]
    productos = ["Aceite", "Arroz", "Atún", "Jabón", "Suavizante"]
    ventas1 = [47, 35, 54, 28, 16]
    ventas2 = [35, 40, 19, 58, 27]
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:      
            estadistica_descriptiva(calificaciones)
        elif opcion == 2:
            ventas_productos1(productos, ventas1, ventas2)
        elif opcion == 3:
            ventas_productos2(productos, ventas1, ventas2)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()
"""
def main():
    continua = True
    calificaciones = [100, 90, 84, 63, 95, 98, 90, 75]
    productos = ["Aceite", "Arroz", "Atún", "Jabón", "Suavizante"]
    ventas1 = [47, 35, 54, 28, 16]
    ventas2 = [35, 40, 19, 58, 27]
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:      

        elif opcion == 2:

        elif opcion == 3:
        
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()
"""



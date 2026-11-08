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
    
def precios_productos(productos, precios):
    plt.title("Precios de productos")
    plt.xlabel("Productos")
    plt.ylabel("Precios")
    barras = plt.bar(productos, precios)
    # Colocando colores a las barras
    barras[0].set_color('b')
    barras[1].set_color('g')
    barras[2].set_color('r')
    barras[3].set_color('c')
    barras[4].set_color('m')
    plt.show()
    
def ventas_productos(productos, ventas):
    plt.title("Ventas de productos")
    plt.xlabel("Productos")
    plt.ylabel("Ventas")
    # Graficando
    plt.plot(productos, ventas, "r*-.")
    # Mostrando el gráfico
    plt.show()

def menu():
    print()
    print("1. Gráfica de precios")
    print("2. Gráfica de ventas")
    print("3. Salir")
    
def main():
    continua = True
    productos = ["Aceite", "Arroz", "Atún", "Jabón", "Suavizante"]
    precios = [46, 39, 21, 28, 130]
    ventas = [47, 35, 54, 28, 16] 
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:      
            precios_productos(productos, precios)
        elif opcion == 2:
            ventas_productos(productos, ventas)
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()


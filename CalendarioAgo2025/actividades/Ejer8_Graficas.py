import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

# -------------------------------------------------------------------
# --------- Estadística descriptiva ---------------------------------
# -------------------------------------------------------------------

def estadistica_descriptiva(pesos):
    print()
    print("ESTADÍSTICA DESCRIPTIVA")
    print()
    print("Pesos:", pesos)
    maximo = np.max(pesos)
    minimo = np.min(pesos)
    promedio = statistics.mean(pesos)
    mediana = statistics.median(pesos)
    moda = statistics.mode(pesos)
    desviacion = statistics.stdev(pesos)
    print("Máximo = %i" % maximo)
    print("Mínimo = %i" % minimo)
    print("Promedio = %.2f" % promedio)
    print("Mediana = %.2f" % mediana)
    print("Moda = %.2f" % moda)
    print("Desviación estándar = %.2f" % desviacion)
    print("Número de 70s =", pesos.count(70))
    
def tipos_cambio(meses, dolar, euro):
    plt.title("Tipos de cambio")
    plt.xlabel("Meses")
    plt.ylabel("Dólar / Euro")

    #"r*-." Estrellas color rojo unidas por raya y puntos alternados
    #"g>-" Flechas color verde unidos por raya continua
    plt.plot(meses, dolar, "r*-.", meses, euro, "g>-") 
    plt.legend(["Dólar", "Euro"])

    #Rotación 45 grados de etiquetas en el eje x
    #plt.xticks(rotation = 45)

    plt.show()

def tipos_cambio2(meses, dolar, euro):
    #divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
    plt.subplot(121)
    plt.xlabel("Meses")
    plt.ylabel("Dólar")
    plt.title("Peso vs Dólar")
    plt.plot(meses, dolar, "c*-") # Estrellas color cian unidas por raya continua

    #divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
    plt.subplot(122)
    plt.xlabel("Meses")
    plt.ylabel("Euro")
    plt.title("Peso vs Euro")
    plt.plot(meses, euro, "mD:") #"mD:" Diamantes color magenta unidos por dos puntos :

    # Salva la gráfica con el nombre de Graficos.png
    plt.savefig("Graficos.png")

    # Muestra la gráfica
    plt.show()
    
def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Tipos de cambio en un gráfico")
    print("3. Tipos de cambio en dos gráficos")
    print("4. Salir")
    
def main():
    continua = True
    pesos = [70, 69.5, 71, 69, 70, 68.5, 68]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"]
    dolar = [20.45, 20.32, 19.94, 20.13, 19.49, 18.95, 18.81, 18.75, 18.36]
    euro =  [21.06, 21.32, 21.69, 22.73, 21.81, 21.87, 21.83, 21.95, 21.60]
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:      
            estadistica_descriptiva(pesos)
        elif opcion == 2:
            tipos_cambio(meses, dolar, euro)
        elif opcion == 3:
            tipos_cambio2(meses, dolar, euro)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()


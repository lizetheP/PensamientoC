import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

# -------------------------------------------------------------------
# --------- Estadística descriptiva ---------------------------------
# -------------------------------------------------------------------

def estadistica_descriptiva(moneda):
    print(moneda)
    maximo = np.max(moneda)
    minimo = np.min(moneda)
    promedio = statistics.mean(moneda)
    mediana = statistics.median(moneda)
    moda = statistics.mode(moneda)
    desviacion = statistics.stdev(moneda)
    print("Máximo = %.2f" % maximo)
    print("Mínimo = %.2f" % minimo)
    print("Promedio = %.2f" % promedio)
    print("Mediana = %.2f" % mediana)
    print("Moda = %.2f" % moda)
    print("Desviación estándar = %.2f" % desviacion)
    
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
    plt.xticks(rotation = 45)


    #divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
    plt.subplot(122)
    plt.xlabel("Meses")
    plt.ylabel("Euro")
    plt.title("Peso vs Euro")
    plt.plot(meses, euro, "mD:") #"mD:" Diamantes color magenta unidos por dos puntos :
    plt.xticks(rotation = 45)

    plt.show()
    # Salva la gráfica con el nombre de Graficos.png
 #   plt.savefig("Graficos.png")

    
def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Tipos de cambio en un gráfico")
    print("3. Tipos de cambio en dos gráficos")
    print("4. Salir")
    
def main():
    continua = True
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", ]
    dolar = [17.15, 17.08, 17.22, 17.10, 17.05, 16.98, 16.92, 17.02]
    euro =  [20.09, 20.18, 19.90, 20.04, 19.91, 19.51, 19.30, 19.70]
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            print("\nDOLAR")
            estadistica_descriptiva(dolar)
            print("\nEURO")
            estadistica_descriptiva(euro)
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


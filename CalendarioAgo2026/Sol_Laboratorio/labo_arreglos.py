import numpy as np

def estadisticas (consumo):
    maximo = np.max(consumo)
    minimo = np.min(consumo)
    promedio = np.mean(consumo)
    mediana = np.median(consumo)
    varianza = np.var(consumo)
    desviacion = np.std(consumo)
    print("Máximo = %.2f" % maximo)
    print("Mínimo = %.2f" % minimo)
    print("Promedio = %.2f" % promedio)
    print("Mediana = %.2f" % mediana)
    print("Varianza = %.2f" % varianza)
    print("Desviación estándar = %.2f" % desviacion)
    
def operaciones1():
    print("\nOPERACIONES CON ARREGLOS")
    
    print("\nEJERCICIO 1")
    voltaje = np.array([12.0, 11.8, 12.2, 11.9, 12.1]) 
    corriente = np.array([1.5, 1.8, 1.4, 2.0, 1.6])
    potencia = voltaje * corriente
    print("POTENCIA: ", potencia)
    
    print("\nEJERCICIO 2")
    inicial = np.array([120, 85, 200, 60, 150, 95]) 
    vendidas = np.array([45, 70, 110, 58, 90, 40])
    inventario = inicial - vendidas
    print("INVENTARIO: ", inventario)

    print("\nEJERCICIO 3")
    distancias = np.array([150, 320, 210, 400]) 
    tiempos = np.array([12, 25, 15, 32]) 
    velocidades = distancias / tiempos
    print("VELOCIDADES: ", velocidades)
    
    print("\nEJERCICIO 4")
    tiempos = np.array([3.4, 3.1, 3.5, 3.2]) 
    otros = np.array([2.9, 3.3]) 
    tiemposf = np.append(tiempos, otros)
    print("TIEMPOS FINALES: ", tiemposf)

def operaciones2():
    print("\nOPERACIONES ENTRE UN ARREGLO Y UN ESCALAR")
    print("\nEJERCICIO 1")
    salarios = np.array([18000, 21500, 19200, 24000, 20500])
    salarios_aumento = salarios * 1.08
    print("SALARIOS CON AUMENTO: ", salarios_aumento)
    
    print("\nEJERCICIO 2")
    celsius = np.array([20.0, 25.5, 30.0, 15.2, 18.8])
    fahrenheit = celsius / 1.8 + 32
    print("FAHRENHEIT: ", fahrenheit)
    
def menu():
    print()
    print("1. Estadísticas")
    print("2. Operaciones1")
    print("3. Operaciones2")
    print("4. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            consumo = np.array([120, 135, 128, 142, 150, 95, 88])
            estadisticas(consumo)
        elif opcion == 2:
            operaciones1()
        elif opcion == 3:
            operaciones2()
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()


    

def dolares_a_pesos(dolares):
    return dolares*19.41

def costo_hotel(noches):
    return noches * 185

def costo_avion(pasajeros):
    return pasajeros * 410

def costo_viaje(noches, pasajeros):
    hotel = costo_hotel(noches)
    avion = costo_avion(pasajeros)
    totalDolares = hotel + avion
    totalPesos = dolares_a_pesos(totalDolares)
    return totalPesos

# pide opción y dependiendo de la opción llama una función diferente
opcion = int(input())     
if (opcion == 1):
    dolares  = float(input())
    print(dolares_a_pesos(dolares))
elif (opcion == 2):
    noches  = int(input())
    print(costo_hotel(noches))
elif (opcion == 3):
    pasajeros  = int(input())
    print(costo_avion(pasajeros))
elif (opcion == 4):
    noches  = int(input())
    pasajeros  = int(input())
    print(costo_viaje(noches,pasajeros))

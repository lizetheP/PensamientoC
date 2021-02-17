def kilometrosMillas(km):
    return km/1.6

def millasKilometros(millas):
    return millas*1.6

def unidadesLongitud():
    print("1.KilometrosMillas")
    print("2.MillasKilometros")
    print("3.Salir")
    
def main():
    #unidadesLongitud()
    opcion = int(input())
    if opcion == 1:
        km = float(input())
        millas = kilometrosMillas(km)
        print("%.2f" % millas)
    elif opcion == 2:
        millas = float(input())
        km = millasKilometros(millas)
        print("%.2f" % km)
    elif opcion == 3:
        print("Adios")
    else:
        print("ERROR OPCION INVALIDA")
        
main()     

def kilometros_millas(km):
    return km/1.6

def millas_kilometros(millas):
    return millas*1.6

def unidades_longitud():
    print("1.Kilometros a millas")
    print("2.Millas a kilometros")
    print("3.Salir")
    
def main():
    unidadesLongitud()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        km = float(input("Introduce los kilometros: "))
        millas = kilometrosMillas(km)
        print("%.2f kilometros equivalen a %.2f millas" % (km, millas))
    elif opcion == 2:
        millas = float(input("Introduce las millas: "))
        km = millasKilometros(millas)
        print("%.2f millas equivalen a %.2f kilometros" % (millas, km))
    elif opcion == 3:
        print("Adios")
    else:
        print("ERROR OPCION INVALIDA")
        
main()     

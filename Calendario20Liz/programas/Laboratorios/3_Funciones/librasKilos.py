def librasKilos(libras):
    return libras/2.2
    
def millasKilometros(millas):
    return millas*1.60934

def goingToMexico(millas, libras):
    kilometros = millasKilometros(millas)
    kilos = librasKilos(libras)
    return kilometros, kilos

m = float(input("Introduce las millas: "))
l = float(input("Introduce las libras: "))
kilometros, kilos = goingToMexico(m, l)
print("%.2f millas equivalen a %.2f kilómetros"%(m,kilometros))
print("%.2f libras equivalen a %.2f kilos"%(l,kilos))

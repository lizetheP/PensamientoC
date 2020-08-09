def millasKilometros(millas):
    return millas*1.60934

m = float(input("Introduce las millas: "))
k = millasKilometros(m)
print("%.2f millas equivalen a %.2f kilometros"%(m, k)) 
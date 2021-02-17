def metros_Pies(metros):
    return metros / 0.3048

def pies_metros(pies):
    return pies * 0.3048

p = float(input("Introduce los pies: "))
m = pies_metros(p)
print("%.2f pies equivalen a %.2f metros"%(p, m))
"""
m = float(input("Introduce los metros: "))
p = metros_Pies(m)
print("%.2f metros equivalen a %.2f pies"%(m, p))
"""
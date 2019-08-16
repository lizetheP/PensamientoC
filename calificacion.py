# Convierte un precio en pesos a dólares
"""
1. Pedir p1, p2, pf y ef
2. cf = p1*.2 + p2*.35 + pf*.15 + ef*.3
3. Escribir (cf)"""

p1 = int(input("Introduce el parcial 1: "))
p2 = int(input("Introduce el parcial 2: "))
pf = int(input("Introduce el proyecto final: "))
ef = int(input("Introduce examen final: "))
cf = p1*.2 + p2*.35 + pf*.15 + ef*.3
print("La calificacion final es: ", cf)          
            
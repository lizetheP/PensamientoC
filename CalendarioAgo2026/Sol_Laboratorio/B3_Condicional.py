
"""
Algoritmo: Huracán
1. Pedir la velocidad v
2. Si v >= 74 y v <= 95
      Escribir("Categoria 1 y daños mínimos")
   sino si v >= 96 y v <= 110
      Escribir("Categoria 2 y daños moderados")
   sino si v >= 111 y v <= 130
      Escribir("Categoria 3 y daños extensos")
   sino si v >= 131 y v <= 155
      Escribir("Categoria 4 y daños extremos")
   sino si v > 155
      Escribir("Categoria 5 y daños catastróficos")
   sino
      Escribir("No es huracán")
"""
v = int(input("Dame la velocidad: "))
if v >= 74 and v <= 95:
    print("Categoria 1 y daños mínimos")
elif v >= 96 and v <= 110:
    print("Categoria 2 y daños moderados")
elif v >= 111 and v <= 130:
    print("Categoria 3 y daños extensos")
elif v >= 131 and v <= 155:
    print("Categoria 4 y daños extremos")
elif v > 155:
    print("Categoria 5 y daños catastróficos")
else:
    print("No es huracán")
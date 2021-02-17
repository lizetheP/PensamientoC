#Temperatura
"""
1. Pedir temperatura (t)
2. Si t >= 100
      escribir("Vapor")
   SiNo
     Si t>= 30 y t<100
        escribir("Caliente")
     SiNo
       Si t>=0 y t<30
          escribir("Fría")
       SiNo
          Si (t>=-273 y t<0)
             escribir("congelada")
          SiNo
             Si (t < -273)
                escribir("Temperatura inexistente")"""
                
v = int(input("Introduce la velocidad: "))
if v >= 74 and v <= 95:
    print("Categoria 1 y daños mínimos")
elif v >= 96 and v<= 110:
    print("Categoria 2 y daños moderados")
elif v >= 111 and v <= 130:
    print("Categoria 3 y daños extensos")
elif v >= 131 and v <= 155:
    print("Categoría 4 y110 daños extremos")
elif v > 155:
    print("Categoría 5 y daños catastróficos")    
else:
    print("No es huracán")
    
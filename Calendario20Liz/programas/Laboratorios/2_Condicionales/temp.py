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
                
t = int(input("Introduce la temperatura: "))
if t >= 100:
    print("Vapor")
elif t>=30 and t<100:
    print("Caliente")
elif t>=0 and t<30:
    print("Fría")
elif t>=-273 and t<0:
    print("congelada")
elif t < -273:                         else:
    print("Temperatura inexistente")       print("Temperatura inexistente") 

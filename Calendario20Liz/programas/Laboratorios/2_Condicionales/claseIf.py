#Calcula el valor de la resistencia

v = float(input("Introduce el valor del voltaje: "))
r = float(input("Introduce el valor de la resistencia: "))
if r > 0:
   i = v / r
   print("La corriente es: %.3f" % i)
elif r == 0:
    print("Error la resistencia es cero")
else:
    print("Error resistencia negativa")

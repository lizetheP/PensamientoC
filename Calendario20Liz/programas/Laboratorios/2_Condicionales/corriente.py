"""Calcula la corriente de un circuito conociendo el voltaje y la resistencia,
suponga que el valor de  la resistencia no puede ser negativa ni cero.
I = V / R
Donde I es la corriente, V el voltaje y R la resistencia. """

"""1. Pedir el voltaje (v)
2. Pedir la resistencia (r)
3. Si r > 0
      i = v / r
      escribir(i)
   SiNo
     Si r < 0
        escribir("La resistencia no puede ser negativa")
     SiNo
        escribir("La resistencia no puede ser cero")"""

v = float(input("Introduce el voltaje: "))
r = float(input("Introduce la resistencia: "))
if r > 0:
    i = v / r
    print("La corriente es: ", i)
elif r < 0:
    print("La resistencia no puede ser negativa")
else:
    print("La resistencia no puede ser cero")
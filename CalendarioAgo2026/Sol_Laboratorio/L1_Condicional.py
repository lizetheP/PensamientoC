"""
Algoritmo: Calificación
1. Pedir c
2. si c == 100
      Escribir("Excelente")
   sino si c >= 90 y c < 100
      Escribir("Muy bien")
   sino si c >= 80 y c < 90
      Escribir("Bien")
   sino si c >= 70 y c < 80
      Escribir("Regular")
   sino si c >= 0 y c < 70
      Escribir("Deficiente")
   sino
      Escribir("ERROR calificación inválida")
"""
c = int(input("Dame la calificación: "))
if c == 100:
    print("Excelente")
elif c >= 90 and c < 100:
    print("Muy bien")
elif c >= 80 and c < 90:
    print("Bien")
elif c >= 70 and c < 80:
    print("Regular")
elif c >= 0 and c < 70:
    print("Deficiente")
else:
    print("ERROR calificación inválida")
    


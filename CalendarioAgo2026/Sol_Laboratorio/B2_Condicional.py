
"""
Algoritmo: Saldo en inversión
1. Pedir el saldo
2. Si saldo > 1000000
      Escribir("Excelente cliente")
   sino si saldo > 100000 y saldo <= 1000000
      Escribir("Buen cliente")
   sino si saldo > 2000 y saldo <= 100000
      Escribir("Cliente promedio")
   sino si saldo >= 0 y saldo <= 2000:
      Escribir("Cliente con saldo insuficiente")
   sino:
      Escribir("¿Y tu dinero?")
"""
saldo = int(input("Introduce el saldo: "))
if saldo > 1000000:
    print("Excelente cliente")
elif saldo > 100000 and saldo <=1000000:
    print("Buen cliente")
elif saldo > 2000 and saldo <= 100000:
    print("Cliente promedio")
elif saldo >= 0 and saldo <= 2000:
    print("Cliente con saldo insuficiente")
else:
    print("¿Y tu dinero?")
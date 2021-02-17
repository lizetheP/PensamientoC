cantidad = int(input("Introduce una cantidad: "))
b200 = cantidad // 200
residuo = cantidad % 200
b50 = residuo // 50
residuo = residuo % 50
b20 = residuo // 20
b1 = residuo % 20
print("Billetes $200 :", b200)
print("Billetes $50 :", b50)
print("Billetes $20 :", b20)
print("Billetes $1 :", b1)

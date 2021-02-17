tiempo = int(input())
horas = tiempo // 3600
print(horas)
residuo = tiempo % 3600
#print("Residuo :", residuo)
minutos = residuo // 60
print(minutos)
segundos = residuo % 60
print(segundos)


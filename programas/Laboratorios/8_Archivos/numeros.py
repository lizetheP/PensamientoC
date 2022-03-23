import random

file = open ("numeros.txt", "r")
file.seek(0)
num = random.randint(1, 6)
print(num)
cont = 1
linea = file.readline()
while linea != "":
    if num == cont:
        numero = list(linea)
        print(numero)
        numero.pop()
        print(numero)
    linea = file.readline()
    cont = cont + 1
file.close()

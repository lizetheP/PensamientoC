def todosPositivos(x, y, z):
    if (x > 0 and  y > 0  and  z > 0):
        return 1
    else:
        return 0

n1 = int(input("Introduce el valor de x: "))
n2 = int(input("Introduce el valor de y: "))
n3 = int(input("Introduce el valor de z: "))
res = todosPositivos (n1, n2, n3)
if (res == 1):
    print("Los 3 valores son positivos")
else:
    print("No todos son positivos")
    
def decrementa(LS, LI, DEC):
    for i in range(LS, LI-1, -DEC):
        print(i)

sup = int(input("Introduce el límite superior: "))
inf = int(input("Introduce el límite inferior: "))
d = int(input("Introduce el decremento: "))
decrementa(sup, inf, d)
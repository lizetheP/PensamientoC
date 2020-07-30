def f1 (n):
    acumulador=0
    contador=1
    while contador <= n: 
        acumulador=acumulador + contador
        contador = contador + 1
    return acumulador


num = int(input("Dame un numero entero: "))
if num >= 1:
    res = f1(num)
    print("f1(%d) = %d" % (num, res))
else:
    print("NUMERO INVALIDO")


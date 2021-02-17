import math

def sumatoria (N):
    acum=0
    i = 1
    while (i <= N):  
        acum=acum + (i*i-3*i) / (math.sqrt (5*i)) 
        i = i + 1
    return acum

def main():
    num = int(input("Dame un numero entero: "))
    if num >= 1:
        res = sumatoria(num)
        print("sumatoria(%i) = %.4f" % (num, res))
    else:
        print("Número inválido")

main()


import math

def funcionG(n):
    acum = 0
    for i in range(5,n+1):
        acum = acum + math.sqrt(2*i -1)/(i**2)
    return acum

def main():
    num = int(input("Introduce un número: "))
    res = funcionG(num)
    print("El resultado es: %.2f" % res)
    
main()
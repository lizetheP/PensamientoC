def potencia(x, n):
    acum = 1
    i = 1
    while i <= n:
        acum = acum * x
        i = i + 1
    return acum
        
def main():
    x = int(input("Introduce un número: "))
    n = int(input("Introduce la potencia: "))
    res = potencia(x, n)
    print("El resultado es", res)
    
main()
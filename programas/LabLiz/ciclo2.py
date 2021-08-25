def potencia(x, n):
    cont = 1
    acum = 1
    while cont <= n:
        acum = acum * x
        cont = cont + 1
    return acum

def main():
    x = int(input("Dame x: "))
    n = int(input("Dame n: "))
    res = potencia(x, n)
    print("El resultado es: ", res)
    
main()


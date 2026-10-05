def suma_positivos(cantidad):
    num = 1
    acum = 0
    while num <= cantidad:
        valor = int(input("Dame un número: "))
        if valor > 0:
            acum = acum + valor
        num = num + 1
    return acum

def main():
    c = int(input("Dame la cantidad de números a sumar: "))
    res = suma_positivos(c)
    print("La suma es:", res)
        
main()


    
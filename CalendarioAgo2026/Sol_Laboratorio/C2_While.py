def suma():
    acum = 0
    valor = int(input("Dame un número: "))
    while valor != 0:
        acum = acum + valor
        valor = int(input("Dame un número: "))
    return acum

def main():
    res = suma()
    print("La suma es:", res)
        
main()


    
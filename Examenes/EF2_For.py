def multiplica_pares(n):
    acum = 1
    num = 2
    for i in range(n):
        acum = acum * num
        num = num + 2
    return acum
        
def main():
    n = int(input("Introduce n: "))
    res = multiplica_pares(n)
    print("Resultado:", res)
    
main()
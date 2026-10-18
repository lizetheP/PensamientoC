import math

def es_primo(n):
    if n <= 1:
        return False
    # Comprueba si algún número entre 2 y la raíz de n lo divide exactamente
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def imprime_20_primos():
    cont = 1
    num = 1
    while cont <= 20:
        res = es_primo(num)
        if res == True:
            print(num)
            cont = cont + 1
        num = num + 1      

def main():
    imprime_20_primos()

main()
    
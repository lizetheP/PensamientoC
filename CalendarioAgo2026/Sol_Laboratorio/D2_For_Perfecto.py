import math
def es_perfecto(n):
    if n <= 1:
        return False
    suma = 0
    # Suma todos los números entre 1 y n-1 que dividen exactamente a n
    for i in range(1, n):
        if n % i == 0:
            suma = suma + i
    if suma == n:
        return True
    else:
        return False

def imprime_4_perfectos():
    cont = 1
    num = 1
    while cont <= 4:
        res = es_perfecto(num)
        if res == True:
            print(num)
            cont = cont + 1
        num = num + 1      

def main():
    imprime_4_perfectos()

main()
    
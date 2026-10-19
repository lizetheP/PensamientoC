import math

def es_primo(n):
    # Comprueba si algún número entre 2 y la raíz de n lo divide exactamente
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def imprime_20_primos():
    cont = 1
    num = 2
    while cont <= 20:
        res = es_primo(num)
        if res == True:
            print(num)
            cont = cont + 1
        num = num + 1      

def es_perfecto(n):
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
    num = 2
    while cont <= 4:
        res = es_perfecto(num)
        if res == True:
            print(num)
            cont = cont + 1
        num = num + 1      

def menu():
    print("1. Imprime 20 primos")
    print("2. Imprime 4 perfectos")
    print("3. Salir")
    
def main():
    continua = True
    while continua == True:
        print() # Imprime un salto de línea
        menu()
        opcion = int (input("Introduce una opción: "))
        if opcion == 1:
            imprime_20_primos()
        elif opcion == 2:
            imprime_4_perfectos()
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()  

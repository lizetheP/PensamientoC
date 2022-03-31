import random
import math

def aleatorios1():
    for i in range (50):
        num = random.randint(0, 70)
        print("%i.  %i" % (i, num))
        
def aleatorios2():
    for i in range (30):
        num = random.randint(30, 80)
        print("%i. %i" % (i, num))
        
def aleatorios3():
    for i in range (20):
        num = random.randint(-15, 40)
        print("%i. %i" % (i, num))

def g(n):
    acum = 0
    for i in range (5, n+1):
        acum = acum + math.sqrt(2*i - 1) / i**2
    return acum

def imprimeN_cada_vez(n) :
    letra = 's'
    num = 1
    while letra == 's' or letra == 'S':
        for i in range(n):
            print(num, end=" ")
            num = num + 1
        letra = str(input("Deseas continuar: "))
def fibonacci(n): # Despliega la serie de Fibonacci con n iteraciones
    num_ant = 0
    num_act = 1
    resultado = 0
    print(num_ant)
    print(num_act)
    for i in range(1, n):
        resultado = num_act + num_ant
        print(resultado)
        num_ant = num_act
        num_act = resultado
def fibonacci2(n):
    F1 = 0
    F2 = 1
    for i in range(n):
        print(F2)
        FN = F1 +F2
        F1 = F2
        F2 = FN
        
def fibonacci(n):
    f1 = 1
    f2 = 1
    print(f1)
    print(f2)
    for i in range(2, n):
        f3 = f1 + f2
        print(f3)
        f1 = f2
        f2 = f3
        
def menu():
    print()
    print("1. Aleatorios 1")
    print("2. Aleatorios 2")
    print("3. Aleatorios 3")
    print("4. Función G")
    print("5. Imprime N cada Vez")
    print("6. Fibonacci")
    print("7. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            aleatorios1()
        elif opcion == 2:
            aleatorios2()
        elif opcion == 3:
            aleatorios3()
        elif opcion == 4:
            n = int(input("Introducir n mayor o igual a 5: "))
            if n >= 5:
                res = g(n)
                print("g(%i) = %.2f" % (n, res))
            else:
                print("ERROR EL NÚMERO TIENE QUE SER MAYOR O IGUAL A 5")
        elif opcion == 5:
            n = int(input("Introducir n mayor o igual a 1: "))
            if n >= 1:
                imprimeN_cada_vez (n)
            else:
                print("ERROR EL NÚMERO TIENE QUE SER MAYOR O IGUAL A 1")
        elif opcion == 6:
            n = int(input("Introducir n mayor o igual a 2: "))
            if n >= 2:
                fibonacci(n)
            else:
                print("ERROR EL NÚMERO TIENE QUE SER MAYOR O IGUAL A 2")
        elif opcion == 7:
            print("Adiós")
            continua = False
        else:
            print("OPCIÓN INVÁLIDA")

main()



# RODOLFO
# RODRIGO
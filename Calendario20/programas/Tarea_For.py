import random
import math

def factorial(n):
    acum = 1
    for i in range(1,n+1):
        acum = acum * i
        if (i == n):
            print(str(i), end=' = ')
            print(str(acum), end=' ')
        else:
            print(str(i), end=' x ')
            
def factorial(n):
    acum = 1
    for i in range(1,n+1):
        acum = acum * i
        if (i == n):
            print(str(i), end=' = ')
            print(str(acum), end=' ')
        else:
            print(str(i), end=' x ')            

def numeros(n): 
    num = int(input("Introduce un número: "))
    print(num)
    menor = num
    mayor = num
    for x in range(1,n):
      num = int(input("Introduce un número: "))
      print(num)
      if (num < menor):
         menor = num
      elif (num > mayor):
          mayor = num
    print("El valor mayor es: ", str(mayor))
    print("El valor menor es: ", str(menor))

def muestraNumeros(n):
    for x in range(1,n):
        print(str(x), end=', ')
    for x in range(n,0,-1):
        if x == 1:
            print(str(x))
        else:
            print(str(x), end=', ')    

def f4(n):
    acum = 0
    for i in range(1,n+1):
        acum = acum + math.pow(3, i)/i
    return acum

def incremento(li, ls, inc):
    for i in range(li,ls+1,inc):
        print(str(i),end=' ')

def imprimeNcadaVez(n):
    x = 1
    opcion = 's'
    while (opcion == 's' or opcion == 'S'):
        for i in range(1, n+1):
            print(str(x), end=' ')
            x= x+1
        opcion = str(input("Deseas continuar: s / n "))
        
def menu():
    print("\n\nMENU")
    print("1. Factorial")
    print("2. Numeros")
    print("3. Muestra numeros")
    print("4. Funcion F4")
    print("5. Incremento")
    print("6. Imprime N cada vez")
    print("7. Salir")
    
continuar = True
while continuar:
    menu()
    opcion =  int(input("Introduce una opcion: "))
    if opcion == 1:
        num = int(input("Introduce un número positivo: "))
        factorial(num)
    elif opcion == 2:
        num = int(input("Introduce un número positivo: "))
        numeros(num)
    elif opcion == 3:
        num = int(input("Introduce un número positivo: "))
        muestraNumeros(num)
    elif opcion == 4:
        num = int(input("Introduce un número positivo: "))
        res = f4(num)
        print("F4(", str(num), ") =", str(res))
    elif opcion == 5:
        li = int(input("Introduce el límite inferior: "))
        ls = int(input("Introduce el límite superior: "))
        inc = int(input("Introduce el incremento: "))
        if (li <= ls):
            incremento(li, ls, inc)
        else:
            print("ERROR el límite inferior debe ser menor que el límite superior")
    elif opcion == 6:
        num = int(input("Introduce un número positivo: "))
        imprimeNcadaVez(num)
    elif opcion == 7:
        print("Adios")
        continuar = False
    else:
        print("Opción inválida")
        continuar = False    
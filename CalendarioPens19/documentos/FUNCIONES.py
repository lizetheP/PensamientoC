"""funcion division(num, den)
    cont = 0
    mientras (num >= den)
        num = num - den
        cont = cont + 1
    regresar cont, num"""

def division(num, den):
    cont = 0
    while num >= den:
        num = num - den
        cont = cont + 1
    return cont, num

"""funcion inversoNumero(num)
    inverso = 0
    mientras num > 0
        num = num/10
        res = num%10
        inverso = inverso*10 + res
    regresar inverso"""

def inversoNumero(num):
    inverso = 0
    while num != 0:
        res = num%10
        num = num//10
        inverso = inverso*10 + res
    return inverso

"""funcion fibonacci(n)
    a=1
    b=1
    cont=2
    escribir(a)
    escribir(b)
    mientras (cont < n-2)
        c = a+b
        escribir(c)
        a = b
        b = c
        cont = cont +1"""

def fibonacci(n):
    i=2
    a = 1
    b = 1
    c = 0
    print(a)
    print(b)
    while i < n:
        c = a + b
        print(c)
        a = b
        b = c
        i = i + 1

def menu():
    print("\n1. Division")
    print("2. Inverso")
    print("3. Fibonacci")

while True:
    menu()
    opcion = int (input("Introduce una opcion: "))
    if opcion == 1:
        n = int(input("Introduce el numerador: "))
        d = int(input("Introduce el denominador: "))
        if d != 0:
            cociente, residuo = division(n,d)
            print("El cociente es: %d y el residuo es: %d" % (cociente, residuo))
        else:
            print("El denominador no puede ser cero")
    elif opcion == 2:
        n = int(input("Introduce un número entero: "))
        res = inversoNumero(n)
        print("El inverso es: ", res)
    elif opcion == 3:
        n = int(input("Introduce un número entero: "))
        if n>=2:
            fibonacci(n)
        else:
            print("Número inválido")
    else:
        print("ERROR OPCION INVALIDA")
        break


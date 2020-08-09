def elevaPotencia(num, potencia):
    cont = 1
    acum = 1
    if potencia >= 0:
        while cont <= potencia:
            acum = acum*num
            cont = cont + 1
    else:
        potencia = potencia*-1
        while cont <= potencia:
            acum = acum/num
            cont = cont + 1       
    return acum

def aproximacionPI(num):
    cont = 1
    acum = 0
    signo = 1
    while cont <= num:
        acum = acum+1/cont*signo
        cont = cont + 2
        signo = signo*-1
    return 4*acum

def menu():
    print("\n1. Potencia")
    print("2. Aproximación de PI")
    print("3. Pikachu")

def dateSimPikachu():
    word = str(input("Introduce una palabra: "))
    while word != "pikachu":
        if word == "pikapika":
            print("chu")
        elif word == "pika!":
            print("pika")
        else:
            print("???")
        word = str(input("Introduce una palabra: "))
    print("pikachu!!!")
    
while True:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        n = int(input("Introduce un número a elevar: "))
        x = int(input("Introduce la potencia: "))
        res = elevaPotencia(n, x)
        print("El resultado es: %.4f" % res)
    elif opcion == 2:
        n = int(input("Introduce un número: "))
        res = aproximacionPI(n)
        print("El resultado es: %.4f" % res)    
    elif opcion == 3:
        dateSimPikachu()
    else:
        print("Opción inválida")
        break


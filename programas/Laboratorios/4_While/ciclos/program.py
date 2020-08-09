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
    word = str(input())
    while word != "pikachu":
        if word == "pikapika":
            print("chu")
        elif word == "pika!":
            print("pika")
        else:
            print("???")
        word = str(input())
    print("pikachu!!!")
    
opcion = int(input())
if opcion == 1:
    n = int(input())
    x = int(input())
    res = elevaPotencia(n, x)
    print("%.4f" % res)
elif opcion == 2:
    n = int(input())
    res = aproximacionPI(n)
    print("%.4f" % res)    
elif opcion == 3:
    dateSimPikachu()
else:
    print("Opción inválida")

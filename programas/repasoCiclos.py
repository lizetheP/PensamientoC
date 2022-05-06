def cuenta_suma():
    acum = 0
    cont = 0
    while acum < 1000:
        num = int(input("Introduce un número: "))
        acum = acum + num
        cont = cont + 1
    print("suma = ", acum)
    print("cantidad de números: ", cont)

def muestra_numeros(n):
    for i in range(1, n):
        print(i, end=" ")
    for i in range(n, 0, -1):
        print(i, end=" ")
                   
def main():
    num = int(input("Introduce un número: "))
    muestra_numeros(num)
    #cuenta_suma()
    
main()
    
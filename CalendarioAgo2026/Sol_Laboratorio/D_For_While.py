def factores_de(x):
    for i in range(1, x):
        if x % i == 0:
            print(i)

def pares(x):
    for i in range(1, x+1):
        if i % 2 == 0:
            print(i)
            
def menu():
    print("MENU")
    print("1. Factores de")
    print("2. Pares")
    print("3. Salir")
    
def main():
    continua = True
    while continua == True:
        print() # Imprime un salto de línea
        menu()
        opcion = int (input("Introduce una opción: "))
        if opcion == 1:
            n = int(input("Dame un número entero positivo: "))
            if n > 0:
                factores_de(n)
            else:
                print("El número debe ser positivo")
        elif opcion == 2:
            n = int(input("Dame un número entero positivo: "))
            if n > 0:
                pares(n)
            else:
                print("El número debe ser positivo")
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()
def suma_positivos(cantidad):
    num = 1
    acum = 0
    while num <= cantidad:
        valor = int(input("Dame un número: "))
        if valor > 0:
            acum = acum + valor
        num = num + 1
    return acum

def suma():
    acum = 0
    valor = int(input("Dame un número: "))
    while valor != 0:
        acum = acum + valor
        valor = int(input("Dame un número: "))
    return acum

def menu():
    print("1. Suma positivos")
    print("2. Suma")
    print("3. Salir")
    
def main():
    menu()
    opcion = int(input("Dame una opción: "))
    if opcion == 1:
        c = int(input("Dame la cantidad de números a sumar: "))
        res = suma_positivos(c)
        print("La suma es:", res)
    elif opcion == 2:
        res = suma()
        print("La suma es:", res)
    elif opcion == 3:
        print("Adiós")
    else:
        print("Error opción inválida")
        
main()


    
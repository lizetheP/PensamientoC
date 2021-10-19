def multiplicacion(a, b):
    acum = 0
    i = 1
    while i <= b:
        acum = acum + a
        i = i + 1
    return acum
        
def main():
    a = int(input("Introduce num1: "))
    b = int(input("Introduce num2: "))
    res = multiplicacion(a, b)
    print("El resultado es", res)
    
main()
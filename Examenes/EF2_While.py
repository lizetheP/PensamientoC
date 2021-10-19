def suma(a, b):
    acum = 0
    while a <= b:
        acum = acum + a
        a = a + 1
    return acum
        
def main():
    a = int(input("Introduce a: "))
    b = int(input("Introduce b: "))
    res = suma(a, b)
    print("La suma es", res)
    
main()
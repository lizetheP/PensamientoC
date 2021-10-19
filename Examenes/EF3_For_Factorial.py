def factorial(num):
    acum = 1
    for i in range(1, num+1):
        acum = acum * i
    return acum
        
def main():
    a = int(input("Introduce num: "))
    res = factorial(a)
    print("El resultado es", res)
    
main()
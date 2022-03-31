def fibonacci(n):
    i=2
    a=1
    b=1
    c=0
    print(a)
    print(b)
    while i<n:
        c=a+b 
        print(c)
        a=b
        b=c
        i=i+1

def fibonacci2(n):
    a=1
    b=1
    print(a)
    print(b)
    for i in range (2, n):
        c=a+b 
        print(c)
        a=b
        b=c
        
        
num = int(input("Introduce un número entero mayor o igual a 2: "))
if num >= 2:
    fibonacci2(num)
else:
    print("ERROR EL NÚMERO DEBE SER MAYOR O IGUAL A 2")

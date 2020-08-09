def fibonacci(n):
    i=0
    a=1
    b=1
    c=0
    print(a)
    print(b)
    while i<n-2:
        c=a+b 
        print(c)
        a=b
        b=c
        i=i+1

num = int(input("Introduce un número entero mayor o igual a 2: "))
if num >= 2:
    fibonacci(num)
else:
    print("ERROR EL NÚMERO DEBE SER MAYOR O IGUAL A 2")

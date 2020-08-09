def inverso(n):
    invertido = 0
    while n != 0:
        resto = n%10 #Guarda el resto de la división del numero y 10,para asi guardar cada dígito
        n = n//10  #isminuye el numero para asi poder utilizar el digito siguiente
        invertido = invertido*10 + resto
    return invertido

num = int(input("Introduce un número entero: "))
res = inverso(num)
print("El número invertido es: ", res)

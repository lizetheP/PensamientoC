"""1.  Pedir longitud lado 1 (lado1)
2.  Pedir longitud lado 2 (lado2)
3.  Pedir longitud lado 3 (lado3)
4.  Si (lado1 = lado2 y lado2 = lado3)
        Escribir(“Es un triángulo equilátero”)
    SiNo
        Si (lado1 = lado2 y lado1 != lado3) o (lado1 = lado3 y lado1 != lado2)
            Escribir(“Es un triángulo isósceles”)
        SiNo
            Si (lado1 != lado2 y lado2 != lado3)
                Escribir(“Es un triángulo escaleno”)"""

lado1 = int(input("Introduce longitud lado 1: "))
lado2 = int(input("Introduce longitud lado 2: "))
lado3 = int(input("Introduce longitud lado 3: "))
if (lado1 == lado2) & (lado2 == lado3):
    print("EQUILATERO")
elif (lado1 == lado2 & lado1 != lado3) | (lado1 == lado3 & lado1 != lado2):
    print("ISOSCELES")
elif lado1 != lado2 & lado2 != lado3:
    print("ESCALENO")







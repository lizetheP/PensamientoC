"""Dadas tres cantidades enteras positivas, que representan la longitud de los lados de un triángulo, se quiere determinar las siguientes situaciones: 
¿Es un triángulo equilátero? Si los tres lados son de igual longitud.
¿Es un triángulo isósceles? Si dos de los tres lados son de igual longitud y uno de distinta longitud.
¿Es un triángulo escaleno? Si los tres lados son de distinta longitud.

1. Pedir lado1
2. Pedir lado2
3. Pedir lado3
4. Si lado1 es igual a lado2 y lado2 es igual a lado3
      escribir("EQUILATERO")
   SiNo
      Si (lado1 es igual a lado2) o (lado1 es igual al lado3) o (lado2 es igual al lado3)
         escribir("ISOSCELES")
      SiNo
        Si lado1 es diferente de lado2 y lado2 es diferente de lado3
           escribir("ESCALENO")"""

lado1 = int(input("Introduce el lado1: "))
lado2 = int(input("Introduce el lado2: "))
lado3 = int(input("Introduce el lado3: "))
if lado1 == lado2 and lado2 == lado3:
    print("EQUILATERO")
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("ISOSCELES")
elif lado1 != lado2 and lado2 != lado3:
    print("ESCALENO")
     
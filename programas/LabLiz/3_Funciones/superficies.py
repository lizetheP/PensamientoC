import math
def sector(radio, angulo):
    return (math.pi*radio*radio*angulo) / 360

def eclipse(a, b):
    return math.pi*a*b

def paralelogramo(a, h):
    return a*h

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main():
    superficies()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        radio = float(input("Introduce el radio: "))
        angulo = float(input("Introduce el angulo: "))
        res = sector(radio, angulo)
        print("La superficie del sector es: %.2f" % res)
    elif opcion == 2:
        a = float(input("Introduce el radio a: "))
        b = float(input("Introduce el radio b: "))
        res = eclipse(a, b)
        print("La superficie de la eclipse es: %.2f" % res)
    elif opcion == 3:
        a = float(input("Introduce el lado a: "))
        h = float(input("Introduce la altura: "))
        res = paralelogramo(a, h)
        print("La superficie del paralelogramo es: %.2f" % res)
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()      
import math

def arco(radio, angulo):
    return (2*math.pi*radio*angulo) / 360

def poligono(l, a):
    return (6*l*a)/2

def triangulo(b, h):
    return (b*h)/2

def figuras():
    print("1. Arco")
    print("2. Poligono")
    print("3. Triangulo")
    print("4. Salir")

def main():
    figuras()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        radio = float(input("Introduce el radio: "))
        angulo = float(input("Introduce el angulo: "))
        res = arco(radio, angulo)
        print("Arco: %.2f" % res)
    elif opcion == 2:
        l = float(input("Introduce el lado: "))
        a = float(input("Introduce el radio: "))
        res = poligono(l, a)
        print("Poligono: %.2f" % res)
    elif opcion == 3:
        b = float(input("Introduce la base: "))
        h = float(input("Introduce la altura: "))
        res = triangulo(b, h)
        print("Triangulo: %.2f" % res)
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()
     
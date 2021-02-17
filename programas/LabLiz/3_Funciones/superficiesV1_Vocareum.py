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
    #figuras()
    opcion = int(input())
    if opcion == 1:
        radio = float(input())
        angulo = float(input())
        res = arco(radio, angulo)
        print("%.2f" % res)
    elif opcion == 2:
        l = float(input())
        a = float(input())
        res = poligono(l, a)
        print("%.2f" % res)
    elif opcion == 3:
        b = float(input())
        h = float(input())
        res = triangulo(b, h)
        print("%.2f" % res)
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()
     
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
    #superficies()
    opcion = int(input())
    if opcion == 1:
        radio = float(input())
        angulo = float(input())
        res = sector(radio, angulo)
        print("%.2f" % res)
    elif opcion == 2:
        a = float(input())
        b = float(input())
        res = eclipse(a, b)
        print("%.2f" % res)
    elif opcion == 3:
        a = float(input())
        h = float(input())
        res = paralelogramo(a, h)
        print("%.2f" % res)
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()
     
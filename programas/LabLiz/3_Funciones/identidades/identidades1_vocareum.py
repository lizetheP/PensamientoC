import math

def gradosRadianes(grados):
    return (math.pi*grados)/180

def cosecante(grados):
    radianes = gradosRadianes(grados)
    return 1/math.sin(radianes)

def secante(grados):
    radianes = gradosRadianes(grados)
    return 1/math.cos(radianes)

def identidades():
    print("1.Cosecante")
    print("2.Secante")
    print("3.Salir")
    
def main():
    #identidades()
    opcion = int(input())
    if opcion == 1:
        grados = float(input())
        resultado = cosecante(grados)
        print("%.1f" % resultado)
    elif opcion == 2:
        grados = float(input())
        resultado = secante(grados)
        print("%.1f" % resultado)
    elif opcion == 3:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()     

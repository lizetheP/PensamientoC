import math

def gradosRadianes(grados):
    return (math.pi*grados)/180

def secanteCuadrada(grados):
    radianes = gradosRadianes(grados)
    return (1 + math.tan(radianes))

def cotangente(grados):
    radianes = gradosRadianes(grados)
    return 1/math.tan(radianes)

def identidades():
    print("1.Secante")
    print("2.Cotangente")
    print("3.Salir")
    
def main():
    #identidades()
    opcion = int(input())
    if opcion == 1:
        grados = float(input())
        resultado = secanteCuadrada(grados)
        print("%.1f" % resultado)
    elif opcion == 2:
        grados = float(input())
        resultado = cotangente(grados)
        print("%.1f" % resultado)
    elif opcion == 3:
        print("Adios")
    else:
        print("ERROR OPCION INVALIDA")
        
main()     

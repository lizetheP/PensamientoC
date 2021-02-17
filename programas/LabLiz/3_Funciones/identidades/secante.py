import math

def gradosRadianes(grados):
    return (math.pi*grados)/180

def secanteCuadrada(grados):
    radianes = gradosRadianes(grados)
    return (1 + math.tan(radianes))

def secante(grados):
    radianes = gradosRadianes(grados)
    return 1/math.cos(radianes)

def cotangente(grados):
    radianes = gradosRadianes(grados)
    return 1/math.tan(radianes)

def cosecante(grados):
    radianes = gradosRadianes(grados)
    return 1/math.sin(radianes)

def identidades():
    print("1.Secante")
    print("2.Cosecante")
    print("3.Salir")
    
def main():
    identidades()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        grados = float(input("Introduce los grados: "))
        resultado = secante(grados)
        print("secante(%.1f) = %.1f" % (grados,resultado))
    elif opcion == 2:
        grados = float(input("Introduce los grados: "))
        resultado = cosecante(grados)
        print("cosecante(%.1f) = %.1f" % (grados,resultado))
    elif opcion == 3:
        print("Adios")
    else:
        print("ERROR OPCION INVALIDA")
        
main()     

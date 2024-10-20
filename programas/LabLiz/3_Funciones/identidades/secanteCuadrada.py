import math

def gradosRadianes(grados):
    return (math.pi*grados)/180

def secante_cuadrada(grados):
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
    identidades()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        grados = float(input("Introduce los grados: "))
        resultado = secante_cuadrada(grados)
        print("secante(%.1f) = %.1f" % (grados,resultado))
    elif opcion == 2:
        grados = float(input("Introduce los grados: "))
        resultado = cotangente(grados)
        print("cotangente(%.1f) = %.1f" % (grados,resultado))
    elif opcion == 3:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()     

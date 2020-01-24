#título          :prisma pentagonal funciones.py
#descripción     :calcula el volumen de un prisma pentangonal.
#autor           :Benjamín Valdés
#python_version  :3.5.2  
#===============================================================

# este programa de ejemplo calcula el 
# peritro de un pentágono, el área de 
# un pentágono y el volmuen de un prisma pentagonal


def perimetro(lado):
    # Devuelve el perimetro de un pentágono.
    return lado * 5

def area(lado, apotema):
    # Devuelve el area de un pentágono
    return (perimetro(lado) * apotema) / 2

def volumen(lado, apotema, altura):
    # Devuelve el volumen de un prisma pentagonal    
    return area(lado, apotema) * altura



print("prisma pentagonal rectangular")

print("volumen de prisma es ", volumen(5,3,6))

print("area del pentágono  es ", area(50, 33))

print("perimetro del pentágono es ", perimetro(301))

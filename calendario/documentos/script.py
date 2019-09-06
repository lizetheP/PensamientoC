#título          :llena estos espacios con tus datos
#descripción     :
#autor           :
#python_version  :  
#==========================================================================

#
 
"""base = 1
altura = 2
area = (base*altura)/2
print("área triangulo", area)"""

def areaTriangulo(base, altura):
    return (base*altura)/2

res = areaTriangulo(1, 2)
print("El área del triángulo es: ", res)

"""lado = 2
area = lado*lado
print("área cuadrado", area)"""

def areaCuadrado(lado):
    return lado*lado

res = areaCuadrado(2)
print("El área del cuadrado es: ", res)

"""base = 1
altura = 2
area_triangulo = (base*altura)/2"""

area_triangulo = areaTriangulo(1,2)
area_cuadrado = areaCuadrado(2)
"""lado = 2
area_cuadrado = lado * lado"""
area_piramide = area_triangulo + area_cuadrado
print("área pirámide", area_piramide)
#título          :prisma pentagonal.py
#descripción     :calcula el volumen de un prisma pentangonal.
#autor           :Benjamín Valdés
#python_version  :3.5.2  
#===============================================================

# este programa de ejemplo calcula el 
# peritro de un pentágono, el área de 
# un pentágono y el volmuen de un prisma pentagonal


print("prisma pentagonal rectangular")

lado = 5
apotema = 3
altura = 6

perimetro = lado * 5
area = (perimetro * apotema) / 2
volumen = area * altura

print("volumen de prisma es ", volumen)

lado = 50
apotema = 33

perimetro = lado * 5
area = (perimetro * apotema)/2

print("area del pentágono  es ", area)


lado = 301
perimetro = lado * 5

print("perimetro del pentágono es ", perimetro)

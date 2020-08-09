print("MENU")
print("1. Corriente")
print("2. Voltaje")
print("3. Resistencia")
opcion=int(input("Introduce una opcion: "))
if opcion == 1:
    v = float(input("Introduce el voltaje: "))
    r = float(input("Introduce la resistencia: "))
    if r > 0:
        i = v/r
        print("La corriente es: ", i)
    else:
        print("La resistencia no puede ser negativa ni cero")
elif opcion == 2:
    i = float(input("Introduce la corriente: "))
    r = float(input("Introduce la resistencia: "))
    v = i*r
    print("La corriente es: ", v)
elif opcion == 3:
    i = float(input("Introduce la corriente: "))
    v = float(input("Introduce el voltaje: "))
    if i > 0:
        r = v/i
        print("La resistencia es: ", r)
    else:
        print("La corriente no puede ser negativa ni cero")    
else:
    print("Opción incorrecta")
    
   
             

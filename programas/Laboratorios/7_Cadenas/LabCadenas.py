def limpiaCadena(caracteresSeguros, cadena):
    cadena2 = ""
    for i in range(0, len(cadena)):
        if (cadena[i] in caracteresSeguros):
            cadena2 = cadena2 + cadena[i]
    return cadena2

def cuentaOcurrencias(cadena, caracter):
    cont =0
    cadena = cadena.lower()
    caracter = caracter.lower()
    for i in range(0, len(cadena)):
        if cadena[i] == caracter:
            cont = cont + 1
    return cont

def obtenNombreCompleto(nombres, paterno, materno):
    cadena = nombres + " " +paterno + " " + materno
    return cadena

def deletreaCadena(cadena):
    cadena2 = ""
    for i in range(0, len(cadena)):
        if i < len(cadena)-1:
            cadena2 = cadena2 + cadena[i] + "-"
        else:
            cadena2 = cadena2 + cadena[i]
    return cadena2

"""def deletreaCadena2(cadena):
    cadena2 = ""
    for i in range(0, len(cadena)):
        if i < len(cadena)-1:
            print(cadena[i], end="-")
        else:
            print(cadena[i])
   """         
def menu():
    print("1. Limpia cadena")
    print("2. Cuenta ocurrencias")
    print("3. Obten nombre completo")
    print("4. Deletrea cadena")
    
caracteresSeguros = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑáéíóú0123456789"
while True:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        c = str(input("Introduce una cadena: "))
        cadena = limpiaCadena(caracteresSeguros, c)
        print(cadena)
    elif opcion == 2:
        cad = str(input("Introduce una cadena: "))
        c = str(input("Introduce un caracter: "))
        res = cuentaOcurrencias(cad, c)
        print(res)
    elif opcion == 3:
        nombres = str(input("Introduce tu nombre: "))
        aPaterno = str(input("Introduce tu apellido paterno: "))
        aMaterno = str(input("Introduce tu apellido materno: "))
        cadena = obtenNombreCompleto(nombres, aPaterno, aMaterno)
        print(cadena)
    elif opcion == 4:
        c = str(input("Introduce una cadena: "))
        deletreaCadena2(c)
        #cadena = deletreaCadena(c)
        #print(cadena)
    else:
        print("Opción inválida")
            
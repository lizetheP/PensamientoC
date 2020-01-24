import math

cont = 0
n = 1
cA = 0
cN = 0

def compruebaClave(listaClaves):
    clave = str(input("Introduce tu clave: "))
    while not (clave in listaClaves):
        clave = str(input("Clave incorrecta. Introduce tu nuevamente tu clave: "))
    print("Bienvenido")
   


listaClaves = ["1234", "5678", "9123","3456", "7891", "8913"]
compruebaClave(listaClaves)
sT = 1000
print("El saldo de la tarjeta es:", sT)

def realizarPago():
    global sT
    cT = cA + cN
    tCa = print("Total de consumo adulto:", cA)
    tCn = print("Total de consumo niño:", cN)
    tC = print("Total de consumo:", cT)
    propina = int(input("Introduce el porcentaje de propina:"))
    porcentaje = cT * propina / 100
    tP = porcentaje + cT
    propinaT = print("Total de propina:", porcentaje)
    totalP = print("Total general:", tP)
    compruebaClave(listaClaves)

    if sT >= tP and cT <= 500:
        print("Gracias por su compra.")
        sT = sT - tP
        print("El nuevo saldo es:", sT)
    elif sT >= tP and cT >= 500 and propina < 10:
        print("Gracias por su compra.")
        sT = sT - tP
        print("El nuevo saldo es:", sT)
    elif sT >= tP and cT > 500 and propina >= 10:
        print("Gracias por su compra.")
        print("Ya puedes gozar de internet gratis por cortesía de la casa.")
        sT = sT - tP
        print("El nuevo saldo es:", sT)
    else:
        print("Saldo insuficiente.")
        print("Recarga tu tarjeta.")
        print("El saldo es:", sT)

    return menuPrincipal()


def recargaTarjeta():
    global sT
    print("1. $100.00")
    print("2. $250.00")
    print("3. $500.00")
    opcion = int(input("Introduce una opcion:"))

    if opcion == 1:
        print("Tu recarga es de $100.00")
        sT = sT + 100.00
        print("Tu nuevo saldo es:", sT)
    elif opcion == 2:
        print("Tu recarga es de $250.00")
        sT = sT + 250.00
        print("Tu nuevo saldo es:", sT)
    elif opcion == 3:
        print("Tu recarga es de $500.00")
        sT = sT + 500.00
        print("Tu nuevo saldo es:", sT)
        global cont
        cont += 1
        print (cont)
        if (cont == 3):
            print("Se te abonó $100.00 gratis")
            print("Tu nuevo saldo es:", sT + 100)
            cont = 0
    else:
        print("Opción invália")
        print("Gracias.")
    return menuPrincipal()

 
def menuPrincipal():
    print("1. Menú adultos")
    print("2. Menú niños")
    print("3. Realizar pago")
    print("4. Recarga de tarjeta")
    print("5. Salir")
    opcion = int(input("Introduce una opcion:"))
    return opcion

def menuAdulto(opc):
    global cA
    if opc == 1:
        print("El precio del menú es: $176.00")
        cA += 176.00
    elif opc == 2:
        print("El precio del menú es: $185.00")
        cA += 185.00
    elif opc == 3:
        print("El precio del menú es:  $169.00")
        cA += 169.00
    else:
        print("Opción inválida.")
        print("El precio del menú es: $0.00")
    return menuPrincipal()

def menuNino(opc):
    global cN
    if opc== 1:
        print("El precio del menú es: $100.00")
        cN += 100.00
    elif opc == 2:
          print("El precio del menú es: $115.00")
          cN += 115.00
    elif opc == 3:
          print("El precio del menú es:  $120.00")
          cN += 120.00
    else:
          print("Opción inválida.")
          print("El precio del menú es: $0.00")
    return menuPrincipal() 

op = menuPrincipal()
while op:
    if op == 1:
        print("Menú adultos")
        print("1.Enchiladas $176.00")
        print("2.Pollo a la jardinera $185.00")
        print("3.Pescado empanizado $169.00")
        opc = int(input("Introduce número de platillo:"))
        op = menuAdulto(opc)
    elif op == 2:
        print("Menú niños")
        print("1.Pizza $100,00")
        print("2.Hot Dog $115.00")
        print("3.Hamburguesa $120.00")
        opc = int(input("Introduce número de platillo:"))
        op = menuNino(opc)
    elif op == 3:
        print("Realizar pago")
        op = realizarPago()
    elif op == 4:
        print("Recarga de tarjeta")
        op = recargaTarjeta() 
    elif op == 5:
        print("Gracias")
        break
    else:
        print("Opción invália")
        break
        

def compruebaClave(listaClaves):
        clave = str(input("Introduce tu clave: "))
        while not (clave in listaClaves):
            clave = str(input("Clave incorrecta, introduce de nuevo tu clave: "))
            
def menuPrincipal():
    print("1. Menú de adulto")
    print("2. Menú de niño")
    print("3. Realizar pago")
    print("4. Recarga de tarjeta")
    print("5. Salir")
    opcion = int(input("Selecciona una opción: "))
    return opcion

def menuAdulto():
    print("Menú de adulto:")
    print("1. Carne asada $230")
    print("2. Chiles rellenos $150")
    print("3. Enchiladas verdes/rojas $95")
    precio= int(input("Seleccione un platillo: "))
    if precio == 1:
        return 230
    elif precio == 2:
        return 150
    elif precio == 3:
        return 95
    else:
        return 0    
    
def menuNino():
    print("Menú de niño:")
    print("1. Hamburguesa chica $65")
    print("2. Sopa de verduras $55")
    print("3. Ensalada $50")
    precio= int(input("Seleccione un platillo: "))
    if precio == 1:
        return 65
    elif precio == 2:
        return 55
    elif precio == 3:
        return 50
    else:
        return 0

def realizarPago(totalComAdulto, totalComNino, saldoTarjeta, listaClaves):
    totalConsumo= totalComAdulto + totalComNino
    print("El total de consumo de adulto es: $", totalComAdulto)
    print("El total de consumo de niño es: $", totalComNino)
    print("El total de consumo es: $", totalConsumo)
    propina = int(input("¿Que porcentaje de propina desea agregar?"))
    totalPropina = (propina * totalConsumo) / 100
    totalGeneral= totalConsumo + totalPropina
    print("La propina es: $", totalPropina)
    print("El total general es: $", totalGeneral)
    if saldoTarjeta >= totalGeneral:
        compruebaClave(listaClaves)
        saldoTarjeta= saldoTarjeta - totalGeneral
        print("Gracias por su compra")
        if totalConsumo > 500 and totalPropina > 10:
            print("Gracias por su compra, usted puede gozar de internet gratis por cortesía de la casa")
        else:
            print("")
    elif saldoTarjeta < totalGeneral:
        print("Recarga tu tarjeta de prepago")
    return saldoTarjeta

def recargaTarjeta(saldoTarjeta):
    global contRec500  
    print("Recargas de tarjeta:")
    print("1. $100")
    print("2. $250")
    print("3. $500")
    opcion= int(input("Seleccione la cantidad que desea recargar: "))
    if opcion == 1:
        saldoTarjeta= saldoTarjeta + 100
    elif opcion == 2:
        saldoTarjeta= saldoTarjeta + 250
    elif opcion == 3:
        contRec500 = contRec500 +1 
        saldoTarjeta= saldoTarjeta + 500
        if contRec500 == 3:
            saldoTarjeta= saldoTarjeta + 100
            print("Ha obtenido una bonificación de $100")
        else:
            print("")
    else:
        print("Opción invalida")
    return saldoTarjeta 
    
    
    
    
saldo= 1000
listaClaves = ["1234", "5678", "9123", "3456", "7891"]
totalA= 0
totalN= 0
contRec500= 0
op = 0 
while op < 5:
    op= menuPrincipal()
    if op == 1:
        precio = menuAdulto()
        totalA= totalA + precio
    elif op == 2:
        precio = menuNino()
        totalN= totalN + precio
    elif op == 3:
        print("Realizar pago")
        saldo= realizarPago(totalA, totalN, saldo, listaClaves)
    elif op == 4:
        print("Recarga de tarjeta")
        compruebaClave(listaClaves)
        print("Bienvenido")
        saldo = recargaTarjeta(saldo)
        print("Su saldo es: $", saldo)
    elif op == 5:
        break
    else:
        print("")
    

    
    
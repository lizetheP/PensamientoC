# Variables
menu =()
saldo = 1000
totalComAdulto = 0
totalComNino = 0
contRec500 = 0

def compruebaClave(listaClaves):
    clave = str(input("Introduce tu clave"))
    while not (clave in listaClaves):
        clave = str(input("Clave incorrecta, introduce de nuevo tu clave"))
    print ("Bienvenido")
    
listaClaves = ["1234" , "5678" , "9123" , "3456" , "7891" , "8913"]
compruebaClave (listaClaves)

def menuAdulto ():
    print ("1. Salmón")
    print ("2. Tacos de camarón")
    print ("3. Burrata")
    op = int(input("Introduce una opción"))
    if op == 1:
        precio = 180.00
        return precio
    elif op == 2:
        precio = 200.00
        return precio
    elif op == 3:
        precio = 300.00
        return precio
    else:
        precio = 0.00
        return precio
    
def menuNiño ():
    print ("1. Hamburguesa")
    print ("2. Spaghetti")
    print ("3. Pizza")
    op = int(input("Introduce una opción"))
    if op == 1:
        precio = 80.00
        return precio
    elif op == 2:
        precio = 50.00
        return precio
    elif op == 3:
        precio = 40.00
        return precio
    else:
        precio = 0.00
        return precio


def realizarPago (totalComAdulto, totalComNino, saldoTarjeta):
    print ("El total de comida de adulto es:", totalComAdulto)
    print ("El total de comida de niño es:", totalComNino)
    totalCon = totalComAdulto + totalComNino
    propina = int(input("¿Que porcentage desea agregar?"))
    propinaF = (propina / 100) * totalCon
    print ("El total de propina es:",propinaF)
    pagoT = propina + totalCon
    print ("El total de pago es:", pagoT)
    if saldoTarjeta < pagoT :
        print ("Recarga tu tarjeta")
    else :
        if pagoT >= 500 and propina >= 10:
            print ("Gracias por su compra. Puede usar internet gratis por cortesía de la casa.")
        else :
            compruebaClave(listaClaves)
            print ("Gracias por su compra")
    totalSaldo = saldoTarjeta - pagoT
    print ("El nuevo saldo es:", totalSaldo)
    return saldoTarjeta

def recargaTarjeta (saldoTarjeta):
    global contRec500
    print ("1. $100.00")
    print ("2. $250.00")
    print ("3. $500.00")
    op = int(input("Introduce una opción"))
    if op == 1:
        recarga = 100.00 + saldoTarjeta
        return recarga
    elif op == 2:
        recarga = 250.00 + saldoTarjeta
        return recarga
    elif op == 3:
        recarga = 500.00 + saldoTarjeta
        recarga = recarga + 1
        if recarga >= 3:
            recarga = recarga + 100.00
            print ("Te has ganado $100 extra de recarga, ahora cuentas con:", saldoTarjeta)
        return recarga
    else:
        print ("Opción inválida")
        
def menuPrincipal ():
     print ("1. Menu Adulto")
     print ("2. Menu Niño")
     print ("3. Realiza Pago")
     print ("4. Recarga Tarjeta")
     opcion = int(input("Introduce una opción"))
     return opcion
def Salir ():
    print ("salir")
     
op = 0    
while op != 5:
    op = menuPrincipal ()
    if op == 1:
        print ("Menu Adulto")
        precio= menuAdulto ()
        print ("El precio del menu es:", precio)
    elif op == 2:
        print ("Menu Niño")
        precio = menuNiño ()
        print ("El precio del menu es:", precio)
    elif op == 3:
        print ("Realiza Pago")
        totalComAdulto = int (input("Introduce el consumo total del adulto"))
        totalComNino = int (input("Introduce el consumo total del niño"))
        saldoTarjeta = int(input(" Introduce el saldo de tarjeta"))
        saldoTarjeta = realizarPago (totalComAdulto, totalComNino, saldoTarjeta)
    elif op == 4:
        print ("Recarga Tarjeta")
        saldoTarjeta = int(input(" Introduce el saldo de tarjeta"))
        recarga = recargaTarjeta (saldoTarjeta)
        print ("Nuevo Saldo es:", recarga)
    elif op == 5:
        print ("Salir")
        break
    else:
        print ("Opción invalida") 
 

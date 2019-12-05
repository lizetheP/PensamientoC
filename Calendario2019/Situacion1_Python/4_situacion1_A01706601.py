def compruebaClave(listaClaves):
    clave=str(input("Introduce tu clave:"))
    while not(clave in listaClaves):
        clave=str(input("Clave incorrecta, introduce de nuevo tu clave:"))
    print("Bienvenido")

def menuPrincipal():
    print("1.Menu adulto")
    print("2.Menu niño")
    print("3.Realizar pago")
    print("4.Recarga de tarjeta")
    print("5.Salir")
    opcion=int(input("Introduce una opcion:"))
    return opcion

def menuAdulto():
    print ("1.Arrachera $200")
    print ("2.Filete de pescado $250")
    print ("3.Alambre de carnes $300")
    op=int(input("Introduce una opcion:"))
    if op==1:
        return 200
    elif op==2:
        return 250
    elif op==3:
        return 300
    else:
        print("Opcion invalida")
        return 0
    
def menuNino():
    print ("1.Hamburguesa $100")
    print ("2.Pechuga rellena de queso $150")
    print ("3.Pizza $200")
    opcion=int(input("Introduce una opcion:"))
    if op==1:
        return 100
    elif op==2:
        return 150
    elif op==3:
        return 200
    else:
        print("Opcion invalida")
        return 0
    
def realizarPago(totalComAdultos,totalComNinos, saldo, listaClaves):
    totalConsumo=totalComAdultos+totalComNinos
    print("Total consumo:",totalConsumo)
    propina=float(input("Introduce el porcentaje de propina:"))
    totalPropina = totalConsumo*propina/100
    print("Total de propina:",totalPropina)
    totalGeneral=totalConsumo+totalPropina
    print("Total general:",totalGeneral)
    if saldo>totalGeneral:
        compruebaClave(listaClaves)
        saldo=saldo-totalGeneral
        print("Su saldo actual es:",saldo)
        if totalConsumosaldo > 500 and propina > 10:
            print("Puede gozar de Internet gratis")
    else:
        print("Recarga de tarjeta")
    return saldo

def recargaTarjeta(saldoTarjeta):
    global contRec500
    print("1.$100")
    print("2.$250")
    print("3.$500")
    opcion=int(input("Introduce una opcion:"))
    if opcion == 1:
        saldoTarjeta = saldoTarjeta + 100
    elif opcion == 2:
        saldoTarjeta=saldoTarjeta+250
    elif opcion == 3:
        saldoTarjeta = saldoTarjeta + 500
        contRec500 = contRec500 + 1
    return saldoTarjeta
 

tAdultos=0
tNinos=0
saldo=1000
contRec500 = 0
listaClaves=["1234","5678","9123","4567","8912"]
compruebaClave(listaClaves)
op = 0
while op!=5:
    op=menuPrincipal()
    if op==1:
        precio=menuAdulto()
        tAdultos=tAdultos+precio
    elif op==2:
        precio=menuNino()
        tNinos=tNinos+precio
    elif op==3:
        print("Realizar pago:")
        saldo = realizarPago(tAdultos, tNinos, saldo, listaClaves)
        print("El nuevo saldo es:",saldo)
    elif op==4:
        print("Recarga de tarjeta")
        saldo = recargaTarjeta(saldo)
        print("El nuevo saldo es:",saldo)
        if contRec500 == 3:
            saldo = saldo + 100
    elif op==5:
        break
    else:
        print("Opcion invalida")
    
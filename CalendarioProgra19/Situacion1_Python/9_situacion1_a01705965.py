def compruebaClave(listaClaves):
    clave=str(input("Introduce tu clave "))
    while not(clave in listaClaves):
        clave=str(input("Clave incorrecta, introduce de nuevo la clave "))
    print("Bienvenido")
    
def menuPrincipal():
    print("1. Menú de adulto")
    print("2. Menú de niño")
    print("3. Realizar pago")
    print("4. Recargar tarjeta")
    print("5. Salir")
    opcion=int(input("Introduce una opción: "))
    return opcion

def menuAdulto():
    print("1. Pozole $85")
    print("2. Enchiladas verdes $90")
    print("3. Chiles rellenos $135")
    opcion=int(input("Seleccione una opción del menú: "))
    if opcion == 1:
        return 85
    elif opcion ==2:
        return 90
    elif opcion ==3:
        return 135
    else:
        return 0
            
def menuNino():
    print("1. Tacos dorados $95")
    print("2. Hamburguesa con papas $125")
    print("3. Milanesa empanizada $110")
    opcion=int(input("Seleccione una opción del menú: "))
    if opcion == 1:
        return 95
    elif opcion ==2:
        return 125
    elif opcion ==3:
        return 110
    else:
        return 0
  
def realizarPago(totalA, totalN, saldoTarjeta, listaClaves):
    totalConsumo= totalA+totalN
    print("El total del consumo de adulto es: ", totalA)
    print("El total del consumo de niño es: ", totalN)
    print("El consumo total es: ", totalConsumo)
    propina=float(input("Introduce el porcentaje de propina que deseas agregar: "))
    totalGeneral= (totalConsumo*(propina/100))+totalConsumo
    totalPropina=totalConsumo*(propina/100)
    print("El total de la propina es: ", totalPropina)
    print("El total del consumo con propina es: ", totalGeneral)
    if saldoTarjeta<totalGeneral:
        print("Recarga tu tarjeta de prepago")
    elif saldoTarjeta > totalGeneral:        
        compruebaClave(listaClaves)
        saldoTarjeta=saldoTarjeta-totalGeneral
        print("Gracias por su compra")
        print("El nuevo saldo de tu tarjeta es: ", saldoTarjeta)
        if totalConsumo>=500 and propina>10:
            print("Puede gozar internet gratis por cortesía de la casa")
    return saldoTarjeta

def recargarTarjeta(saldoTarjeta):
    global cont
    
    print("1. $100")
    print("2. $250")
    print("3. $500")
    opcion=int(input("Seleccione una opción de recarga: 1/2/3 "))
    if (opcion==1):
        saldoTarjeta=saldoTarjeta+100
        print("El nuevo saldo es: ", nuevoSaldo)
    elif (opcion==2):
        saldoTarjeta=saldoTarjeta+250
        print("El nuevo saldo es: ", nuevoSaldo)
    elif (opcion==3):
        saldoTarjeta=saldoTarjeta + 500
        cont = cont + 1
        if cont==3:
            saldoTarjeta=saldoTarjeta+100
            print("Se ha hecho acreedor a $100 extra de recarga, su nuevo saldo es: ", saldoTarjeta)
        print("El nuevo saldo es: ", saldoTarjeta)
    else:
        print("Opción incorrecta")
        print ("El saldo de la tarjeta es: ", saldoTarjeta)
    return saldoTarjeta

    
listaClaves=["1234", "5678", "9123", "3456", "7891", "8913"]
compruebaClave(listaClaves)
    
cont = 0
op=0
totalA = 0
totalN = 0
saldoTarjeta = 1000
listaClaves=["1234", "5678", "9123", "3456", "7891", "8913"]
while op<=5:
    op=menuPrincipal()
    if op==1:
        print("Menú de adulto ")
        precioA=menuAdulto()
        totalA = totalA + precioA
        
    elif op==2:
       print("El menú de niño es: ")
       precioN=menuNino()
       totalN=totalN+precioN
    
    elif op==3:
        print("Realizar pago: ")
        saldoTarjeta = realizarPago(totalA, totalN, saldoTarjeta, listaClaves)
        
    elif op==4:
        print("Recargar tarjeta")
        saldoTarjeta =recargarTarjeta(saldoTarjeta)
        
    elif op==5:
        break
          
    else:
        print("Opción inválida")



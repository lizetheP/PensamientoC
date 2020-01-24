totalAdultos = 0
totalNinos = 0
totalPropina = 0
totalGeneral = 0
listaClaves = ["4321", "6284", "0486", "2735", "6667"]


def menuPrincipal():
    print("1. Menú de adulto ")
    print("2. Menú de niño ")
    print("3. Realizar pago ")
    print("4. Recarga tarjeta ")
    print("5. Salir ")
    opcion = int(input("Introduce una opción: "))
    return opcion


def menuAdulto():
    res = int(input("Seleccione una opción: "))
    if res == 1:
        print ("el precio del menú es de $120")
        precio = float(0+120)
        return precio
    
    elif res == 2:
        print ("El precio del menú es de $110.00 ")
        precio = float(0+110)
        return precio
        
    elif res == 3:
        print ("El precio del menu es $140.00")
        precio = float(0+140)
        return precio

    else:
        print ("Intente otra vez")
        print("0")
    
def menuNino(): 
    res = int(input("Seleccione una opción: "))
    if res == 1:
        print ("el precio del menú es : $120.00")
        precio = float(0+120)
        return precio
    elif res == 2:
        print ("El precio del menú es : $150.00 ")
        precio = float(0+150)
        return precio
    elif res == 3 :
        print ("El precio del menú es : $180.00 ")
        precio = float(0+180)
        return precio
    else :
        print ("Intente otra vez")
        print("0") 

def recargarTarjeta (SaldoTarjeta):
    global contRec500
    global saldoTarjeta
    print ("el saldo de su tarjeta es:", saldoTarjeta)
    print ("Recargar tarjeta")
    print ("1. $100")
    print ("2. $250")
    print ("3. $500")
    print ("4. Salir")
    recTar =(input("Seleccionar una opcion:"))
    if (recTar == "1"):
        saldoTarjeta += 100
        print ("El nuevo saldo de la tarjeta es:", saldoTarjeta)
    elif (recTar == "2"):
        saldoTarjeta += 250
        print ("El nuevo saldo de la tarjeta es:", saldoTarjeta)
    elif (recTar == "3") :
        if contRec500 >=2:
            saldoTarjeta += 600
            print ("Por tres recargas, se le agregan 100 pesos a su saldo actual, su nuevo saldo es :", saldoTarjeta)
        else :
            saldoTarjeta += 500
            contRec500 +=1 
            print ("El nuevo saldo de la tarjeta es:", saldoTarjeta)
    elif recTar == 4: 
        print ("Opción inválida")


def realizarPagos (totalAdultos, totalNinos, saldoTarjeta, listaClaves):

    totalConsumo = totalNinos + totalAdultos
    print("Consumo menú adultos:", totalAdultos,"\nConsumo menú niños:", totalNinos,"\nTotal de consumo:", totalConsumo)
    propinaAgregada= input ("¿Desea agregar propina? si/no: ")
    totalPropina = 0
    totalGeneral = totalConsumo
    
    if (propinaAgregada.lower() == "si"):
        propina = float(input("Introducir porcentaje de propina que desea dejar: "))
        totalPropina = totalConsumo*propina/100
        print("La propina es de: ", totalPropina)
    print("Resumen General\nTotal consumo,$ " + str(totalAdultos)+ "en menú adultos\nTotal consumo,$" + str(totalNinos)+ "en menú ninos")
    print(" \n La cantidad a pagar de la propina es",totalPropina)
    print(" \n La cantidad a pagar es: ", totalGeneral)
    saldoTarjeta = 1000
    
    if totalGeneral > saldoTarjeta :
        print ("Saldo insuficiente, su saldo actual es de : ", saldoTarjeta, "Favor de recargar su tarjeta")
    
    else :
        saldoTarjeta = saldoTarjeta - totalGeneral
        totalGeneral = totalConsumo + totalPropina
        if (totalGeneral > 500 and totalPropina > 10):
            print ("Querido usuario, usted puede gozar de internet gratuito, invita la casa")
    propAutorizada = int(input("Introduzca su clave para autorizar el descuento de la propina: "))
    if (propAutorizada == 4321):
        print ("su saldo actual es de : $", saldoTarjeta)
        print ("Gracias por su compra ! ")


    

def compruebaClave (listaClaves):
    clave = str (input("Introduce tu clave: "))
    
    while not (clave in listaClaves) :
        clave = str (input("Clave incorrecta, introduce clave correcta"))
    print ("Bienvenido") 

compruebaClave (listaClaves)


saldoTarjeta = 1000
recargaTarjeta = 0
nuevoSaldo =0
op=0
recTar = 0
contRec500 =0

while (op != '5'):
    print ("1. Menu Adulto")
    print ("2. Menu de Niño")
    print ("3. Realizar pago") 
    print ("4. Recarga Tarjeta")
    print ("5. Salir")
    op = int (input("Introduce una opción :"))
    
    if op == 1 :
        print ("Menu Adulto")
        print ("     1. Chilaquiles $120")
        print ("     2. Molletes $110")
        print ("     3. Omelette $140")
        totalAdultos += menuAdulto() 
        
    elif op == 2 :
        print ("Menu Niño")
        print ("     1. Nuggets del pollo $120")
        print ("     2. Sandwich $150")
        print ("     3. Pancakes $180")
        totalNinos += menuNino() 
    
    elif op == 3 :
        print ("Realizar pago")
        realizarPagos (totalAdultos, totalNinos, saldoTarjeta, listaClaves)
        
    elif op == 4 :
        print ("Recarga Tarjeta")
        recargarTarjeta(saldoTarjeta)
        
    elif op == 5 :
        print ("Salir") 
        break
    else :
        print ("Opción Inválida")
    


    
  

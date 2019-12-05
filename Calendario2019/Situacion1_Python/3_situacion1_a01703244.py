def compruebaClave (listaClave):
    clave= str(input("Introduce tu clave:"))
    while not(clave in listaClave):
        clave= str(input("Clave incorrecta, introduce de nuevo tu clave:"))
    print ("Bienvenido")
        
listaClave =["1234", "7162", "6243", "4621", "8931"]
compruebaClave (listaClave)


def menuAdulto ():
    print ("1. Tacos $100.00")
    print ("2. Enchiladas $1500.00")
    print ("3. Torta $250. 00")
    op = int(input("Introduce una opcion: "))
    if op== 1:
        precio = 100.00
        return precio
    elif op== 2:
        precio= 150.00
        return precio 
    elif op== 3:
        precio= 250.00
        return precio 
    else:
        precio= 0.00
        return precio

def menuNino ():
    print ("1. Quesadillas 80.00")
    print ("2. Hot Dogs $60.00")
    print ("3. Galletas de chocolate $40.00")
    op= int(input("Introduce la opción:"))
    if op== 1:
        precio= 80.00
        return precio
    elif op== 2:
        precio= 60.00
        return precio 
    elif op== 3:
        precio= 40.00
        return precio 
    else:
        precio= 0.00
        return precio

    
def realizarPago (totalCA, totalCN, saldoTarjeta, listaClave):
    print ("Total de comidas de Adulto es:", totalCA)
    print ("Total de comidas de Niño es:", totalCN)
    totalF= totalCA+totalCN
    print ("El consumo total sin propina es:", totalF)
    propina= int(input("Introduce el porcentaje de propina:"))
    propinaF= (propina/100)* totalF
    print ("Total de propina:", propinaF)
    totalFP= totalF+propinaF
    print ("El consumo total con propina es:", totalFP)
    print ("Saldo total de la tarjeta es:", saldoTarjeta)
    if saldoTarjeta<totalFP:
        print ("Recargar tarjeta")
    else:
        compruebaClave(listaClave)
        if totalFP>= 500 and propina>=10:
            print ("Gracias por su compra, puedes gozar de internet gratis por cortesía de la casa:")
        else:
            print ("Gracias por su compra")
        saldoTarjeta= saldoTarjeta-totalFP
        print ("El nuevo saldo es:", saldoTarjeta)
    return saldoTarjeta
    
def recargaTarjeta (saldoTarjeta):
    global contRec500 
    print ("El saldo actual de tu tarjeta es:", saldoTarjeta)
    print ("1. $100.00")
    print ("2. $250.00")
    print ("3. $500.00")
    op= int(input("Introduce una opción: "))
    if op== 1:
        saldoTarjeta= saldoTarjeta+100.000
        return saldoTarjeta
    elif op== 2:
        saldoTarjeta= saldoTarjeta+250.00
        return saldoTarjeta 
    elif op== 3:
        saldoTarjeta= saldoTarjeta+500.00
        contRec500= contRec500 + 1
        print ("El contador subio a: ", contRec500)
        if contRec500 >= 3:
            saldoTarjeta= saldoTarjeta+ 100
            return saldoTarjeta
        else:
            return saldoTarjeta
    else:
        print ("Opción inválida, el saldo de tu tarjeta no fue modificado")
        return saldoTarjeta


def menuPrincipal ():
    print ("1. Menu adulto")
    print ("2. Menu niño")
    print ("3. Realiza pago")
    print ("4. Recarga tarjeta")
    print ("5. Salir")
    opcion= int(input("Introduce una opción:"))
    return opcion

op= 0
saldoTarjeta= 1000
totalCA= 0
totalCN=  0
contRec500= 0 
while (op!= 5):
    op= menuPrincipal ()
    if op== 1:
        print ("Menu adulto")
        precio = menuAdulto()
        print("El precio es: ", precio)
        totalCA= totalCA+precio
    elif op== 2:
        print ("Menu niño")
        precio= menuNino()
        print ("El precio es:", precio)
        totalCN= totalCN+precio
    elif op== 3:
        print ("Realiza pago")
        saldoTarjeta= realizarPago (totalCA,totalCN, saldoTarjeta, listaClave)
    elif op== 4:
        print ("Recarga tarjeta")
        saldoTarjeta= recargaTarjeta(saldoTarjeta)
        print ("El nuevo saldo es: ", saldoTarjeta)
    elif op==5:
        break 
    else:
        print ("Opción inválida")


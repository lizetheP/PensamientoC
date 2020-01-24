import math

def compruebaClave(listaClaves):
    clave = str(input("Introduce la clave "))
    while not(clave in listaClaves):
        clave = str(input("Clave de acceso incorrecta, introduce de nuevo tu clave "))
    print("Bienvenido")

listaClaves = ["2404", "0424", "0401", "0104", "1234"]
compruebaClave(listaClaves)

def menuPrincipal():
    print("1.Menú Adulto")
    print("2.Menú Niño")
    print("3.Realizar pago")
    print("4.Recarga de tarjeta")
    print("5.Salir")
    opcion = int(input("Ingresa una opción del menú "))
    return opcion

def menuAdulto():
    print("Menú de Adulto")
    print("1.Tampiqueña $95")
    print("2.Hamburguesa $75")
    print("3.Orden de Tacos $30")
    op = int(input("Ingrese una opción "))
    if op == 1: 
     return 95 
    elif op == 2:
     return 75
    elif op == 3:
     return 30
    else:   
        print("El precio del platillo es: 0")    
    return menuPrincipal()

def menuNiño():
    print("Menú de Niño")
    print("1.Dedos de pescado $55")
    print("2.Nuggets $45")
    print("3.Helado $15")
    op= int(input("Ingrese una opción "))
    if op == 1: 
     return 55 
    elif op == 2:
     return 45
    elif op == 3:
     return 15
    else:   
        print("El precio del platillo es: 0")    
    return menuPrincipal()

def realizarPago(totalAdultos, totalNinos, saldoTarjeta, listaClaves):
    print("El saldo de la tarjeta es:", saldoTarjeta)
    tc=totalAdultos+totalNinos
    tca=print("Total comida de adultos", totalAdultos)
    tcn=print("Total de comidas de niños", totalNinos)
    TC=print("Total de consumo: ", tc)
    pp=int(input("Introduce el porcentaje de propina "))
    tp=pp*tc/100
    print("Total propina: ", tp)
    tg=tp+tc
    print("Total general: ", tg)
    if saldoTarjeta<tg:
       print("Recarga tu tarjeta de prepago")
    elif saldoTarjeta>tg:
        compruebaClave(listaClaves)
        print("Gracias por su compra")
        if tc>500 and pp>10:
            print("Puede gozar de internet gratis por cortesía de la casa")
    a=saldoTarjeta-tg
    print("El saldo nuevo es: ", a)
    return menuPrincipal()

def recargaTarjeta():
    print("1.$100.00")
    print("2.$250.00")
    print("3.$500.00")
    saldo=int(input("Introduce la opción de la cantidad que desea recargar "))
    if saldo==1:
       op1=saldoTarjeta+100
       print("El nuevo saldo es: ", op1)
    elif saldo==2:
         op2=saldoTarjeta+250
         print("El nuevo saldo es: ", op2)
    elif saldo==3:
         op3=saldoTarjeta+500
         print("Recarga de:", 500)
         print("El nuevo saldo es: ", op3)
         global cont
         cont+=1
         print (cont)
         if (cont==3):
             print("Se te abonaron $100.00 gratis")
             print("Tu nuevo saldo es", op3+100)
             cont = 0
    else:
          print("Opción no válida")
    return saldo

op = 0
totalAdultos = 0
totalNinos = 0
saldoTarjeta = 1000
while op != 5:
   op= menuPrincipal()
   if op == 1:
    precio = menuAdulto()
    totalAdultos = totalAdultos + precio
   elif op == 2:
    precio = menuNiño()
    totalNinos = totalNinos + precio
   elif op == 3:
    print("Realizar pago")
    saldo=realizarPago(totalAdultos, totalNinos, saldoTarjeta, listaClaves)
   elif op == 4:
    print("Recarga de tarjeta")
    ns= recargaTarjeta()
   elif op == 5:
       break
   else:
    print("Opción inválida")
    

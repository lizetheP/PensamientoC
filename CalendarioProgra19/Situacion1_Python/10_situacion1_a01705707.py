c=0

saldoTarjeta = 1000
recargaTarjeta = 0
nuevoSaldo = 0

p1 = 150
p2 = 120
p3 = 110

p4 = 110
p5 = 90
p6 = 110

Exit = 0

totalPropina = 0
totalComAdultos = 0
totalComNinos = 0
totalGeneral = 0
contRec500 = 0

listaClaves = ["1", "1234", "5678", "9123", "3456", "7891", "8913"]


def menu():
    print("1. Menú de adulto ")
    print("2. Menú de niño ")
    print("3. Realizar pago ")
    print("4. Recarga de tarjeta ")
    print("5. Salir")
    opcion = int(input("Introduce una opción: "))
    return opcion

def menuAdulto ():
    global p1
    global p2
    global p3
    p = 0
    res = int(input("Seleccione una opción: "))
    if res == 1:
        print ('El precio del menu es $150.00')
        con = input(" ¿Confirmar? SI/NO: ")
        if con.lower() == "si":
            p = float(p+p1)
            return p
        elif con.lower() == "no":
            Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
        else:
            print("Intente otra vez")
        Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
    elif res == 2:
        print ('El precio del menu es $120.00')
        con = input("¿Confirmar? SI/NO: ")
        if con.lower() == "si":
            p = float(p+p2)
            return p
        elif con.lower() == "no":
            Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para salir del programa: ")
        else:
            print("Intente otra vez ")
        Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
    elif res == 3:
        print ('El precio del menu es $110.00')
        con = input(('¿Confirmar? SI/NO: '))
        if con.lower() == 'si':
            p = float(p+p3)
            return p
        elif con.lower() == 'no':
            Exit = input ('Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ')
        else :
            print ('Intente otra vez')
        Exit = input ('Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ')
    elif res == 4:
        Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
    else:
        print ("0")

def menuNino ():
    global p4
    global p5
    global p6
    p = 0
    res = int(input("Seleccione una opción: "))
    if res == 1:
        print ('El precio del menu es $110.00')
        con = input(" ¿Confirmar? SI/NO: ")
        if con.lower() == "si":
            p = float(p+p4)
            return p
        elif con.lower() == "no":
            Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
        else:
            print("Intente otra vez")
        Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
    elif res == 2:
        print ('El precio del menu es $90.00')
        con = input("¿Confirmar? SI/NO: ")
        if con.lower() == "si":
            p = float(p+p5)
            return p
        elif con.lower() == "no":
            Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para salir del programa: ")
        else:
            print("Intente otra vez ")
        Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
    elif res == 3:
        print ('El precio del menu es $110.00')
        con = input(('¿Confirmar? SI/NO: '))
        if con.lower() == 'si':
            p = float(p+p6)
            return p
        elif con.lower() == 'no':
            Exit = input ('Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ')
        else :
            print ('Intente otra vez')
        Exit = input ('Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ')
    elif res == 4:
        Exit = input("Presione ENTER para regresar al Menú Principal\nPresione 1 para SALIR del programa: ")
    else:
        print ("0")

def recargaTarjeta (SaldoTarjeta):
    global contRec500
    global saldoTarjeta
    print("El saldo de su tarjeta es: ", saldoTarjeta)
    print("1. $100")
    print("2. $250")
    print("3. $500")
    print("4. Salir")
    recarga = (input("Introduce una opción: "))
    if (recarga == "1"):
        saldoTarjeta += 100
        print("El nuevo saldo es:", saldoTarjeta)
    elif (recarga == "2"):
        saldoTarjeta += 250
        print("El nuevo saldo es:", saldoTarjeta)
    elif (recarga == "3"):
        if contRec500 >= 2:
             saldoTarjeta += 600
             print("El nuevo saldo por 3 recargas de 500 es de 100 pesos más\n El nuevo saldo +100 es:", saldoTarjeta)
        else:
            saldoTarjeta += 500
            contRec500 += 1
            print("El nuevo saldo es:", saldoTarjeta)
    elif op == 4:
        Exit
    elif (recarga < "3"):
        print("Opción inválida")


        

def realizarPagos(totalComAdultos, totalComNinos, saldoTarjeta, listaClaves):
    global tarjeta
    totalConsumo = totalComAdultos + totalComNinos
    print('Consumo menú adultos:', totalComAdultos,'\nConsumo menú niños:', totalComNinos, "\nTotal de consumo:", totalConsumo)
    propina_Y_N = input("¿Desea dejar propina? SI/NO: ")
    totalPropina = 0
    totalGeneral = totalConsumo 
    if (propina_Y_N.lower() == 'si'):
        propina = float(input('¿Qué porcentaje de propina desea dejar? '))
        totalPropina = totalConsumo*propina/100
        print('La propina es de: ', totalPropina)
        totalGeneral = totalConsumo + totalPropina
    print("\nResumen General\n\nConsumo " + str(totalComAdultos)+ " en menú adultos,\nConsumo " + str(totalComNinos) + " en menú niños")
    print("El total a pagar: ", totalGeneral, "que incluye una propina de", totalPropina)
    saldoTarjeta = 1000
    if totalGeneral > saldoTarjeta :
        print('Su saldo es insuficiente\nSu saldo actual es de ',saldoTarjeta,'\nPor favor recargue su tarjeta')
    else:
        saldoTarjeta = saldoTarjeta- totalGeneral
        if (totalGeneral > 500 and totalPropina > 10):
            print('Querido usuario, usted puede gozar de internet gratis por cortesía de la casa')
    tip_aut = str(input('Digite su clave para autorizar el uso de la tarjeta: '))
    if tip_aut in listaClaves:
        print('Su saldo actual es de: $',saldoTarjeta)
        print('¡Gracias por su compra!\n')

def compruebaClave(listaClaves):
    clave = str(input("Introduce tu clave: "))
    while not(clave in listaClaves):
        clave = str(input("Intenta de nuevo, introduce tu clave de acceso: "))
    print("Bienvenido")

compruebaClave(listaClaves)

while (Exit != '1'):
    print ("1. Menú adultos")
    print ('2. Menú niños')
    print ("3. Realizar pagos")
    print ("4. Recargar tarjeta")
    print ("5. Salir")
    op= int(input('Escriba el número de opción: '))
    
    if op == 1 :
        print("Menú de adulto ")
        print("    1. Hamburguesa $150 ")
        print("    2. Ensalada $120 ")
        print("    3. Tacos $110 ")
        totalComAdultos += menuAdulto()
        
    elif op == 2 :
        print("Menú de niños ")
        print("    1. Alitas $110 ")
        print("    2. Hotdog $90 ")
        print("    3. Salchipapa $110 ")
        totalComNinos += menuNino()
    
    elif op == 3:
        print("Realizar pago ")
        realizarPagos(totalComAdultos, totalComNinos, saldoTarjeta, listaClaves)      
    
    elif op == 4 :
        print("Recargar tarjeta")
        recargaTarjeta (saldoTarjeta)
        
    elif op == 5:
        print("Salir")
        break
    
    else:
        print("Opcion invalida")
        
    
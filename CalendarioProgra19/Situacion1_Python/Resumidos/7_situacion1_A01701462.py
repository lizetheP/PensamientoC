milanesa = 70
salchicha = 40
pastor = 80
hambur = 50
pollo = 30
helado = 40
contA = 0
contN = 0
opcion = 0
saldoI = 1000
contRec500 = 0
contrasena = "1234", "4321", "6789", "9876", "1928"

def compruebaClave(listaClaves):
    clave = str(input("Introducir clave: "))
    while not(clave in listaClaves):
        clave = str(input("Clave incorrecta, introduce nuevamente la clave"))
    print("Bienvenido")
        
listaClaves = ["1234", "4321", "6789", "9876", "1928"]
compruebaClave(listaClaves)

def menuPrincipal():
    print("1. Menu de adulto")
    print("2. Menu de niño")
    print("3. Realizar pago")
    print("4. Recarga de tarjeta")
    print("5. Salir")
    opcion = int(input("Introduce una opcion: "))
    return opcion

op = 0
while opcion != 5:
    op = menuPrincipal()
    if op == 1:
        print("Menu de adulto")
    elif op == 2:
        print("Menu de niño")
    elif op == 3:
        print("Realizar pago")
    elif op == 4:
        print("Recarga de tarjeta")
    elif op == 5:
        break
else:
    print("Opción invalida")

def menuAdulto():
    op = 0
    global contA
    while op == 0:
        print("Menú de adulto")
        print("1. Torta milanesa $70")
        print("2. Torta salchicha $40")
        print("3. Torta pastor $80")
        comA = int(input("Seleccionar opcion del menu: "))
        if comA == 1:
            contA = contA + milanesa
        elif comA == 2:
            contA = contA + salchicha
        elif comA == 3:
            contA = contA + pastor


def menuNino():
    op = 0
    global contN
    while op == 0:
        print("Menú de niños")
        print("1. Hamburguesa $50")
        print("2. Pollo $30")
        print("3. Helado $40")
        comN = int(input("Seleccionar opcion del menu: "))
        if comN == 1:
            contN = contN + hambur
        elif comN == 2:
            contN = contN + pollo
        elif comN == 3:
            contN = contN + helado


def recargaTarjeta():
    op = 0
    contadormovimientos = 0
    bono = 100
    global saldoI
    global contRec500
    while reset == 0:
        print("1. $100")
        print("2. $250")
        print("3. $500")
        print("4. Salir")
        recar = int(input("Seleccione el monto a recargar: "))
        if recar == 1:
            saldoI += 100
            contRec500 += 100
        elif recar == 2:
            saldoI += contRec500
            contRec500 += 250
        elif recar == 3:
            saldoI += 500
            contRec500 += 500
            contadormovimientos += 1
        if contadormovimientos == 3:
            saldoI += bono
            print("Usted ha recibido $100 por haber recargado $1,500 o mas.")
            print("Usted ha recargado $", contRec500, "mas $", bono, "de bonificacion.")
        print("Su nuevo saldo en la tarjeta es de $", saldoI)
        if recar == 4:
            menuprincipal()


def realizarPago():
    print("El total de la cuenta de adultos es: $", contA)
    print("El total de la cuenta de niños es: $", contN)
    acum = contA + contN
    print("El total de la cuenta es: $", acum)
    print("1. sí")
    print("2. no")
    aceptar = int(input("¿Desea dejar propina?: "))
    if aceptar == 1:
        prop = int(input("¿Qué porcentaje de propina desea dejar? (Mayor a 9%): "))
        while prop >= 10:
            j = (prop * acum) / 100
            print("La propina es de: $", j)
            print("Se requiere de firma para descontar la propina")
            print("Por favor introduzca su contraseña")
            if str(input("Autorizar: ")) == contrasena:
                total = acum + j
                k = saldoI - total
                if total > 500 and aceptar == 1:
                    if saldoI <= 0 or total > saldoI:
                        print("El saldo de la tarjeta es insuficiente")
                        print("Necesita recargar su tarjeta")
                        print("Seleccione el monto a recargar")
                        recargo()
                    else:
                        print("Su nuevo saldo en la tarjeta es de: $", k)
                        print("Gracias por su compra.")
                        print("Puede gozar de internet gratis por parte de la casa.")
                        final()
                else:
                    print("Un gusto atenderle.")
            else:
                print("Contraseña incorrecta. Inténtelo de nuevo.")
                realizarpago()
        if prop < 10:
            print("Por favor introduzca un porcentaje mayor a 9%")
            realizarpago()
    else:
        total = acum
        if aceptar == 2:
            if saldoI <= 0 or total > saldoI:
                print("El saldo de la tarjeta es insuficiente")
                print("Necesita recargar su tarjeta")
                print("Seleccione el monto a recargar")
                recargo()
            else:
                k = (saldoI - acum)
                print("Se requiere de firma para autorizar el pago")
                print("Por favor introduzca su contraseña")
                if str(input("Autorizar: ")) == contrasena:
                    print("Su nuevo saldo en la tarjeta es de: $", k)
                    print("Gracias por su compra")
                    final()


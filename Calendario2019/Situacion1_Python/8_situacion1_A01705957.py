# Andrea Castrezana Gonzalez 
# Pablo Segura
# Pablo AlvareZ
# Situacion Problema 1
# 26/Novimebre/2019
# A01706544
# A01706160
# A01705957

#VARIABLES GLOBALES 
contRec500= 0
listaClave=["12345", "23456","34567","45678","56789"]
saldoTarjeta=1000



#MenuPrincipal: Menu Principal de la Funcion
def menuPrincipal():
    print("1. Menu Adulto")
    print("2. Menu Niño")
    print("3. Realiza Pago")
    print("4. Recarga Tarjeta")
    print("5. Salir")
    opcion=int(input("Introduce una opción: "))
    return opcion

#compruebaClave
def compruebaClave():
  i = True
  while i:
    clave=str(input("Introduce tu clave : "))
    if clave not in listaClave:
      print("Clave incorrecta")
      i = True
    else: 
      print("Tu clave es CORRECTA, BIENVENIDO: ")
      i = False
 
  
  
#menuAdulto
def menuAdulto():
  print("1.Pollo")
  print("2.Ribeye")
  print("3.Pasta")
  opcion=int(input("Elige una opción"))
  
  if opcion== 1:
    print("El precio del menu es: $180")
  elif opcion==2:
    print("El precio del menu es: $350")
  elif opcion==3:
    print("El precio del menu es: $270")
  else: 
    print("Opción no valida")

#menuNiño
def menuNiño():
  print("1.Milanesa de Pollo")
  print("2.Dedos de queso")
  print("3.NuggetsDePollo")
  opcion=int(input("Elige una Opción"))
  if opcion==1:
    print("El precio del menu es: $80")
  elif opcion==2:
    print("El precio del menu es: $50")
  elif opcion==3:
    print("El precio del menu es: $40")
  else:
    print("Opción no valida")

#realizaPago
def realizaPago(totalComAdulto,totalComNiño,saldoTarjeta):
    global saldoTarjeta
    totalConsumo=totalComAdulto+totalComNiño
    print("El total del consumo de adulto es: ",totalComAdulto)
    print("El total del consumo de niños es:",totalComNiño)
    print("El total del consumo es:", totalConsumo)

    propina=int(input("¿Qué porcentaje de propina deseas dar?(10%,15%,20%) Escribe el porcentaje en numero entero"))
    nuevoTotal=totalConsumo * (propina/100)+
    print("Tu nuevo total es:", nuevoTotal)
    if saldoTarjeta < nuevoTotal:
      print("Recarga tu tarjeta de prepago")
      return saldoTarjeta
    elif saldoTarjeta > nuevoTotal:
      saldoTarjeta = saldoTarjeta - nuevoTotal
      print("Gracias por su compra")
      if nuevoTotal>500 and propina>10:
        print("puede gozar de Internet gratis por cortesía de la casa")
    return saldoTarjeta

#recargarTarjeta 
def recargarTarjeta():
  global saldoTarjeta
  print("Tu saldo actual es: $ ", saldoTarjeta)
  print("¿Cuánto desea recargar?")
  print("1. $100")
  print("2. $250")
  print("3. $500")
  opcion= int(input("Elige una opción"))
  if opcion==1:
    saldoTarjeta = saldoTarjeta + 100
    print("Tu nuevo saldo es: ",saldoTarjeta)
  elif opcion==2:
    saldoTarjeta = saldoTarjeta + 250
    print("Tu nuevo saldo es: ",saldoTarjeta)
  elif opcion==3:
    saldoTarjeta = saldoTarjeta + 500
    #Cuenta cuantas veces se ha hecho una recarga de 500
    contRec500+1 
    #Si se han hecho mas de 3 recargas de 500, suma 100 pesos al saldo actual de la cuenta
    if contRec500 >= 3:
      print("Felicidades has hecho mas de 3 recargas, recibiras gratis: $100 ")
      saldoTarjeta = saldoTarjeta + 100
    print("Tu nuevo saldo es: ",saldoTarjeta)


  else:
    print("Opción inválida")
    return saldoTarjeta


# Funcion main 

compruebaClave()
op=menuPrincipal()
while op != 5:
  op=menuPrincipal()
  if op==1:
          menuAdulto()
  elif op==2:
          menuNiño()    
  elif op==3:
      comidaAdulto=int(input("Ingresa el total de comida de adulto: "))
      comidaNiño=int(input("Ingresa el total de comida de niño: "))
      saldoT=int(input("Ingresa tu saldo de la tarjeta: "))
      realizaPago(comidaAdulto,comidaNiño,saldoT)
  elif op==4:
      recargarTarjeta()
  elif op==5:
      print("gracias")
  else:
      print("Opción inválida")
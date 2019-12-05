#Situacion problema 1
#Vacaciones con tarjeta de prepago
#A01702379 David Dorantes Olmedo
#A01702382 Valeria Barajas


#Variables
Recarga500= 0
listaClaves=["ABC000","ABC111","ABC222","ABC333","ABC123"]
saldoT=1000


#MenuPrincipal
def MenuPrincipal():
  print("1. Menú Niños")
  print("2. Menú Adultos")
  print("3. Pagar")
  print("4. Recargar saldo en tarjeta")
  print("5. Salir")
  op=int(input("Elige una opción"))
  return op


#compruebaClave
def compruebaClave():
  i = True
  while i:
    clave=str(input("Introduce la clave : "))
    if clave not in listaClaves:
      print("Contraseña incorrecta")
      i = True
    else: 
      print("Contraseña correcta, bienvenido: ")
      i = False


#MenuNiños
def MenuNiños():
  print("1. Nuggets+Papas a la francesa")
  print("2. Pasta+Minihamburguesa")
  print("3. Arros+Pechuga asada")
  op=int(input("Elige una opción"))
        
  if op==1:
   print("El precio del platillo es $100")
  elif op==2:
   print("El precio del platillo es $120")
  elif op==3:
   print("El precio del platillo es $100")
  else:
   print("Opción inválida")


#MenuAdultos
def MenuAdultos():
  print("1. Lasagna+Ensalada")
  print("2. Pizza+Ensalada")
  print("3. Papa horneada+Rib eye")
  op=int(input("Elige una opción"))

  if op==1:
   print("El precio del platillo es $150")
  elif op==2:
   print("El precio del platillo es $160")
  elif op==3:
   print("El precio del platillo es $190")
  else:
   print("Opción inválida")


#RealizarPago
def RealizarPago(TotNiño,TotAdulto,saldoTarjeta):
  global saldoT
  totalConsumo=TotAdulto+TotNiño
  print("El total del consumo del niño es: ",TotNiño)
  print("El todal del consumo del adulto es: ",TotAdulto)
  print("El total del consumo es: ", totalConsumo)

  propina=int(input("¿Cuánto porcentaje de propina deseas dejar? 10%, 15%, 20%? Escribe el porcentaje en entero"))
  nuevoTot=totalConsumo * (propina/100) + totalConsumo
  print("Tu nuevo total es: ", nuevoTot)
  if saldoT<nuevoTot:
    print("Recarga tu tarjeta")
    return saldoT
  elif saldoT>nuevoTot:
    saldoT= saldoT - nuevoTot
    print("¡Gracias!")
    if nuevoTot>500 and propina>10:
      print("¡Enhorabuena! Tiene internet gratis de cortesía")
      return saldoT


#recargaT
def recargaT():
  global saldoT
  print("Tu saldo actual es: ", saldoT)
  print("Cantidad a recargar: ")
  print ("1. $100")
  print ("2. $250")
  print ("3. $500")
  op=int(input("Elige una opción"))
  if op==1:
   saldoT=saldoT + 100
   print("Tu nuevo saldo es: ",saldoT)
  elif op==2:
     saldoT=saldoT + 250
     print("Tu nuevo saldo es: ",saldoT)
  elif op==3:
     saldoT=saldoT + 500
     print("Tu nuevo saldo es: ",saldoT)

     #numero de recargas de 500
     Recarga500+1
     #Con más de 3 recargas, agrega $100 a su saldo actual
     if Recarga500 >=3:
      print("Hiciste más de 3 recargas, tienes $100 gratis")
      saldoT=saldoT+100
      print("Tu saldo ahora es de: ", saldoT)
     else:
      print("Opción inválida")
      return saldoT


# Funcion main 

compruebaClave()
op=MenuPrincipal()
while op != 5:
  op=MenuPrincipal()
  if op==1:
          MenuNiños()
  elif op==2:
          MenuAdultos()    
  elif op==3:
      comidaAdulto=int(input("Ingresa el total de comida de adulto: "))
      comidaNiño=int(input("Ingresa el total de comida de niño: "))
      saldoTarjeta=int(input("Ingresa tu saldo de la tarjeta: "))
      RealizarPago(comidaAdulto,comidaNiño,saldoTarjeta)
  elif op==4:
      recargaT()
  elif op==5:
      print("Hasta pronto! gracias!")
  else:
      print("Opción inválida")
      


  




  

  


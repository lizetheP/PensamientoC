def evaluax(x):
  if x > 0:
    res = x ** 2
  else:
    res = x * 4
  return res

def menu():
  print("1. Evalua x")
  print("2. Salir")
  
def main():
  menu()
  opcion = int(input("Escoge una opción "))
  if opcion == 1:
    num = float(input("Dame un número "))
    res = evaluax(num)
    print("El resultado es %.2f" % res)
  elif opcion == 2:
    print("Adios")
  else:
    print("ERROR OPCION INVALIDA")

main()
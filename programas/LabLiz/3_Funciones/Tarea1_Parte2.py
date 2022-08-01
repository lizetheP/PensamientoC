distancia = 10.0
if distancia >= 50.0:
    print("El objeto esta lejos")
elif distancia >= 10.0 and distancia < 50.0:
    print("El objeto esta cerca.")
elif distancia > 0.0 and distancia < 10:
    print("El objeto esta muy cerca.")
elif distancia == 0.0:
  print("Colision")
else:
  print("Error en la distancia.")
  
  
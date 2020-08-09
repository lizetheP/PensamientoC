def creaMatriz(renglones, columnas):
    matriz = []
    for i in range(0, renglones):
        matriz.append([])
        for j in range(0, columnas):
            valor = int(input())
            matriz[i].append(valor)  # matriz[i].insert(j, valor)
    return matriz

def creaMatriz2(renglones, columnas):
    matriz =  [ ]
    for i in range(0, renglones):
        matriz.insert(i, [ ] )
        for j in range(0, columnas):
            valor = int(input("Introduce un valor: "))
            matriz[i].insert(j, valor)
    return matriz

def sumaDiagonal(matriz):
    acum = 0
    columnas = len(matriz)
    renglones = len(matriz[0])
    if columnas == renglones:
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                if i==j:
                    acum = acum + matriz[i][j]
        return acum
    else:
        return False

def sumaDiagonal_Inversa(matriz):
    acum = 0
    renglones = len(matriz)
    columnas = len(matriz[0])
    if renglones == columnas:
        columna = len(matriz[0])-1
        for i in range(0, len(matriz)):
            acum = acum + matriz[i][columna]
            columna = columna-1
        return acum
    else:
        return False
    
def encuentraGrupo(matriz, cadena):
    acum = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if cadena == matriz[i][j]:
                return matriz[i]
                break
    return "el nombre no es epico"

nombresEpicos= [ ["Naofumi", "Filo", "Raphtalia"], ["Rand Al'thor", "Perrin Arabaya", "Mathrim Cauldron", "Egwene Al'vere", "Nynaieve Al'mere"], ["Lithany of Fury", "Macragge's Honour", "Vengeful Spirit", "Harbinger of Doom", "Chronicle of Ashes"], ["Cloud Strife", "Sephiroth", "Vincent Valentine", "Zack Fair", "Aerith Gainsborough", "Tifa Lockhart", "Barret Wallace", "Yuffie Kisaragi"], ["Cormyr", "WestGate", "Suzeil", "Menzoberranzan", "Waterdeep"], ["Atlas", "Dectective Comics", "Dark Horse", "Image"] ]
opcion = int(input())
if opcion == 1:
    r = int(input())
    c = int(input())
    matriz = creaMatriz2(r, c)
    print(matriz)
elif opcion == 2:
    r = int(input())
    c = int(input())
    matriz = creaMatriz(r, c)
    res = sumaDiagonal(matriz)
    print(res)
elif opcion == 3:
    r = int(input())
    c = int(input())
    matriz = creaMatriz(r, c)
    res = sumaDiagonal_Inversa(matriz)
    print(res)
elif opcion == 4:
    cadena = str(input())
    lista = encuentraGrupo(nombresEpicos, cadena)
    print(lista)
else:
    print("Opción inválida")
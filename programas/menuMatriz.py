def creaMatriz(renglones, columnas):
    matriz = []
    for i in range(0, renglones):
        matriz.append([])
        for j in range(0, columnas):
            matriz[i].append(5)  
    return matriz
    
r = int(input("Introduce el número de renglones: "))
c = int(input("Introduce el número de columnas: ")) 
M = creaMatriz(r,c)
print(M)


"""
continua = True
while continua:
    menu()
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        
    elif opcion == 2:
    
    elif opcion == 3:
    
    elif opcion == 4:
        print("\n Adios")
        continua = False
    else:
        print("\n ERROR OPCION INVALIDA")
        continua = False"""
        
        
        
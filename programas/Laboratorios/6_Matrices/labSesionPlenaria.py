def multiplicaColumna(M, col, valor):
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            if j == col:
                M[i][j] = M[i][j]*valor

def multiplicaColumna(M, col, valor):
    for i in range(0, len(M)):
        M[i][col] = M[i][col]*valor
        
def posicionPares(M):
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            if M[i][j]%2 == 0:
                print("El valor %d esta en la posicion %d, %d"%(M[i][j], i, j))
                
                
                
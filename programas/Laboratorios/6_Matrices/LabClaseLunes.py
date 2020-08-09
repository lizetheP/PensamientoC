def multiplicaColumna(M, col, num):
    for i in range(0, len(M)):
        for j in range(0, len(M[i])):
            if j==col:
                M[i][j] = M[i][j] * num
            
def multiplicaColumna(M, col, num):
    for i in range(0, len(M)):
        M[i][col] = M[i][col] * num
import random

M1 = [[1,2,3],[3,1,2],[4,4,5]]
M2 = [[1,3,3],[3,1,2],[4,4,5]]
M3 = [[1,4,4],[3,1,2],[4,4,5]]
MU = [['_','_','_'],['_','_','_'],['_','_','_']]
  
  0 1 2
0 1 _ _
1 _ 1 _
1 _ _ _

MU[x][y] = M[x][y]
MU[x2][y2] = M[x2][y2]

if MU[x][y] != MU[x2][y2]:
    MU[x][y] = '_'
    MU[x2][y2] = '_'
 
num = random.randint(1, 3)
if num == 1:
    M = M1
elif num == 2:
    M = M2
elif num == 3:
    M = M3

print(M)
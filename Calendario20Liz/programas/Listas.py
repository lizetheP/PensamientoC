import random
import math

def inicializaVector(A):
    for i in range(0,10):
        valor = random.randint(-50,51)
        A.insert(i, valor)

def imprimeVector(A):
    for i in range(0,10):
        print("A[", i, "] = ", A[i])
        
A=[]
inicializaVector(A)
imprimeVector(A)
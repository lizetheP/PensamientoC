def cuentaConsonantes(nombre):
    file=open(nombre,"r")
    cont = 0
    while True:
        letra = file.read(1) # Lee un caracter del archivo
        if (letra.isalpha() and letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u'):
            cont = cont + 1
        if not letra: # Si no es letra, es fin de archivo
            cont = cont -1
            break
    file.close()
    return cont

def uneArchivos(nombreO, nombreD):
    fileO=open(nombreO,"r")
    fileD=open(nombreD,"a")
    while True:
        letra = fileO.read(1) # Lee un caracter del archivo
        fileD.write(letra)
        if not letra: # Si no es letra, es fin de archivo
            break
    fileO.close()
    fileD.close()
   
nombreO = str(input("Introduce el nombre del archivo origen: "))
nombreD = str(input("Introduce el nombre del archivo destino: "))
uneArchivos(nombreO, nombreD)
ruta="nombreArchivo.txt"
archivo=open(ruta,"w+")
i = 1
while i<=5:
    frase = str(input("Introduce una frase: "))
    archivo.write(frase+"\n")
    i = i+1
archivo.seek(0)
print(archivo.read())
archivo.close()

def escribe5frases(nombre):
    file=open(nombre,"w+")
    i = 1
    while i<=5:
        frase = str(input("Introduce una frase: "))
        file.write(frase+"\n")
        i = i+1
    file.close()

nombre = str(input("Introduce el nombre del archive: "))
escribe5frases(nombre)

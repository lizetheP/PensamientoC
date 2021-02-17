def imprime4():
    letra = 's'
    num = 1
    while letra == 's' or letra == 'S':
        for i in range(4):
            print(num)
            num = num + 1
        letra = str(input("Deseas continuar: (S/N) "))

imprime4()
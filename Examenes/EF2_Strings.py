def cuenta_vocales(cadena):
    ca = 0
    ce = 0
    ci = 0
    co = 0
    cu = 0
    for i in range(len(cadena)):
        if cadena[i].lower() == 'a':
            ca = ca + 1
        elif cadena[i].lower() == 'e':
            ce = ce + 1
        elif cadena[i].lower() == 'i':
            ci = ci + 1
        elif cadena[i].lower() == 'o':
            co = co + 1
        elif cadena[i].lower() == 'u':
            cu = cu + 1
    print("Vocal a:", ca)
    print("Vocal e:", ce)
    print("Vocal i:", ci)
    print("Vocal o:", co)
    print("Vocal u:", cu)

def main():
    cadena = str(input("Introduce una cadena: "))
    cuenta_vocales(cadena)
    
main()
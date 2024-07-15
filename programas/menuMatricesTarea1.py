def main():
    continua = True
    r = int(input("Introduce el número de renglones: "))
    c = int(input("Introduce el número de columnas: ")) 
    m = creaMatriz(r, c)
    while continua == True:
        menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            imprime_matriz(m)
        elif opcion == 2:
            imprime_matriz(m)
            res = promedio_matriz(m)
            print("El promedio es %.1f" % res)
        elif opcion == 3:
            
        elif opcion == 4:
            imprime_matriz(m)
            posicion_impares(m)
        elif opcion == 5:
            
        elif opcion == 6:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()








        
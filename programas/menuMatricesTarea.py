def main():
    continua = True
    r = int(input("Introduce el número de renglones: "))
    c = int(input("Introduce el número de columnas: ")) 
    m = creaMatriz(r, c)
    while continua == True:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            imprime_matriz(m)
        elif opcion == 2:
            imprime_matriz(m)
            res = promedio_matriz(m)
            print("El promedio es %.1f" % res)
        elif opcion == 3:
            # COMPLETAR
        elif opcion == 4:
            imprime_matriz(m)
            posicion_pares(m)
        elif opcion == 5:
            # COMPLETAR
        elif opcion == 6:
            print("Adiós")
            continua = False
        else:
            print("Error opción inválida")
        
main()




        
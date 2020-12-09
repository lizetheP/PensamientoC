Algoritmo: Carbohidratos
var
  entero: m, a
inicio
  Escribir ("Dame las moleculas")
  Leer(m)
  si (m <= 0)
     Escribir(""El número de moléculas es incorrecto")
  sino
    En caso_de (m)
       1:  Escribir("MOnosacaridos")
           Escribir ("Dame los atomos")
           Leer(a)
           En caso_de(a)
              3: Escribir("Thosa")
              4: Escribir("Tetrosa")
              5: Escribir("Ribosa")
              6: Escribir("Glucosa o Frutosa")
              default: Escribir("El número de átomos es incorrecto")
           fin_caso
       2:  Escribir("Disacaridos")
       3:
       4:
       5:
       6:
       7:
       8:
       9:
       10:
           Escribir("Oligosacaridos")
       default: Escribir("Polisacaridos")
   fin_caso

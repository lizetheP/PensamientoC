#include <stdio.h>
#include <stdlib.h>

//Celsius = 5 / 9 ( Farenheit – 32)

/*Algoritmo : Conversión de grados farenheit a celsius
variables
      float  f, c
inicio
      Escribir("Dame los grados farenheit")
      leer(f)
      c = 5 / 9 ( f – 32)
      Escribir(c) */

void main()
{
    float  celsius, farenheit;

  printf("\n Dame los grados Farenheit: ");
  scanf("%f",  &farenheit);
  celsius = 5.0 / 9 * ( farenheit - 32);
  printf("\n %.2f grados farenheit equivalen a %.2f grados celsius",  farenheit, celsius);

  printf("\n\n\n");
  system("PAUSE");
}





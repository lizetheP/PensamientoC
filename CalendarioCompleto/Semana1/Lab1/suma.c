#include <stdio.h>
#include <stdlib.h>
/*
Algoritmo: Grados farenheit
var
   real: farenheit, celsius
inicia
   Escribir(Dame los grados farenheit)
   leer(farenheit)
   celsius = 5/9(farenheit-32)
   Escribir(celsius)
fin*/


int main()
{
   float farenheit, celsius;

   printf("\n Introduce los grados farenheit: ");
   scanf("%f", &farenheit);
   celsius = 5.0/9*(farenheit-32);
   printf("\n %.2f farenheit equivalen %.2f celsius", farenheit, celsius);

    printf("\n\n");
    system("PAUSE");
}

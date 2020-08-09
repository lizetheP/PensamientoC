#include <stdio.h>
#include <stdlib.h>

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

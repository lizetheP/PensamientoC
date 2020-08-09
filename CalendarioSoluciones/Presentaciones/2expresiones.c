#include <stdio.h>
#include <stdlib.h>

void main()
{
float x, y, z;

x = 5 * 7 * (6 / 2) % 4 * 3 - 10;
y = ((13 % 6 * 2/4) + (1+6*3-2)) - ((5.0/2));
z = (2 * 3) + (6 - 2 * 5 / 2 - 4 * 3 / 2.0);

printf("\n 1. El valor de x es %f", x);
printf("\n 2. El valor de y es %f", y);
printf("\n 3. El valor de z es %f", z);
if ((4>=7*3+2 && 8 > 3 || 5 > 6) && (7 * 3 < 5 + 12 * 2 ))
    printf("\n 4. Verdadero");
else
    printf("\n 4. Falso");

if ((7 > 3 && 5 <=10) || (5>=10 && 6<20))
    printf("\n 5. Verdadero");
else
    printf("\n 5. Falso");
}

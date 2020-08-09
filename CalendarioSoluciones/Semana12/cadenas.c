#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int cuantosCaracteres(char cadena[50])
{
    int i=0, cont = 0;
    while (cadena[i] != '\0')
    {
        if (cadena[i] != ' ')
            cont++;
        i++;
    }
    return cont;
}

int cuantasRepeticiones(char cadena[50], char letra)
{   int i=0, cont = 0;
    while (cadena[i] != '\0')
    {
        if (toupper(cadena[i]) == toupper(letra)) //if (tolower(cadena[i]) == tolower(letra))
            cont++;
        i++;
    }
    return cont;
}

void main()
{ char A[50], let;
  int res;
  printf("\n Introduce una frase: ");
  fflush(stdin);
  gets(A);
  printf("\n Introduce una letra: ");
  fflush(stdin);
  scanf("%c", &let);
  res = cuantasRepeticiones(A, let);
  printf("\n La frase tiene %i caracteres %c", res, let);
  printf("\n\n");
  system("PAUSE");
}

// Aimee Sophia

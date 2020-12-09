#include <stdio.h>
#include <stdlib.h>

void llena(int A[10])
{   int i;

    for (i=0; i<10; i++)
    {
        A[i] = i;
     }
}

void mueveVectorIzquierda(int A[10])
{   int i, temp;
    temp = A[0];
    for (i=0; i<9; i++)
    {
        A[i] = A[i+1];
     }
     A[i] = temp;

}

void imprime(int A[10])
{   int i;
    for (i=0; i<10; i++)
    {
        printf("%i ", A[i]);
     }
}

int main()
{
   int A[10];

   llena(A);
   imprime(A);
   mueveVectorIzquierda(A);
   printf("\n");
   imprime(A);

   printf("\n\n");
   system("PAUSE");
}

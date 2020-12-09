#include <stdio.h>
#include <stdlib.h>

#define ren 3
#define col 3

void iniciaMatriz(int M[ren][col])
{
  int i, j;
  for (i=0; i<ren; i++)
  {
     for (j=0; j<col ; j++)
     {
       M[i][j] = 5;
     }
  }
}

void iniciaMatriz2(int M[ren][col])
{
  int i, j, num=1;
  for (i=0; i<ren; i++)
  {
     for (j=0; j<col ; j++)
     {
       M[i][j] = num;
       num++;
     }
  }
}
void imprimeMatriz(int M[ren][col])
{
  int i, j;
  for (i=0; i<ren; i++)
  {
     for (j=0; j<col; j++)
     {
       printf("%3i", M[i][j]);
     }
     printf("\n");
  }
}

void sumaMatriz(int A[ren][col], int B[ren][col], int C[ren][col])
{
  int i, j;
  for (i=0; i<ren; i++)
  {
     for (j=0; j<col ; j++)
     {
        C[i][j] = A[i][j] + B[i][j];
     }
  }
}

void main()
{
  int M1[ren][col], M2[ren][col], M3[ren][col];

  printf("\n");

  iniciaMatriz(M1);
  imprimeMatriz(M1);

  printf("\n");

  iniciaMatriz2(M2);
  imprimeMatriz(M2);

  printf("\n");

  sumaMatriz(M1, M2, M3);
  imprimeMatriz(M3);

  printf("\n\n");
  system("PAUSE");
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void factoresDe(int n)
{   int i;
    for (i=1; i<n; i++)
    {
      if (n%i == 0)
         printf(" %i ", i);
    }
}

void secuenciaDescendente(int n)
{  int cont=0;
   printf("\n El valor inicial es %i ", n);
   while (n > 1)
   {
      if (n%2 == 0)
         n = n / 2;
      else
         n = n*3 + 1;
      printf("\n El siguiente valor es %i", n);
      cont++;
   }
   printf("\n El valor final es %i", n);
   printf("\n El numero de pasos son %i", cont);
}

void interesCompuesto(float saldo, int meses, float interes)
{ int i;
  float saldoT, intereses;
  printf("\n         Saldo  Interes  Total");
  for (i=1; i<=meses; i++)
  {
    intereses = saldo * interes/100;
    saldoT = saldo + intereses;
    printf("\n Mes %i: %.0f + %.0f = %.0f", i, saldo,intereses,saldoT);
    saldo = saldoT;
  }
}

void llenaVector(int A[10])
{ int i;
  srand(time(NULL));
  for (i=0; i<10; i++)
  {
      A[i] = rand()%201-100;
  }
}

void imprimeVector(int A[10])
{ int i;
  for (i=0; i<10; i++)
  {
    printf("\n A[%i] = %i", i, A[i]);
  }
}

void menu()
{
 printf("\n MENU \n");
 printf("\n A. Factores de un numero ");
 printf("\n B. Imprime secuencia descendente ");
 printf("\n C. Intereses Compuestos ");
 printf("\n D. Llena vector ");
 printf("\n E. Imprime vector ");
 printf("\n S. Salir ");
}

int main()
{
char opcion;
int num, meses, A[10];
float interes, saldo;
do
{
 menu();
 printf("\n Pulse la opcion deseada: ");
 fflush(stdin);
 scanf("%c", &opcion);
 switch(opcion)
 {
    case 'a':
    case 'A':
        printf("\n Introduce un numero positivo: ");
        scanf("%i", &num);
        if (num > 0)
            factoresDe(num);
        else
            printf("\n ERROR EL NUMERO DEBE SER POSITIVO");
    break;
    case 'b':
    case 'B':
        printf("\n Introduce un numero positivo: ");
        scanf("%i", &num);
        if (num > 0)
            secuenciaDescendente(num);
        else
            printf("\n ERROR EL NUMERO DEBE SER POSITIVO");
    break;
    case 'c':
    case 'C':
        printf("\n Introduce el saldo: ");
        scanf("%f", &saldo);
        printf("\n Introduce los meses: ");
        scanf("%i", &meses);
        printf("\n Introduce el interes: ");
        scanf("%f", &interes);
        interesCompuesto(saldo, meses, interes);
    break;
    case 'd':
    case 'D':
        llenaVector(A);
        printf("\n Vector inicializado!!!");
    break;
    case 'e':
    case 'E':
        imprimeVector(A);
    break;
    case 's':
    case 'S':
        _exit(0);
    break;
    default:
        printf("\n ERROR OPCION INVALIDA");
   }
   printf("\n\n");
   system("PAUSE");
   system("cls");
 }while (opcion != 's' && opcion != 'S');
}

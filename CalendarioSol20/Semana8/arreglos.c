#include <stdio.h>
#include <stdlib.h>

void inicializa (int A[10])
{    int i;
     for (i=0; i<10; i++)
            A[i] = i ;
}

void sumaDos (int A[10])
{    int i;
     for (i=0; i<10; i++)
            A[i] = A[i] + 2;
}

void imprime(int A[10])
{
  int i;
  for (i=0; i<10; i++)
  {
     printf("\n A[%i] =%i ", i, A[i]);
  }

}

void menu()
{
   printf("\n MENU \n ");
   printf("\n 1. Inicializa");
   printf("\n 2. Suma dos ");
   printf("\n 3. Imprime arreglo ");
   printf("\n 4. Salir \n");
}

void main()
{
 int A[10], opcion ;
 do
 {
   menu();
   printf("\n Dame una opcion: ");
   scanf("%i", &opcion);
   switch(opcion)
   {
       case 1:
            inicializa(A);
            printf("\n\n ARREGLO INICIALIZADO \n");
       break;
       case 2:
            sumaDos(A);
            printf("\n\n ARREGLO LE SUMO 2 \n");
       break;
       case 3:
            imprime(A);
       break;
       case 4:
           _exit(0);
       break;
       default:
          printf("\n OPCION INVALIDA");
   }
   printf("\n\n");
   system("PAUSE");
   system("cls");
 }while (opcion != 4);
}

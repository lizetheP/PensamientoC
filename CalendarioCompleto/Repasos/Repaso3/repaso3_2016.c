#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define REN 4
#define COL 6

void llenaMatriz(int M[REN][COL])
{
  int i, j, num=1;

  for (i=REN-1; i>=0; i--)
  {
      for (j=0; j < COL; j++)
      {
          M[i][j] = num;
          num++;
      }
  }
}

void llenaMatriz2(int M[REN][COL])
{
  int i, j, num=2;

  for (i=REN-1; i>=0; i--)
  {
      for (j=COL-1; j>=0; j--)
      {
          M[i][j] = num;
          num = num + 2;
      }
  }
}

void imprimeMatriz(int M[REN][COL])
{
  int i, j, num=1;

  for (i=0; i<REN; i++)
  {
      for (j=0; j < COL; j++)
      {
          printf("%3i", M[i][j]);
      }
      printf("\n");
  }
}

void escribeCadena(char frase[50], char ruta[50])
{  FILE *arch;
   int i=0;

   arch = fopen(ruta, "w");
   if (arch != NULL)
   {
    while (frase[i] != '\0')
    {
       if (frase[i]  != ' ')
       {
         fputc(toupper(frase[i]), arch);
       }
       i++;
    }
    fclose(arch);
   }
   else
     printf("\n ERROR EL ARCHIVO NO SE PUDO CREAR");
}

void copiaInvertido(char rutaO[50], char rutaD[50])
{  char letra;
   FILE *ori;
   FILE *des;

   ori = fopen(rutaO, "r");
   des = fopen(rutaD, "w");
   if (ori != NULL && des != NULL)
   {
       letra = fgetc(ori);
       while (letra != EOF)
       {
           if (letra >= 'A' && letra <= 'Z')
           {
               letra = tolower(letra);
           }
           else
             if (letra >= 'a' && letra <= 'z')
             {
                 letra = toupper(letra);
             }
           fputc(letra, des);
           letra = fgetc(ori);
       }
       fclose(ori);
       fclose(des);
   }
   else
     printf("\n ERROR ALGUN ARCHIVO NO SE PUDO ABRIR");
}

int main()
{
  int M[REN][COL], opcion;
  char frase[50], ruta[50], rutaO[50], rutaD[50];

  do
  {
    printf("\n 1. Llena matriz");
    printf("\n 2. Llena matriz2");
    printf("\n 3. Imprime matriz");
    printf("\n 4. Escribe cadena");
    printf("\n 5. Copia invertido");
    printf("\n 6. Salir");
    printf("\n Dame una opcion: ");
    scanf("%i", &opcion);
    printf("\n");
    switch(opcion)
    {
        case 1:
           llenaMatriz(M);
           imprimeMatriz(M);
        break;
        case 2:
           llenaMatriz2(M);
           imprimeMatriz(M);
        break;
        case 3:
           imprimeMatriz(M);
        break;
        case 4:
           printf("\n Dame una frase: ");
           fflush(stdin);
           gets(frase);
           printf("\n Dame la ruta: ");
           fflush(stdin);
           gets(ruta);
           escribeCadena(frase, ruta);
        break;
        case 5:
           printf("\n Dame la ruta origen: ");
           fflush(stdin);
           gets(rutaO);
           printf("\n Dame la ruta destino: ");
           fflush(stdin);
           gets(rutaD);
           copiaInvertido(rutaO, rutaD);
        break;
        case 6:
           _exit(0);
        break;
        default:
          printf("\n Opcion invalida");

    }
    printf("\n\n");
    system("PAUSE");
    system("CLS");

  }while (opcion != 6);

}

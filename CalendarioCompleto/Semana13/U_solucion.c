#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/*Algoritmo: Escribir 10 frases
1. Recibir como parametro ruta[50]
2. Declarar variables
     FILE : arch
     char : frase[100]
     entero : i
3. Abrir arch en modo escritura
4. Si arch existe
       for(i=1; i<=10; i++)
            Escribir("Dame una frase")
            Leer (frase)
            Escribir frase en arch
            Escribir salto de línea en arch
       cerrar(arch)
5. Sino
     Escribir ("ERROR")*/


void escribirEnArchivo (char ruta[50])
{ FILE *arch;
  char frase[100];
  int i;
  arch = fopen(ruta, "w");
  if (arch != NULL)
  {
       for(i=1; i<=10; i++)
       {
            printf("\n Dame una frase: ");
            fflush(stdin);
            gets(frase);
            fputs(frase, arch);
            fputc('\n', arch);
       }
       fclose(arch);
  }
  else
     printf("\n ERROR");
}

/*Algoritmo: Cuenta caracteres
1. Recibir como parametro ruta[50]
2. Declarar variables
     FILE : arch
     char : letra
     entero : cont = 0
3. Abrir arch en modo lectura
4. Si arch existe
       Leer letra de arch
       mientras letra no sea fin de archivo
          si letra es diferente de espacio en blanco y salto de línea
             cont++
          Leer letra de arch
       cerrar(arch)
5. Sino
     Escribir ("ERROR")
6. Regresar cont  */

int cuentaCaracteres(char ruta[50])
{
    FILE *arch;
    char letra;
    int cont = 0;
    arch = fopen(ruta, "r");
    if (arch != NULL)
    {
       letra = fgetc(arch);
       while (letra != EOF)
       {
          if (letra != ' ' && letra != '\n')
          {
              cont++;
          }
          letra = fgetc(arch);
       }
       fclose(arch);
    }
    else
      printf("\n ERROR");
    return cont;
}

/*Algoritmo: Copia archivo
1. Recibir como parametro rutaO[50], rutaD[50]
2. Declarar variables
     FILE : archO, archD
     char : letra
     entero : cont = 0
3. Abrir archO en modo lectura
4. Abrir archD en modo escritura
5. Si archO y archD existen
       Leer letra de archO
       mientras letra no sea fin de archivo
          letra = toupper(letra)
          Escribir letra en archD
          Leer letra de archO
       cerrar(archO)
       cerrar(archD)
6. Sino
     Escribir ("ERROR")
*/

void copiaArchivo(char rutaO[50], char rutaD[50])
{   FILE *archO, *archD;
    char letra;
    int cont = 0;
    archO = fopen(rutaO, "r");
    archD = fopen(rutaD, "w");
    if (archO != NULL && archD != NULL)
    {
       letra = fgetc(archO);
       while (letra != EOF)
       {
          letra = toupper(letra);
          fputc(letra, archD);
          letra = fgetc(archO);
       }
       fclose(archO);
       fclose(archD);
    }
    else
       printf("ERROR");
}

/*Algoritmo: Imprime archivo
1. Recibir como parametro ruta[50]
2. Declarar variables
     FILE : arch
     char : letra
3. Abrir arch en modo lectura
4. Si arch existe
       Leer letra de arch
       mientras letra no sea fin de archivo
          Escribir la letra en pantalla
          Leer letra de arch
       cerrar(arch)
5. Sino
     Escribir ("ERROR")
*/

void imprimeArchivo(char ruta[50])
{   FILE *arch;
    char letra;
    arch = fopen(ruta, "r");
    if (arch != NULL)
    {
       letra = fgetc(arch);
       while (letra != EOF)
       {
          printf("%c", letra);
          letra = fgetc(arch);
       }
       fclose(arch);
    }
    else
      printf("\n ERROR");
}

void menu()
{
    printf("\n MENU \n");
    printf("\n A. Escribir en archivo");
    printf("\n B. Cuenta Caracteres en archivo");
    printf("\n C. Copia Archivo");
    printf("\n D. Imprime Archivo");
    printf("\n S. Salir");
    printf("\n Pulse la opcion deseada: ");

}

void main ()
{
  char ruta[50], rutaD[50], opcion;
  int res;
  do
  {
    menu();
    fflush(stdin);
    scanf("%c", &opcion);
    switch (opcion)
    {
      case 'a':
      case 'A':
            printf("\n Introduce la ruta: ");
            fflush(stdin);
            gets(ruta);
            escribirEnArchivo(ruta);
      break;
      case 'b':
      case 'B':
            printf("\n Introduce la ruta: ");
            fflush(stdin);
            gets(ruta);
            res = cuentaCaracteres(ruta);
            printf("\n El archivo tiene %i caracteres", res);
      break;
      case 'c':
      case 'C':
            printf("\n Introduce la ruta origen: ");
            fflush(stdin);
            gets(ruta);
            printf("\n Introduce la ruta destino: ");
            fflush(stdin);
            gets(rutaD);
            copiaArchivo(ruta, rutaD);
      break;
      case 'd':
      case 'D':
            printf("\n Introduce la ruta: ");
            fflush(stdin);
            gets(ruta);
            imprimeArchivo(ruta);
      break;
      case 's':
      case 'S':
            _exit(0);
      break;
    }
     printf("\n\n");
     system("PAUSE");
     system("cls");
  }while (opcion != 's' && opcion != 'S');
}

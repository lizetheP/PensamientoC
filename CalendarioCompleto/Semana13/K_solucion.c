#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/*Algoritmo: Escribir 5 frases en un archivo
1. Declarar variables:
    FILE : arch
    char : frase[50]
    entero : i
2. Abrir arch en modo escritura
3. Si arch existe
        for (i=1; i<=5; i++)
          Escribir("Dame una frase")
          Leer(frase)
          Escribir frase en arch
        Cerrar(arch)
4. Sino
     Escribir("ERROR")*/

void escribirEnArchivo ( )
{ FILE *arch;
  char frase[50];
  int i;
  arch = fopen("frases.txt", "w");
  if (arch != NULL)
  {
     for (i=1; i<=5; i++)
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

/*Algoritmo: Cuenta consonantes
1. Declarar variables:
    FILE : arch
    char : letra
    entero : cont = 0
2. Abrir arch en modo lectura
3. Si arch existe
       Leer letra de arch
       mientras letra sea diferente de fin de archivo
          si (letra es consonante)
               cont++
          Leer letra de arch
       Cerrar(arch)
4. Sino
     Escribir("ERROR")
5. Regresar cont*/

int cuentaConsonantes()
{  FILE *arch;
   char letra;
   int cont = 0;
   arch = fopen("frases.txt", "r");
   if (arch != NULL)
   {
       letra = fgetc(arch);
       while (letra != EOF)
       {
          letra = toupper(letra);
         // if (letra >= 66 && letra <= 90 && letra != 'E' && letra != 'I' && letra != 'O' && letra != 'U')
          if (letra >= 'B' && letra <= 'Z' && letra != 'E' && letra != 'I' && letra != 'O' && letra != 'U')
               cont++;
          letra = fgetc(arch);
       }
       fclose(arch);
   }
   else
     printf("ERROR");
   return cont;
}

/* Algoritmo: escribirConFormato
1. Declarar variables:
    FILE : arch
    char : frase[20], carrera[5]
    real : calif
2. Abrir arch en modo escritura
3. Si arch existe
        Escribir("Dame tu nombre")
        Leer(nombre)
        Escribir("Dame tu carrera")
        Leer(carrera)
        Escribir("Dame tu calificacion final")
        Leer(calif)
        Escribir nombre, carrera, calif en arch
        Cerrar(arch)
4. Sino
     Escribir("ERROR")*/

void escribirConFormato()
{
    FILE *arch;
    char nombre[20], carrera[5];
    float calif;
    arch = fopen("calis.txt", "w");
    if (arch != NULL)
    {
        printf("\n Dame tu nombre: ");
        fflush(stdin);
        gets(nombre);
        printf("\n Dame tu carrera: ");
        fflush(stdin);
        gets(carrera);
        printf("\n Dame tu calificacion final: ");
        scanf("%f", &calif);
        fprintf(arch, "%s %s %f", nombre, carrera, calif);
        fclose(arch);
    }
    else
      printf("ERROR");
}

/*Algoritmo: LEER CON FORMATO
1. Declarar variables:
    FILE : arch
    char : frase[20], carrera[5]
    real : calif
2. Abrir arch en modo lectura
3. Si arch existe
        Leer con formato nombre, carrera, calif del arch
        Escribir (nombre, carrera, calif)
        Cerrar(arch)
4. Sino
     Escribir("ERROR")*/

void leerConFormato()
{
    FILE *arch;
    char nombre[20], carrera[5];
    float calif;
    arch = fopen("calis.txt", "r");
    if (arch != NULL)
    {
        fscanf(arch, "%s %s %f", &nombre, &carrera, &calif);
        printf("\n %s %s %f", nombre, carrera, calif);
        fclose(arch);
    }
    else
      printf("ERROR");
}

void main()
{
  char opcion;
  int res;
  do
  {
    printf("\n\n MENU\n");
    printf("\n A. Escribir en archivo\n");
    printf("\n B. Cuenta Consonantes\n");
    printf("\n C. Guarda datos de alumnos\n");
    printf("\n D. Muestra datos de alumnos\n");
    printf("\n S. Salir\n");
    printf("\n Pulse la opcion deseada: ");
    fflush(stdin);
    scanf("%c", &opcion);
    switch (opcion)
    {
        case 'A':
        case 'a':
            escribirEnArchivo();
        break;
        case 'B':
        case 'b':
            res=cuentaConsonantes();
            printf("\n El archivo tiene %i consonantes\n", res);
        break;
        case 'C':
        case 'c':
            escribirConFormato();
        break;
        case 'D':
        case 'd':
            leerConFormato();
        break;
        case 'S':
        case 's':
            _exit(0);
        break;
    }
    printf("\n\n");
    system("PAUSE");
    system("cls");
  }while (opcion!='S'&& opcion!='s');
}

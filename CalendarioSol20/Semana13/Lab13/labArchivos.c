#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/*Algoritmo: Escribe 5 frases en archivo
1. Declarar arch, frase[50], i
2. Abrir arch en modo de escritura
3. Si el arch existe
      for (i=1; i<=5; i++)
      {
          Escribir("Dame una frase")
          Leer (frase)
          Escribir frase en arch
      }
      Cerrar(ach)
4. Sino
     Escribir ("ERROR ARCHIVO NO SE PUDO CREAR")*/


void escribirEnArchivo ()
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
     printf("\n ERROR ARCHIVO NO SE PUDO CREAR");
}

/*Algoritmo: Cuenta consonantes
1. Declarar arch, i=0, letra
2. Abrir arch en modo de lectura
3. Si el arch existe
      letra = leer letra de arch
      while (letra != EOF)
      {
         si (letra es consonante)
         {
             i++
         }
         letra = leer letra de arch
      }
      Cerrar(ach)
4. Sino
     Escribir ("ERROR ARCHIVO NO SE PUDO ABRIR")
5. Regresar i*/

int cuentaConsonantes()
{FILE *arch;
 int i=0;
 char letra;
 arch = fopen("frases.txt", "r");
 if (arch != NULL)
 {    letra = fgetc(arch);
      while (letra != EOF)
      {  letra = tolower(letra);
         if (letra >= 'b' && letra <= 'z' && letra != 'e'
             && letra != 'i' && letra != 'o' && letra != 'u')
         {
             i++;
         }
         letra = fgetc(arch);
      }
      fclose(arch);
 }
 else
     printf("\n ERROR EL ARCHIVO NO SE PUDO ABRIR");
 return i;
}

/*Algoritmo: Escribir con formato
1. Declarar arch, nombre[30], carrera[5], calif
2. Abrir arch en modo de escritura
3. Si el arch existe
      Escribir("Dame tu nombre")
      leer(nombre)
      Escribir("Dame tu carrera")
      leer(carrera)
      Escribir("Dame tu calificacion")
      leer(calif)
      Escribir en archivo de texto (nombre, carrera, calif)
      Cerrar(ach)
4. Sino
     Escribir ("ERROR ARCHIVO NO SE PUDO CREAR")*/

void escribirConFormato()
{
  FILE *arch;
  char nombre[30], carrera[5];
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
      printf("\n Dame tu calificacion: ");
      scanf("%f", &calif);
      fprintf(arch, "%s %s %.1f", nombre, carrera, calif);
      fclose(arch);
  }
  else
     printf("\n ERROR ARCHIVO NO SE PUDO CREAR");
}

/*Algoritmo: Leer con formato
1. Declarar arch, nombre[30], carrera[5], calif
2. Abrir arch en modo de lectura
3. Si el arch existe
      Leer con formato del archivo(nombre, carrera, calif)
      Escribir en C (nombre, carrera, calif)
      Cerrar(arch)
4. Sino
     Escribir ("ERROR ARCHIVO NO SE PUDO ABRIR")*/

void leerConFormato()
{
  FILE *arch;
  char nombre[30], carrera[5];
  float calif;
  arch = fopen("calis.txt", "r");
  if (arch != NULL)
  {
      fscanf(arch,"%s %s %f", &nombre, &carrera, &calif);
      printf("\n %s %s %.1f", nombre, carrera, calif);
      fclose(arch);
  }
  else
     printf("\n ERROR ARCHIVO NO SE PUDO ABRIR");
}
int main ()
{
  char ruta[50], opcion;
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

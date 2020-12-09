#include <stdio.h>
#include <stdlib.h>

void nuevoArchivo(char rutaO[25], char rutaD[25])
{
    FILE *ori;
    FILE *des;
    char letra;

    ori = fopen(rutaO, "r");
    des = fopen(rutaD, "w");

    if (ori != NULL && des != NULL)
    {
        letra = fgetc(ori);
        while (letra != EOF)
        {
          letra = tolower(letra);
          fputc(letra, des);
          letra = fgetc(ori);
        }
        fclose(ori);
        fclose(des);
    }
    else
      printf("\n ERROR CON ALGUN ARCHIVO");
}



int main()
{ char rutaO[25], rutaD[25];

  printf("\n Dame la ruta origen: ");
  fflush(stdin);
  gets(rutaO);
  printf("\n Dame la ruta destino: ");
  fflush(stdin);
  gets(rutaD);
  nuevoArchivo(rutaO, rutaD);

}

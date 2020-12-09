#include <stdio.h>
#include <stdlib.h>

/*Algoritmo: Cuentas de ahorro
var
    caracter : opcion, opcion2
    real : saldo, saldof, interes

inicio
   Escribir("OPCIONES
                        a. Muestra los tipos de cuenta de ahorro (Muestra en pantalla la tabla que se ilustra en el problema. Dar el formato más apropiado.)
                        b. Calcular el saldo después de intereses o comisiones.
                        s. Salir  (Cerrar la ventana. NOTA: Utiliza la instrucción para salir _exit(0);  Incluye la libreria <stdlib.h> )
                    ")
   Leer(opcion)
   En Caso (opcion)
       'a':
       'A'
           Mostrar los tipos de cuentas de ahorro
       'b':
       'B':
           Escribir(" TIPO DE CUENTA
                            a. Libretón
                            b. Banorte Fácil
                            c. Ahorro Scotiabank
                            Dame el tipo de cuenta")
            Leer(opcion2)
            En caso(opcion2)
               'a':
               'A':
                    Escribir("Dame el saldo")
                    Leer(saldo)
                    si (saldo < 750)
                         saldof = saldo - 75
                    sino
                         interes = saldo * 1.05%
                         saldof = saldo + interes
                    Escribir(saldof)
               'b':
               'B':
                    Escribir("Dame el saldo")
                    Leer(saldo)
                    si (saldo < 1000)
                         saldof = saldo - 75
                    sino
                         interes = saldo * 1.35%
                         saldof = saldo + interes
                    Escribir(saldof)
                'c':
                'C':
                    Escribir("Dame el saldo")
                    Leer(saldo)
                    si (saldo < 2000)
                         saldof = saldo - 60
                    sino
                         interes = saldo * .9%
                         saldof = saldo + interes
                    Escribir(saldof)
                 default:
                     Escribir("OPCION INVALIDA")
       's':
       'S':
           Salir del programa
       default:
            Escribir("OPCION INVALIDA")
fin                */


void main()
{  char  opcion, opcion2;
   float  saldo, saldof, interes;

   printf("\n MENU DE OPCIONES \n");
   printf("\n a. Muestra los tipos de cuenta de ahorro ");
   printf("\n b. Calcular el saldo despues de intereses o comisiones");
   printf("\n s. Salir \n");
   printf("\n Dame una opcion: ");
   fflush(stdin); // Libera la memoria
   scanf("%c", &opcion);
   switch (opcion)
   {
       case 'a':
       case 'A':
            printf("\n Banco \t\t Nombre de \t Tasa de    Saldo     Cuota por ");
            printf("\n \t\t cuenta \t interes    minimo    manejo");
            printf("\n  \t\t\t\t mensual              de cuenta");
            printf("\n------------------------------------------------------------------");
            printf("\n Bancomer \t Libreton \t  1.05% \t    $750.00    $75.00 ");
            printf("\n Banamex  \t Banorte Facil \t  1.35% \t    $1000.00   $75.00 ");
            printf("\n Scotiabank \t Ahorro Scotia \t  0.9% \t    $2000.00   $60.00 ");
       break;
       case 'b':
       case 'B':
           printf("\n TIPO DE CUENTA \n");
           printf("\n a. Libreton ");
           printf("\n b. Banorte Facil ");
           printf("\n c. Ahorro Scotiabank \n");
           printf("\n Dame el tipo de cuenta: ");
           fflush(stdin);  // Libera la memoria
           scanf("%c", &opcion2);
           switch(opcion2)
           {
               case 'a':
               case 'A':
                    printf("\n Dame el saldo: ");
                    scanf("%f", &saldo);
                    if (saldo < 750)
                         saldof = saldo - 75;
                    else
                    {
                         interes = saldo * 1.05/100;
                         saldof = saldo + interes;
                    }
                    printf("\n Saldo final : %.2f ", saldof);
               break;
               case 'b':
               case 'B':
                    printf("\n Dame el saldo: ");
                    scanf("%f", &saldo);
                    if (saldo < 1000)
                         saldof = saldo - 75;
                    else
                    {
                         interes = saldo * 1.35/100;
                         saldof = saldo + interes;
                     }
                    printf("\n Saldo final : %.2f ", saldof);
                break;
                case 'c':
                case 'C':
                    printf("\n Dame el saldo: ");
                    scanf("%f", &saldo);
                    if (saldo < 2000)
                         saldof = saldo - 60;
                    else
                    {
                         interes = saldo * .9/100;
                         saldof = saldo + interes;
                     }
                    printf("\n Saldo final : %.2f ", saldof);
                 break;
                 default:
                     printf("\n OPCION INVALIDA");
             }
       break;
       case 's':
       case 'S':
           _exit(0);  // Instrucción para salir del programa
       break;
       default:
            printf("\n OPCION INVALIDA");
     }
     printf("\n\n");
     system("PAUSE");
}

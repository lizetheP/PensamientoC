#include <stdio.h>
#include <stdlib.h>

int main()
{
/*
   int i = 0;
                            int n = 5;
                            while (i <= n)
                            {
                                 if (i % n == 0)
                                 {
                                      i = i + 1;
                                 }
                                 else
                                 {
                                     i = i * 2;
                                 }
                            }

  printf("\n %i", i);


  int a = 10, b = 3, c, bandera = 1;
                            do
                            {
                                 c = a % b;
                                 a = b;
                                 b = c;
                                 if (c == 0)
                                 {
                                      bandera = 0;
                                 }
                            } while (bandera == 1);


  printf("\n a: %i, b: %i, c: %i", a, b, c);

  int sum = 0, i, j;
                                  for (i = 0; i < 3; i++)
                                  {
                                         sum = sum + i;
                                         for (j = 0; j < 3; j++)
                                         {
                                                  sum = sum + j;
                                          }
                                  }

                                 int sum = 0, i, j;
                                  for (i = 0; i < 3; i++)
                                  {
                                          sum = sum + i;
                                          for (j = i; j < 3; j++)
                                          {
                                                sum = sum + j;
                                          }
                                  }
*/
int sum = 0, i, j;
                                   for (i = 0; i < 3; i++)
                                   {
                                          sum = sum + i;
                                          for (j = 3; j > 0; j--)
                                          {
                                                  sum = sum + j;
                                           }
                                   }


  printf("\n sum : %i", sum);
  printf("\n\n");
  system("PAUSE");

}

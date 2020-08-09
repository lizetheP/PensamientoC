#include <stdio.h>
#include <stdlib.h>

int main()
{
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
                                 printf("\n %i %i", i, n);
                            }
}

/*
Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números 
maiores que 0.
*/

#include <stdio.h>
#include <stdlib.h>

int	main()
{
    int count = 0, number = 1, multiple = 5;
    while (count < 5 )
    {
        if (number % multiple == 0)
        {
            printf("O número %d é multiplo de %d\n",number, multiple);
            count++;
        }
        number ++;
    }

    system("pause");
    return 0;
}

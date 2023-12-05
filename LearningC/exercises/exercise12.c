/*
 Faça um programa que leia um vetor de 10 posições. Conte e mostre quantos valores pares ele possui. 
*/

#include <stdio.h>
#include <stdlib.h>


int	main()
{
    int size = 10;
    int vector[size];
    int evenCount = 0;

    printf("\tContador de números pares:\n");
    for (int i = 0; i < size; i++)
    {
        printf("\tDigite o %dº valor: ",(i+1));
        scanf("%d",&vector[i]);
        
        if (vector[i] % 2 == 0)
            {
                evenCount ++;
                
            }
    }

    printf("\tQuantidade de números pares: %d\n",evenCount);

    system("pause");
    return 0;
}

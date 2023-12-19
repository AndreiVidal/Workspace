/*
 Faça um programa que leia um vetor de 10 posições. Conte e mostre quantos valores pares ele possui. 
*/

#include <stdio.h>
#include <stdlib.h>

#define SIZE  10

int	main()
{
    int vector[SIZE];
    int evenCount = 0;

    printf("\tContador de números pares:\n");
    for (int i = 0; i < SIZE; i++)
    {
        printf("\tDigite o %dº valor: ",(i+1));
        while(scanf("%d", &vector[i]) != 1) //Making Sure It's an Integer
        {
            printf("Entrada inválida. Por favor, insira um números: ");
            int c;
            while ((c = getchar()) != '\n' && c != -1 );
        }
        if (vector[i] % 2 == 0)
            {
                evenCount ++;
                
            }
    }

    printf("\tQuantidade de números pares: %d\n",evenCount);

    getchar();
    return 0;
}

/*
Faça um programa que leia 10 números e escreva o maior e o menor valor lido
*/

#include <stdio.h>
#include <stdlib.h>

int	main()
{

    int value , greaterNumber, lowerNumber;
    for (int i = 0; i < 10; i++)
    {
        printf("Digite o %dº valor: ",(i + 1));
        scanf("%d",&value);
        if (greaterNumber < value)
        {
            greaterNumber = value;
        }
        if (lowerNumber > value)
        {
            lowerNumber = value;
        }
    }
        printf("O maior valor é %d\n",greaterNumber);
        printf("O menor valor é %d\n",lowerNumber);

    system("pause");
    return 0;
}

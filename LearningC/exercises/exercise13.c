/*
Faça um programa que leia um vetor de 10 posições e atribua valor 0 para todos os elementos que 
possuírem valores negativos
*/

#include <stdio.h>
#include <stdlib.h>


int	main()
{
    int size = 10;
    int vector[size];
    for (int i = 0; i < size; i++)
    {
        printf("%dº número: ",(i + 1));
        while(scanf("%d", &vector[i]) != 1) //Making Sure It's an Integer
        {
            printf("Entrada inválida. Por favor, insira um número inteiro: ");
            fflush(stdin);//Clear Buffer
        }

        if (vector[i] < 0)
        {
            vector[i] = 0;
        }
    
        
    }
    printf("\tNúmeros digitados\n");
    for (int i = 0; i < size; i++)
    {
        printf("%dº: %d\n",(i + 1),vector[i]);
        
    }
    

    system("pause");
    return 0;
}

/*
Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa 
deve executar os seguintes passos: 
a) Atribula os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7; 
b) Armazene em uma variável inteira simples a soma entre os valores das posições A[0], A[1] e A[5] do vetor 
e mostre na tela esta soma; 
c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100; 
d) Mostre na tela cada valor do vetor A, um em cada linha. 

*/

#include <stdio.h>
#include <stdlib.h>


int	main()
{
    int A[6];
    A[0] = 1;
    A[1] = 0;
    A[2] = 5;
    A[3] = -2;
    A[4] = -5;
    A[5] = 7;

    int sumVet = A[0] + A[1] + A[5];

    printf("A some entre os valores %d %d %d reseulta em %d\n",A[0],A[1],A[5], sumVet);

    A[4] = 100;

    for (int i = 0; i < 6; i++)
    {
        printf("Valor na %dº posição é %d\n",(i+1),A[i]);
    }

    system("pause");
    return 0;
}

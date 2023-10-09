#include <stdio.h>
#include <stdlib.h>
/*
    Escreva um programa que leia um número inteiro e apresente seu antecessor e seu sucessor. 
*/


int main()
{
    int number;

    printf(" Digite um número inteiro: ");
    scanf("%d", &number);
    printf(" \nO numero digitado foi %d", number);
    printf(" \nSeu antecessor é %d", number-1);
    printf(" \nSeu sucessor é %d\n", number+1);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>

/*
    Faça um programa que leia três valores e apresente como resultado a soma dos quadrados dos valores lidos
*/

int	main()
{
    int n1, n2, n3, result;
    printf("\t===>>> Soma dos quadrados <=====\n");
    
    printf("Digite o primeiro valor\n");
    scanf("%d",&n1);
    
    printf("Digite o segundo valor\n");
    scanf("%d",&n2);
    
    printf("Digite o terceiro valor\n");
    scanf("%d",&n3);
    n1 *= n1;
    n2 *= n2;
    n3 *= n3;
    result = n1 + n2 +n3 ;

    printf("\tA soma dos quadrados dos valores é = %d\n",result);

    system("pause");
    return 0;
}

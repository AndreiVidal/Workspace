/*
 Escreva um programa que declare um inteiro, inicialize-o com 0, incremente-o de 100 em 100, imprimindo 
seu valor na tela, até que seu valor seja 100000 (cem mil).
*/

#include <stdio.h>
#include <stdlib.h>

int	main()
{
    int number = 100000;

    for(int i = 0; i <= number; i += 100)
    {
        printf("%d\n",i);
    }
    
    system("pause");
    return 0;
}

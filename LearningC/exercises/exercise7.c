/*
    Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao 
valor que cada um deu para a realização da aposta. Faça um programa que leia quanto cada apostador 
apostou, o valor do prêmio e imprima quanto cada um ganharia do prêmio com base no valor investido.
*/

#include <stdio.h>
#include <stdlib.h>

int	main()
{
    float stakeAmount1, stakeAmount2, stakeAmount3 ;
    float prize;
    float prizeBetter1, prizeBetter2, prizeBetter3;

    printf("#####################################\n");

    printf("Digite o valor do premio: ");
    scanf("%f",&prize);

    printf("\nDigite o valor investido do primeiro apostador: ");
    scanf("%f",&stakeAmount1);
    
    printf("\nDigite o valor investido do segundo apostador: ");
    scanf("%f",&stakeAmount2);
    
    printf("\nDigite o valor investido do terceiro apostador: ");
    scanf("%f",&stakeAmount3);

    float totalAmount = stakeAmount1 + stakeAmount2 +stakeAmount3;

    prizeBetter1 = (stakeAmount1 / totalAmount) * prize;
    prizeBetter2 = (stakeAmount2 / totalAmount) * prize;
    prizeBetter3 = (stakeAmount3 / totalAmount) * prize;

    printf("O valor total do premio é de R$ %.2f \n",prize);
    printf("O valor será dividido respectivamente em RS %.2f, RS %.2f, RS %.2f\n",prizeBetter1, prizeBetter2, prizeBetter3);

    printf("#####################################\n");

    system("pause");
    return 0;
}

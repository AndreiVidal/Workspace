/*
Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e
apresente o valor do rendimento e o valor total (valor do depósito + valor do rendimento).
*/
#include <stdio.h>

int main()
{
    float deposit, rate, income, total;

    printf("Digite o valor do depósito: ");
    scanf("%f", &deposit);
    printf("Digite a taxa de juros: ");
    scanf("%f", &rate);
    
    income = deposit * (rate / 100);
    total = deposit + income;

    printf("Você depositou R$ %.2f com a taxa de %.2f %%\n", deposit, rate);
    printf("seu valor total é de R$ %.2f\n",total);


    return 0;
}

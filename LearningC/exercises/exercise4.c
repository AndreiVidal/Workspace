/*
Escreva um programa que receba dois números, calcule e apresente o resultado
do primeiro número elevado ao segundo.
*/

#include <stdio.h>
#include <math.h>
#include <locale.h>


int main()
{
    setlocale(LC_ALL,"");
    int number1, number2, total;

    printf("Calcular potência entre dois numeros\n");
    printf("Digite um número inteiro: ");
    scanf("%d", &number1);
    printf("\nDigite a potência: ");
    scanf("%d", &number2);

    total = pow(number1, number2);

    printf("%d elevado a %.d é igual a %d\n\n", number1, number2, total);
    return 0;
}

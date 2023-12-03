/*
Construa um programa que receba a idade de uma pessoa e identifique sua classe
eleitoral: não eleitor (menor que 16 anos de idade), eleitor obrigatório (entre 18 e
65 anos) e eleitor facultativo (entre 16 e 18 anos e maior que 65 anos).
*/

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portugese");
    int idade;

    printf("Digite sua idade: ");
    scanf("%d", &idade);
    if (idade < 16)
    {
        printf("Você não tem idade para votar, volte dentro de %d anos \n", (16 - idade));
    }
    else if (idade <= 17 || idade > 65)
    {
        printf("Seu voto é facultattivo.\n");
    }
    else
    {
        printf("Seu voto é obrigatório.\n");
    }

    return 0;
}
/*
    Elabore um programa que receba quatro notas e calcule a média aritmética entre elas.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float grade1, grade2, grade3, grade4, avarage;

    printf("\n Informe a nota 1: ");
    scanf("%f",&grade1);
    printf("\n Informe a nota 2: ");
    scanf("%f",&grade2);
    printf("\n Informe a nota 3: ");
    scanf("%f",&grade3);
    printf("\n Informe a nota 4: ");
    scanf("%f",&grade4);
    avarage = (grade1+grade2+grade3+grade4) / 4 ;
    printf("\n\tSua média aritmética é %.2f\n",avarage);
    
    return 0;
}

/*
 Faça um programa que tenha uma função que receba um vetor de inteiros como parâmetro e retorne o 
maior valor. 
*/

#include <stdio.h>

int findLargestValue(int array[], int size);

int main()
{
    int myArray[] = {5, 8, 9, 45, 99};
    int size = sizeof(myArray) / sizeof(myArray[0]);
    int result = findLargestValue(myArray , size);
    printf("O maior valor é %d\n", result);

    return 0;
}

int findLargestValue(int array[],int size)
{
    int largestValue = 0;

    for (int i = 0; i < size; i++)
    {
        if (i == 0)
        {
            largestValue = array[i];
        }
        
        if (array[i] > largestValue)
        {
            largestValue = array[i];
        }
    }

    return largestValue;
}
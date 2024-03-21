#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, maior, menor;
    int inicio = 1;

    while(num >= 0){
        scanf("%d", &num);
        if(inicio == 1){
            maior = num;
            menor = num;
        }
        inicio = 0;

        if(num > maior){
            maior = num;
        }
        if(num < menor){
            menor = num;
        }
    }
    printf("maior numero: %d", maior);
    printf("menor numero: %d", menor);
}
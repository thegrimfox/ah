#include <stdio.h>

int main()
{
    int num=0, A, B;
    printf("ingrese el primer numero para sumar: ");
    scanf("%d", &A);

    printf("ingrese el segundo numero a sumar: ");
    scanf("%d", &B);

    num = A + B;

    printf("el resultado final es = %d", num);
    return 0;
}
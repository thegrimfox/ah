#include<stdio.h>
#include<stdlib.h>

int main()
{
    /*malloc es para delimitar espacio*/
    int *bigarray= malloc(10 * sizeof(int));
    for (int i = 0; i < 10; i++)
    {
        bigarray[i]=i;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", bigarray[i]);
    }

    return 0;
}
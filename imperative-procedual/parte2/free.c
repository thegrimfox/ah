#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *bigarray= (int*) calloc(10, sizeof(int));
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", bigarray[i]);
        bigarray[i]=i;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", bigarray[i]);
    }
    /*el comando free es para limpiar la memoria*/
    free(bigarray)
    return 0;
}
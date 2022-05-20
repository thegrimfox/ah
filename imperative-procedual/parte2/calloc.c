#include<stdio.h>
#include<stdlib.h>
int main()
{
    /*calloc es parecido a malloc pero calloc define un valor por defecto */
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
    return 0;
}
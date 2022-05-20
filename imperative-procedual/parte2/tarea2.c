#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char **argv)
{
    int A = 0;
    int B = 0; 
    int sum;
    int c;

    opterr = 0;

    while ((c = getopt(argc, argv,"a:b:")) !=-1)
        switch (c)
        {
        case 'a':
            A = atoi(optarg);
            break;
        case 'b':
            B = atoi(optarg);
        
        default:
            break;
        }
    sum = A + B;
    printf("la suma entre %d y %d seria: %d", A, B,sum);

    return 0;
}
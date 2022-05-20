#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int main(int argc, char **argv)
{
    int Aflag = 0;
    int Bflag = 0;
    char sum[5], res[5], div[5], mul[5];
    int c, sul;

    opterr = 0;

    while ((c = getopt(argc, argv, "a:b:t:")) != -1)
        switch (c)
        {
        case 'a':
            Aflag = atoi(optarg);
            break;
        case 'b':
            Bflag = atoi(optarg);
            break;
        case 't':
            if (optarg == sum)
            {
                sul = Aflag + Bflag;
            }
            else if (optarg == res)
            {
                sul = Aflag - Bflag;
            }
            else if (optarg == mul)
            {
                sul = Aflag * Bflag;
            }
            else if (optarg == div)
            {
                sul = Aflag / Bflag;
            }
            break;        
        default:
            break;
        }
    printf("la operacion seleccionada entre %d y %d el resultado final fue: %d", Aflag, Bflag, sul);
    return 0;
}
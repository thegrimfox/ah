#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int main(int argc, char **argv)
{
    int Aflag = 0;
    int Bflag = 0;
    char* operacion;
    int c, sul=0;

    opterr = 0;

    while ((c = getopt(argc, argv, "a:b:t:")) != -1){
        switch (c)
        {
        case 'a':
            Aflag = atoi(optarg);
            break;
        case 'b':
            Bflag = atoi(optarg);
            break;
        case 't':
            operacion = optarg;
            break;        
        default:
            break;
        }
    }

    if (strcmp(operacion, "sum")==0)
        {
            sul = Aflag + Bflag;
        }
    else if (strcmp(operacion,"res")==0)
        {
            sul = Aflag - Bflag;
        }

    printf("la operacion seleccionada %s entre %d y %d el resultado final fue: %d", operacion, Aflag, Bflag, sul);
    return 0;
}

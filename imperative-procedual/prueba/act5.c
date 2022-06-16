#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    int v = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    int res = 0;

    opterr = 0;

    while ((d = getopt (argc, argv, "vb:c:")) !=-1)
        switch(d)
        {
        case 'v':
            v = 1;
            break;
        case 'b':
            b = atoi(optarg);
            break;
        case 'c':
            c = atoi(optarg);
            break;
        case '?':
            return 1;
        default:
            abort();
        }
    res = b;
    for (int i = 1; i < c; i++)
        {
            res = res * b;
        }
    if (v)
    {
        printf("res equals = %d", res);
    }
    return 0;
}
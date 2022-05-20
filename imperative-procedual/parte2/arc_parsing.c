#include<ctype.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char **argv)
{
    int aflag = 0;
    int bflag = 0;
    char *cvalue = NULL;
    int index;
    int c;

    opterr = 0;

    while ((c = getopt(argc, argv, "ab:c:")) != -1)
        switch (c)
        {
        case 'a':
            aflag = 1;
            break;
        case 'b':
            bflag = atoi(optarg);
            break;
        case 'c':
            cvalue = optarg;
            break;
        case '?':
            if (optopt == 'c')
                fprintf (stderr, "option -%c requires an argument.\n", optopt);
            else if (isprint(optopt))
                fprintf (stderr, "unknown option `-%c'.\n", optopt);
            else
                fprintf (stderr,
                        "unknown option character `\\x%x'.\n",optopt);
            return 1;
        default:
            abort();  
        }
    printf ("aflag = %d, bflag = %d, cvalue = %s\n", aflag, bflag, cvalue);

    for (index = optind; index < argc; index++)
        printf ("non-option argument %s\n", argv[index]);
    return 0;
}
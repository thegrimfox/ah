#include<stdio.h>
#include<string.h>

int main()
{
    char str[]="hello world";
    char *p;
    p=str;
    printf("first character is: %c\n", *p);
    p = p+1;
    printf("next character is: %c\n", *p);
    printf("printing all the character in a string\n");
    p=str;
    for (int i = 0; i < strlen(str); i++)
    {
        printf("%c\n", *p);
        p++;
    }
        
    return 0;
}
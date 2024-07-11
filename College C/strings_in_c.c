#include <stdio.h>
void printstr(char arr[])
{
    int i=0;
    while (arr[i]!='\0')
    {
        printf("%c",arr[i]);
        i++;
    }
    printf("\n");
}
int main()
{
    // char str[]={'p','u','l','k','i','t','\0'};
    // printstr(str);

    char str1[]="Pulkit";
    printstr(str1);//using custom function
    printf("%s\n",str1);//using printf

    char str2[20];
    gets(str2);//taking input string using gets, avoid scanf because you can't take whitespaces with it.
    puts(str2);//another way to print string

    return 0;
}
#include <stdio.h>
int main()
{
    FILE *ptr=NULL;

    // ptr=fopen("myfile2.txt","r");
    // ptr=fopen("myfile2.txt","w");
    ptr=fopen("myfile2.txt","r+");
    // ptr=fopen("myfile2.txt","a+");
    // char c=fgetc(ptr);
    // printf("The character that I read is %c\n",c);
    // c=fgetc(ptr);
    // printf("The character that I read is %c",c);


    // char str[34];
    // fgets(str, 16, ptr);
    // printf("The string I read is %s",str);


    fputc('o',ptr);
    fputc('o',ptr);
    fputs("This is a string",ptr);
    fclose(ptr);
    return 0;
}
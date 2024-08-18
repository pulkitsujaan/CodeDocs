#include <stdio.h>
int main()
{
    FILE *ptr=NULL;
    char str[50]="This is a good string\n";

    //reading a file
    // ptr=fopen("myfile.txt","r");
    // fscanf(ptr,"%s",str);
    // printf("The string stored is: %s\n",str);

    //writing a file
    // ptr=fopen("myfile.txt","w");
    // fprintf(ptr,"%s",str);

    //append a file
    ptr=fopen("myfile.txt","a");
    fprintf(ptr,"%s",str);
    return 0;
}

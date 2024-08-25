#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char const *argv[])
{
    const char * operation;
    int num1,num2;
    operation=argv[1];
    num1=atoi(argv[2]);
    num2=atoi(argv[3]);

    // printf("Operation is %s\n",operation);
    // printf("Num1 is %d\n",num1);
    // printf("Num2 is %d\n",num2);

    if (strcmp(operation,"add")==0)
    {
        printf("%d\n",num1+num2);
    }
    if (strcmp(operation,"subtract")==0)
    {
        printf("%d\n",num1-num2);
    }
    if (strcmp(operation,"multiply")==0)
    {
        printf("%d\n",num1*num2);
    }
    if (strcmp(operation,"divide")==0)
    {
        printf("%d\n",num1/num2);
    }
    

    return 0;
}

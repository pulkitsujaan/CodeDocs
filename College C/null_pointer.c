#include <stdio.h>
int main()
{
    int a = 6;
    int* ptr=NULL;
    printf("The address of a is: %d\n",ptr);
    // printf("The value of ptr is: %d",*ptr);//this statement is not valid and program will crash as null pointer cannot be dereferenced
    ptr=&a;
    printf("The value of ptr is: %d",*ptr);
    return 0;
}
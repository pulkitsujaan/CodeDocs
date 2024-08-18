#include <stdio.h>
int main()
{
    int a=46;
    int *ptr;//wild pointer
    // *ptr=67;//this is not a good practice
    ptr=&a;
    printf("The value of this pointer is %d",*ptr);
    return 0;
}
/*void pointers cannot be dereferenced directly*/


#include <stdio.h>
int main()
{
    int a=78;
    float b=9.8;
    void *ptr=&a;
    ptr=&b;
    // printf("the value of a is: %d",*((int*)ptr));
    printf("the value of a is: %.2f",*((float*)ptr));
    return 0;
}
/*
a static variable when initialised in a variable, it remembers it's value from previous call and keeps the changes that were made to it.

local variable is given prescendence over global variable.

*/
#include <stdio.h>
int ret(int a)
{
    static int var1=10;
    printf("Static variable value: %d\n",var1);
    var1++;
    return a*10;
}
int main()
{
    int a=6;
    // printf("The value of a is %d\n",a);
    a=ret(a);
    a=ret(a);
    a=ret(a);
    a=ret(a);
    a=ret(a);
    a=ret(a);
    a=ret(a);
    // printf("The value of a is %d\n",a);    
    return 0;
}
/*
Auto storage Class: Local variables
default initial value:garbage value


External storage class: Global Variables
default initial value:0

extern keyword: used to tell compiler that the variable is defined somewhere else and there's no need to allocate space to it

global variables cannot be redifined;
*/


//by default variables are stored in auto class
#include <stdio.h>

//extern 
int sumfunc(int a, int b){
    extern int sum;
    return sum;
}

//static variable remembers it's previous value
int myfunc(){
    static int variable;
    printf("Value: %d\n",variable);
    variable++;
    return 0;
}

int sum=90;
int main()
{
    // int sum=256;
    // auto int sum=90;//also valid

    // int sum =sumfunc(3,5);
    // printf("The value of sum is: %d",sum);
    // int myvar=69;
    register int myvar=100;//to store this variable in register class

    myfunc();
    myfunc();
    myfunc();
    myfunc();
    myfunc();

    

    return 0;
}
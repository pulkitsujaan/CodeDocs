#include <stdio.h>
#include <stdlib.h>


int* danglefunc(){
    int a=5,b=10;
    int sum=a+b;
    return &sum;//sum
}
int main()
{
    // case 1: De allocation of a memory block
    int *ptr=(int*)malloc(7*sizeof(int));
    ptr[0]=45;
    ptr[1]=55;
    ptr[2]=35;
    ptr[3]=25;
    ptr[4]=47;
    free(ptr);//ptr is a dangling pointer now
    
    //case 2: function returning local variable address
    int *ptr2=danglefunc();

    //case 3: variable goes out of scope
    int *ptr3=NULL;
    {
        int a=12;
        ptr=&a;
    }
    //now ptr3 is a dangling pointer

    return 0;
}
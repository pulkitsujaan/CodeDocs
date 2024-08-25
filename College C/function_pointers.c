#include <stdio.h>
int sum(int a, int b){
    return a+b;
}
int main()
{
    printf("The sum of 5 and 6 is %d\n", sum(5,6));

    int (*fptr)(int, int);
    fptr=&sum;
    int d=(*fptr)(5,11);
    printf("Sum: %d",d);
    return 0;
}
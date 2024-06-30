#include <stdio.h>

int swap(int* x, int* y)
{
    int c;
    c=*x;
    *x=*y;
    *y=c;

}
int main()
{
    int a=10,b=20;
    printf("Value of a: %d, Value of b: %d\n",a,b);
    swap(&a,&b);
    printf("Value of a: %d, Value of b: %d\n",a,b);
    return 0;
}
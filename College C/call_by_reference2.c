#include <stdio.h>
int func(int* x, int*y)
{
    *x=*x+*y;
    *y=*x-(*y+*y);
}
int main()
{
    //quick quiz
    int a,b;
    printf("Enter a: ");
    scanf(" %d",&a);
    printf("Enter b: ");
    scanf(" %d",&b);

    func(&a,&b);
    printf("Final a: %d,\nFinal b: %d\n",a,b);
    return 0;
}
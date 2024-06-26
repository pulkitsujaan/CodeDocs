#include <stdio.h>
int sum(int a, int b)//with return value, with argument
{
    return a+b;
}

void printstar(int n)//with argument, no return value
{
    for (int i = 0; i < n; i++)
    {
        printf("%c",'*');
    }  
}
int returnnumber()//no argument, with return value
{
    int a;
    printf("Enter a number:");
    scanf("%d",&a);
    return a;
}
void helloworld()
{
    printf("Hello World!");
}
int main(int argc, char const *argv[])
{
    int a=10,b=20;
    int c=sum(a,b);
    printf("The sum is %d\n",c);
    printstar(6);
    returnnumber();
    helloworld();
    return 0;
}
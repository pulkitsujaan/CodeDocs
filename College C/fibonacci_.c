/*KYA HAI YE?!*/
#include <stdio.h>
int fibbo_recursive(int number)
{

    int res;
    if (number==1 || number==2)
    {
        return number-1;
    }
    else
    {
        return (fibbo_recursive(number-1) + fibbo_recursive(number-2));

    }
    
}
int fibbo_iterative(int n)
{
    
}


int main(int argc, char const *argv[])
{
    int num;
    printf("Enter an index to get fibonacci number of that index: ");
    scanf(" %d",&num);
    int fibbonacci=fibbo_recursive(num);
    printf("The fibbonacci series of this number is: %d",fibbonacci);
    return 0;
}

#include <stdio.h>
int main()
{
    int a,b,c;
    printf("Enter three numbers: ");
    scanf(" %d%d%d",&a,&b,&c);
    if (c==(a*a + b*b))
    {
        printf("%d is equal to sum of squares of %d and %d",c,a,b);
    }
    else if (a==(b*b + c*c))
    {
        printf("%d is equal to sum of squares of %d and %d",a,b,c);
    }
    else if (b==(a*a + c*c))
    {
        printf("%d is equal to sum of squares of %d and %d",b,a,c);
    }
    else{
        printf("Condition not satisified");
    }
    
    return 0;
}

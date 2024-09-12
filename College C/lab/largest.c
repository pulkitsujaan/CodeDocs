#include <stdio.h>
int main()
{
    int a,b,c;
    printf("Enter three numbers:\n");
    scanf("%d%d%d",&a,&b,&c);
    if (a>c && a>b)
    {
        printf("%d is greatest",a);
    }
    else if (b>c && b>a)
    {
        printf("%d is greatest",b);
    }
    else{
        printf("%d is greatest",c);
    }
    
    
    return 0;
}

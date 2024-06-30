#include <stdio.h>
int triangle_pattern(int n)
{
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    
}

int rev_triangle_pattern(int n)
{
    for (int i = n; i>0; i--)
    {
        for (int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
}
int main()
{
    int type,num;
    printf("----Star Pattern-------\n-What kind of star pattern do you want to print?\nPress 0: for Triangular Star Pattern.\nPress 1: for Reversed triangular star pattern.\n\n--------:");

    scanf("%d",&type);

    printf("Enter the number of rows you want to print: ");
    scanf(" %d",&num);
    if (type==0)
    {
        triangle_pattern(num);
    }
    else if (type==1)
    {
        rev_triangle_pattern(num);
    }
    
    
    return 0;
}
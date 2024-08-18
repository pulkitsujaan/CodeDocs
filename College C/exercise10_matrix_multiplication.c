#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[3][4], b[4][2], sum=0;
    int result[3][2];

    printf("Enter first matrix: \n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            // printf("Enter element [%d, %d]\n",i,j);
            scanf("%d",&a[i][j]);
            // getchar();
        }
        
    }

    printf("Enter second matrix: \n");
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            // printf("Enter element [%d, %d]\n",i,j);
            scanf("%d",&b[i][j]);
            // getchar();
        }
        
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                sum+=a[i][k]+b[k][j];
            }
            result[i][j]=sum;
            sum=0;
        }
        
    }

    //result printing

    printf("\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("%d ",result[i][j]);
        }
        printf("\n");
    }
    
    
    return 0;
}
#include <stdio.h>
int main(int argc, char const *argv[])
{
    // int age, i;
    // printf("Enter your age:\n");
    // scanf("%d",&age);
    // for (i = 0; i < age; i++)
    // {
    //     printf("%d\n",i);
    // }
    int i,j;
    for (int i = 0; i<=5; i++)
    {
        for (j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    
    
    return 0;
}

#include <stdio.h>
int main(int argc, char const *argv[])
{
    // int array1[4];
    // array1[0]=4;
    // array1[1]=5;
    // array1[2]=6;
    // array1[3]=7;

    int array2[]={1,2,3,4,5};//1d array
    // printf("%d",array2[2]);
    

    int array3[][4]={
        {1,2,3,4},
        {5,6,7,8}
    };
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf("%d",array3[i][j]);
        }
    printf("\n");
    }
    
    return 0;
}

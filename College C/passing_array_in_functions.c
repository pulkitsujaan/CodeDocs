#include <stdio.h>

int func(int array[])
{
    for (int i = 0; i < 5; i++)
    {
        printf("The value at %d is %d\n",i,array[i]);
    }
    
    array[0]=653;//This statement will change the value of original array because address was given to the formal parameter
    return 0;
}

void func2(int* ptr)
{
    for (int i = 0; i < 5; i++)
    {
        printf("The value at %d is %d\n",i,*(ptr+i));
    }
    
    *(ptr+1)=66;
}
int func3(int array3d[2][2])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            printf("The value at (%d,%d) is %d\n",i,j,array3d[i][j]);
        }
        
    }
    
}
int main()
{
    int arr[]={1,22,345,67,34};
    // printf("The value at 0 is: %d\n",arr[0]);
    // func(arr);//address passed, not the array
    // printf("The value at 0 is: %d\n",arr[0]);

    // func2(arr);
    // func2(arr);

    int arr2[][2]={{1,2},{3,4}};
    func3(arr2);//passing multi-dimensional arrays in functions
    return 0;
}
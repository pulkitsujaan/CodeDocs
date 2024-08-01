/*
malloc
calloc
realloc
free

*/
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *ptr;
    int n;
    printf("Enter the size of array you want to create: ");
    scanf(" %d", &n);

    // malloc initialize array elements with garbage value
    //  ptr=(int*)malloc(n*sizeof(int));

    // calloc initialize array elements with 0
    ptr = (int *)calloc(n, sizeof(int));

    // use of realloc
    printf("Enter the size of new array you want to create: ");
    scanf(" %d", &n);
    ptr = (int *)realloc(ptr, n * sizeof(int));

    // for (int i = 0; i < n; i++)
    // {
    //     printf("Enter value of element %d of array: ",i+1);
    //     scanf(" %d",&ptr[i]);
    // }

    for (int i = 0; i < n; i++)
    {
        printf("Value of element %d of array is: %d\n", i + 1, ptr[i]);
    }

    free(ptr); // memory that was being used is free now
    return 0;
}
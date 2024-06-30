#include <stdio.h>
int main()
{
    // char a='3';
    // char* ptra=&a;
    // printf("%d\n",ptra);
    // printf("%d",ptra-2);

    int arr[]={1,2,3,4};
    // printf("Value of first element: %d\n",arr[0]);

    printf("Address of first element: %d\n",&arr[0]);
    printf("Address of second element: %d\n",&arr[1]);
    printf("Address of first element: %d\n",arr);
    printf("Address of second element: %d\n",arr+1);

    printf("Value of first element: %d\n",*(&arr[0]));
    printf("Value of second element: %d\n",*(&arr[1]));
    printf("Value of first element: %d\n",*(arr));
    printf("Value of second element: %d\n",*(arr+1));

    return 0;
}
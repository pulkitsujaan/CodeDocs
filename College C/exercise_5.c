/*

Array reversal

*/

#include <stdio.h>

void arrrev(int arr[])
{
    int c;
    for (int i = 0; i < 4/2; i++)
    {
        
        c=arr[i];
        arr[i]=arr[3-i];
        arr[3-i]=c;
    }
    
}
int main()
{
    int array[]={1,2,3,4};
    printf("Array before reversal:\n");
    for (int i = 0; i < 4; i++)
    {
        printf("%d\n",array[i]);
    }
    printf("Array after reversal:\n");
    arrrev(array);
    for (int i = 0; i < 4; i++)
    {
        printf("%d\n",array[i]);
    }
    return 0;
}
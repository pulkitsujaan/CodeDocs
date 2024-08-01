#include <stdio.h>
#include <stdlib.h>
#include<string.h>
int main()
{

    int length;
    char* emp;

    char a,b;//example demonstration

    printf("-----ABC Pvt. ltd.-----\nEnter details of three employees\n");

    for (int i = 1; i < 4; i++)
    {
        printf("Employee %d:\n",i);
        printf("Enter no. of characters in your eID: ");
        scanf(" %d",&length);
        //if you don't insert getchar() here then scanf consumes the enter key as a valid input
        getchar();
        printf("Enter value of a: ");
        scanf("%c",&a);
        getchar();
        printf("Enter value of b: ");
        scanf("%c",&b);
        

        emp=(char*)calloc((length+1),sizeof(char));
        printf("Enter your eID: ");
        scanf(" %s",emp);

        printf("Your employee ID is: %s\n",emp);
        free(emp);
    }
    


    return 0;
}
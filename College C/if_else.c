/*
#include <stdio.h>
int main(int argc, char const *argv[])
{
    int age;
    printf("Enter your age: ");
    scanf("%d",age);
    if (age>=18)
    {
        printf("You're eligible to vote!");
    }
    else{
        printf("You're not eligible to vote!");
    }
    
    
    return 0;
}
*/

// quiz
#include <stdio.h>
int main(int argc, char const *argv[])
{
    char maths;
    char science;
    
    printf("Have you passed Maths exam?(y/n)\n");
    scanf("%c",&maths);
    printf("Have you passed science exam?(y/n)\n");
    scanf(" %c",&science);
    if (maths=='y' && science=='y')
    {
        printf("You are awarded with a gift worth of 45rs");
    }
    else if ((maths=='y' && science=='n')||(maths=='n' && science=='y'))
    {
        printf("You are awarded with a gift worth of 15rs");
    }

    return 0;
}

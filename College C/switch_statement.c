#include<stdio.h>
int main(int argc, char const *argv[])
{
    int age;
    printf("Enter your age: ");
    scanf("%d",&age);
    switch (age)
    {
    case 5:
        printf("5 saal ka baalak");
        break;
    
    case 10:
        printf("10 saal ka baalak");
        break;
    
    default:
        printf("KYA?!");
        break;
    }
    return 0;
}

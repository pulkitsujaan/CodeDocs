#include <stdio.h>
int main(int argc, char const *argv[])
{
    int age;
    for (int i = 0; i < 5; i++)
    {
        printf("------%d------\n",i);
        printf("Enter your age:\n");
        scanf("%d",&age);
        if (age==18)
        {
            break;
        }
        else if (age<5)
        {
            continue;
        }
        else{
            printf("Your age is %d\n",age);
        }
        
        
    }
    
    

    return 0;
}

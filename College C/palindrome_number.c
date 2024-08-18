#include <stdio.h>
int isPalindrome(int a){
    int num=a;
   int reversed=0;
   while(a!=0){
    reversed=(reversed*10) + (a%10);
    a=a/10;

   }
   if (reversed==num)
   {
    return 1;
   }
   else{
    return 0;
   }
   
}
int main()
{
    int number;
    printf("Enter a number to check palindrome: ");
    scanf(" %d",&number);

    if (isPalindrome(number))
    {
        printf("The number %d is a palindrome.",number);
    }
    else{
        printf("The number %d is not a palindrome.",number);
    }

    return 0;
}
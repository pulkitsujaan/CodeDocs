#include <stdio.h>
int main(int argc, char const *argv[])
{
    int age, i = 0;
    printf("Enter your age:\n");
    scanf("%d", &age);
    do
    {
        printf("%d\n", i);
        i = i + 1;
    } while (i < age);
    return 0;
}

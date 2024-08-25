#include <stdio.h>
int main(int argc, char const *argv[])
{
    // printf("The value of argc is %d",argc);
    for (int i = 0; i <= argc; i++)
    {
        printf("The argument number %d has a value %s\n", i, argv[i]);
    }

    return 0;
}

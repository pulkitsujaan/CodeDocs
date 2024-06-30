#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a=56;
    int* point_a=&a;
    printf("The Value of a is: %d\n",a);
    printf("The address of a is: %p\n",&a);

    printf("The value of a is : %d\n",*point_a);
    printf("The address of a is: %p\n",point_a);

    printf("The value of pointer is: %p\n",point_a);
    printf("The address of pointer is: %p\n",&point_a);

    printf("The hexadecimal value of pointer is: %x",point_a);
    return 0;
}

#include <stdio.h>
#include <string.h>

/*
code works properly when this is a structure but when it is converted to a union it gives garbage values in the elements that were declared first, only last element gives correct value.
*/

union Employee
{
    int id;
    float salary;
    char name[30];
};

int main()
{
    union Employee vimal;
    vimal.id=34;
    strcpy(vimal.name,"Vimal");
    vimal.salary=50000;

    printf("The name of the employee is %s\n",vimal.name);
    printf("The id of %s is %d\n",vimal.name,vimal
    .id);
    printf("The salary of %s is %.2f\n",vimal.name,vimal.salary);
    return 0;
}

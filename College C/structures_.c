#include <stdio.h>
#include <string.h>
// initialization of structure
struct
    company
{
    int age;
    char name[32];
    float salary;
};
int main()
{
    struct company Employee;
    Employee.age = 20;
    Employee.salary = 3200;
    strcpy(Employee.name, "Pulkit"); // using string.h library

    // printf("Name: %s\n",Employee.name);
    // printf("Age: %d\n",Employee.age);
    // printf("Salary: %.2f",Employee.salary);

    struct company Employee2 = {23, "OKEYE", 6900};
    printf("%d\n%s\n%.2f", Employee2.age, Employee2.name, Employee2.salary);
    return 0;
}
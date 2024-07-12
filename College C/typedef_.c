// used to give an alias name to datatypes
// typedef <original_name> <alias name>

#include <stdio.h>
#include <string.h>
typedef struct company
{
    int age;
    char name[32];
    float salary;
}com;//alias name 'com' given to 'struct company'

int main()
{
    // typedef unsigned long ul;
    // ul var1, var2 ,var4;


    com employee;//alias used(original can also be used)
    employee.age=56;
    strcpy(employee.name,"Pulkit");
    employee.salary=90000;
    printf("%.2f\n",employee.salary);


    //can also be used in pointers
    int* a,b;//in this statement a is a pointer integer, while b is a normal integer variable, hence we use typedef to initialize more than one pointers together

    typedef int* ptr_int;

    ptr_int var1,var2;
    int c=56;
    int d=100;
    var1=&c;
    var2=&d;

    printf("%p\n",var1);
    printf("%p",var2);
    


    return 0;
}
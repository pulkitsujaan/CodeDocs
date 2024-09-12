#include <stdio.h>
#include <math.h>
int main()
{
    float a,b,c;
    float root1,root2;
    printf("Enter the value of a,b,c for quadratic equation:\n");
    scanf("%f%f%f",&a,&b,&c);
    float discr=(b*b)-4*a*c;
    if (discr<0)
    {
        printf("Imaginary roots");
    }
    else if (discr==0)
    {
        root1=-b/(2*a);
        printf("Single root of this equation is %.2f",root1);
    }
    else{
        root1=(-b+sqrt(discr))/(2*a);
        root2=(-b-sqrt(discr))/(2*a);
        printf("Roots of this equation are %.2f and %.2f",root1,root2);
    }
    
    
    return 0;
}

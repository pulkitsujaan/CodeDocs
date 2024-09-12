#include <stdio.h>
#define PI 3.14
int main()
{
    float r;
    printf("Enter radius of the circle:");
    scanf("%f",&r);
    float area=PI*r*r;
    float circum=2*PI*r;
    printf("The area of this circle is %.2f and circumference of this circle is %.2f",area,circum);
    return 0;
}

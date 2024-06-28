#include <stdio.h>
float km_to_miles(float num)
{
    return num / 1.609;
}
float inches_to_foot(float num)
{
    return num / 12;
}
float cms_to_foot(float num)
{
    return num / 30.48;
}
float pounds_to_kgs(float num)
{
    return num / 2.205;
}
float inches_to_cms(float num)
{
    return num * 2.54;
}

int main(int argc, char const *argv[])
{
    int select;
    float num, convert;
    char choice;
    do
    {
        printf("------Conversion-------\nSelect what you want to convert:\n1.Km to Miles.\n2.Inches to Foot.\n3.Centimeter to Foot.\n4.Pounds to Kg.\n5.Inches to Centimeter.\n---:");
    scanf("%d", &select);

    // print a line which asks the user to give input in respective units
    switch (select)
    {
    case 1:
        printf("Enter value in Km:");
        break;
    case 2:
        printf("Enter value in Inches:");
        break;
    case 3:
        printf("Enter value in Centimeter:");
        break;
    case 4:
        printf("Enter value in Pounds:");
        break;
    case 5:
        printf("Enter value in Inches:");
        break;
    default:
        break;
    }

    // take input
    scanf("%f", &num);

    // conversion
    switch (select)
    {
    case 1:
        convert = km_to_miles(num);
        break;
    case 2:
        convert = inches_to_foot(num);
        break;
    case 3:
        convert = cms_to_foot(num);
        break;
    case 4:
        convert = pounds_to_kgs(num);
        break;
    case 5:
        convert = inches_to_cms(num);
        break;
    default:
        break;
    }

    // print final value
    printf("Converted unit:%.2f\n", convert);

    printf("Do you want to convert again?(y/n):");
    scanf(" %c",&choice);
    }
    while (choice=='y');
    return 0;
}
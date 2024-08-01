/*travel agency manager*/
#include <stdio.h>
#include <string.h>


typedef struct driver_details{
    char name[34];
    int DL_number;
    int route;
    float kms;
}driver;
int main()
{
    int which;
    driver dr1,dr2,dr3;//drivers inititalized
    
    //details of driver 1
    printf("Enter details of Driver 1\n",dr1.name);
    printf("Name: ");
    scanf("%s",dr1.name);
    printf("Enter DL Number: ");
    scanf(" %d",&dr1.DL_number);
    printf("Enter Route No.: ");
    scanf(" %d",&dr1.route);
    printf("Enter the number of kilometers you've driven a vehicle: ");
    scanf(" %f",&dr1.kms);

    // Details of driver 2
    printf("\nEnter details of Driver 2\n",dr2.name);
    printf("Name: ");
    scanf("%s",dr2.name);
    printf("Enter DL Number: ");
    scanf(" %d",&dr2.DL_number);
    printf("Enter Route No.: ");
    scanf(" %d",&dr2.route);
    printf("Enter the number of kilometers you've driven a vehicle: ");
    scanf(" %f",&dr2.kms);

    // details of driver 3
    printf("\nEnter details of Driver 3\n",dr3.name);
    printf("Name:");
    scanf("%s",dr3.name);
    printf("Enter DL Number: ");
    scanf(" %d",&dr3.DL_number);
    printf("Enter Route No.: ");
    scanf(" %d",&dr3.route);
    printf("Enter the number of kilometers you've driven a vehicle: ");
    scanf(" %f",&dr3.kms);

    printf("\n\nWhich driver's details do you want? ");
    scanf(" %d",&which);

    switch (which)
    {
    case 1:
        printf("Details of Driver %s\n",dr1.name);
        printf("DL Number: %d\n",dr1.DL_number);
        printf("Route: %d\n",dr1.route);
        printf("Experience: %.2fkms\n",dr1.kms);
        break;
    
    case 2:
        printf("Details of Driver %s\n",dr2.name);
        printf("DL Number: %d\n",dr2.DL_number);
        printf("Route: %d\n",dr2.route);
        printf("Experience: %.2fkms\n",dr2.kms);
        break;

    case 3:
        printf("Details of Driver %s\n",dr3.name);
        printf("DL Number: %d\n",dr3.DL_number);
        printf("Route: %d\n",dr3.route);
        printf("Experience: %.2fkms\n",dr3.kms);
        break;
    
    default:
        break;
    }
    
    return 0;
}
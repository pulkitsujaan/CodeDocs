/*		[H]			*/


/* (a)
#include<stdio.h>
int main(){
	int basic_salary;
	int gross_salary, da, rent_allowance;
	
	printf("Enter your basic salary: ");
	scanf("%d",&basic_salary);
	
	da=basic_salary/5.0;
	rent_allowance=(basic_salary*2)/5.0;
	gross_salary=basic_salary+da+rent_allowance;
	
	printf("Your gross salary is: Rs.%d\nDA: Rs.%d\nRent Allowance: Rs.%d",gross_salary,da,rent_allowance);
}
*/

/*  (b)
#include<stdio.h>
int main(){
	
	int input_dist,meter,feet,inch,cm;
	
	printf("Enter distance b/w the cities in km:\n");
	scanf("%d",&input_dist);
	
	meter=input_dist*1000;
	feet=input_dist*3281;
	inch=input_dist*39370;
	cm=input_dist*100000;
	
	printf("Distance:\nIn meters: %d m\nIn feet: %d feet\nIn inches: %d inch\nIn Centimeters: %d cm",meter, feet, inch, cm);
}
*/

/* (c)
#include<stdio.h>
int main(){
	int sub_1,sub_2,sub_3,sub_4,sub_5,
	total_marks,percentage;
	
	printf("Enter Marks obtained in 5 Subjects(Out of 100)\n");
	scanf("%d %d %d %d %d", &sub_1, &sub_2, &sub_3, &sub_4, &sub_5);
	
	total_marks=sub_1+sub_2+sub_3+sub_4+sub_5;
	percentage=total_marks/5;
	
	printf("Your total marks: %d/500\n",total_marks);
	printf("Your Percentage: %d%c",percentage,37);
}
*/

/* (d)
#include<stdio.h>
int main(){
	float temp;
	printf("Enter temperature of your city in Fahrenheit:\n");
	scanf("%f",&temp);
	temp=(temp - 32) * 5/9;
	printf("Temperature in Centigrade Degrees: %.2f",temp);
}
*/

/* (e)
#include<stdio.h>
int main(){
	float length, breadth, radius,area_rect,
	perimeter_rect,area_circle,perimeter_circle;
	
	printf("Enter Length & Breadth of Rectangle(in m): ");
	scanf("%f %f",&length,&breadth);
	
	area_rect=length*breadth;
	perimeter_rect=2*(length+breadth);
	printf("Area of Rectangle: %.2f\n",area_rect);
	printf("Perimeter of Rectangle: %.2fm\n\n",perimeter_rect);
	
	
	printf("Enter radius of circle(in cm): ");
	scanf("%f",&radius);
	
	area_circle=3.14*(radius*radius);
	perimeter_circle=2*3.14*radius;
	printf("Area of Circle: %.2f\n",area_circle);
	printf("Perimeter of Circle: %.2fcm",perimeter_circle);
	
}
*/


/* (f)
#include<stdio.h>
int main(){
	int C,D,X;
	printf("Enter two numbers: ");
	scanf("%d %d",&C,&D);
	printf("C=%d    D=%d\n",C,D);
	
	X=C;
	C=D;
	D=X;
	
	printf("C=%d    D=%d",C,D);
}
*/


/* (g)
#include<stdio.h>
int main(){
	int num,a,b,c,d,e,sum;
	printf("Enter a five digit number to find the sum of its digits: ");
	scanf("%d",&num);
	e=num%10;
	d=(num/10)%10;
	c=(num/100)%10;
	b=(num/1000)%10;
	a=(num/10000)%10;
	sum=a+b+c+d+e;
	printf("Sum of its digits: %d",sum);
}
*/


/* (h) 
#include<stdio.h>
int main(){
	int num,a,b,c,d,e,reversed;
	printf("Enter a five digit number, get it reversed: ");
	scanf("%d",&num);
	e=(num%10)*10000;
	d=((num/10)%10)*1000;
	c=(num/100)%10*100;
	b=(num/1000)%10*10;
	a=(num/10000)%10;
	reversed=a+b+c+d+e;
	printf("Reversed Number: %d",reversed);
}
*/

/* (i)
#include<stdio.h>
int main(){
	int num,a,b,sum;
	printf("Enter a four digit number to get sum of first and last digit of the number: ");
	scanf("%d",&num);
	b=(num%10);
	a=num/1000;
	sum=a+b;
	printf("Sum: %d",sum);
}
*/

/* (j)
#include<stdio.h>
int main(){
	int total_population=80000;
	
	int total_men=52.0/100*total_population;
	int total_women=total_population-total_men;

	int total_literate=48.0/100*total_population;
	int total_illiterate=total_population-total_literate;
	
	int men_literate=35.0/100*total_population;
	int women_literate=total_literate-men_literate;
	
	int men_illiterate=total_men-men_literate;
	int women_illiterate=total_women-women_literate;
	
	printf("Total Population: %d\n\n",total_population);
	printf("Total Illiterate Men: %d\n",men_illiterate);
	printf("Total Illiterate Women: %d",women_illiterate);
	
}
*/

/* (k)
#include<stdio.h>
int main(){
	int amount_withdrawn;//let it be 670
	printf("Enter amount of money to get denominations in 10, 50, 100: ");
	scanf("%d",&amount_withdrawn);
	
	
	int note_100=amount_withdrawn/100;//670/100----6 notes of 100rs
	int note_10=((amount_withdrawn-(note_100*100))%50)/10;//((670-(6*100))%50)----1 note of 50rs
	int note_50=(amount_withdrawn-((note_100*100)+(note_10*10)))/50;//((670-((6*100)+(1*10)))/50----2 notes of 10rs
	
	printf("Rs.100 notes: %d\n",note_100);
	printf("Rs.50 notes: %d\n",note_50);
	printf("Rs.10 notes: %d",note_10);
}
*/


/* (l)
#include<stdio.h>
int main(){
	float total_SP,profit,total_CP,cost;
	printf("Enter the total selling price of 15 items: ");
	scanf("%f",&total_SP);
	printf("Enter the profit earned: ");
	scanf("%f",&profit);
	
	total_CP=total_SP-profit;
	cost=total_CP/15.0;
	printf("Cost of one item: %.2f",cost);
}
*/


/* (m)
#include<stdio.h>
int main(){
	int num,a,b,c,d,e,final_num;
	printf("Enter a five digit number: ");
	scanf("%d",&num);
	e=((num%10)+1);
	d=(((num/10)%10)+1)*10;
	c=(((num/100)%10)+1)*100;
	b=(((num/1000)%10)+1)*1000;
	a=(((num/10000)%10)+1)*10000;
	final_num=a+b+c+d+e;
	printf("New Number: %d",final_num);
}
*/

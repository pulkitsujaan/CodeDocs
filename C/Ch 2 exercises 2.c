/* Exercises */
/* [C] */
////(a)
//#include<stdio.h>
//int main(){
//	float cp,sp;
//	printf("Enter CP and SP: ");
//	scanf("%f %f",&cp,&sp);
//	if(cp>sp)
//		printf("You made a loss of Rs.%.2f",cp-sp);
//	else
//		printf("You made a profit of Rs.%.2f",sp-cp);
//}


////(b)
//#include<stdio.h>
//int main(){
//	int num;
//	printf("Enter a number: ");
//	scanf("%d",&num);
//	if(num%2==0)
//		printf("Even Number");
//	else
//		printf("Odd Number");
//}


////(c)
//#include<stdio.h>
//int main(){
//	int year;
//	printf("Enter any year to check it's a leap year or not: ");
//	scanf("%d",&year);
//	if(year%4==0)
//		printf("Leap Year")	;
//	else
//		printf("Not a Leap year");
//}


////(e)
//#include<stdio.h>
//int main(){
//	int num,a,b,c,d,e,reverse;
//	printf("Enter a five digit number: ");
//	scanf("%d",&num);
//	e=(num%10)*10000;
//	d=((num/10)%10)*1000;
//	c=((num/100)%10)*100;
//	b=((num/1000)%10)*10;
//	a=num/10000;
//	
//	reverse=e+d+c+b+a;
//	printf("Reversed: %d",reverse);
//	
//	if (reverse==num){
//		printf("\nReversed and original numbers are equal");
//	}
//}

////(f)
//#include<stdio.h>
//int main(){
//	int ram,shyam,ajay;
//	printf("Enter ages of Ram, Shyam, and Ajay: ");
//	scanf("%d %d %d",&ram, &shyam, &ajay);
//	
//	if(ram<shyam && ram<ajay)
//		printf("Ram is the Youngest");
//	else if(shyam<ram && shyam<ajay)
//		printf("Shyam is the Youngest");
//	else
//		printf("Ajay is the Youngest");
//		
//	
//	
//}


////(g)
//#include<stdio.h>
//int main()
//{
//	int a,b,c;
//	printf("Enter the angles of a Triangle: ");
//	scanf("%d %d %d",&a,&b,&c);
//	if ((a+b+c)==180)
//		printf("Triangle is Valid");
//	else
//		printf("Triangle is not valid");
//}


////(h)
//#include<stdio.h>
//int main(){
//	int num;
//	printf("Enter a number to find its absolute value: ");
//	scanf("%d",&num);
//	if (num<0)
//		printf("Absolute value: %d",num*(-1));
//	else
//		printf("Absolute value: %d",num);
//}


////(i)
//#include<stdio.h>
//int main(){
//	int length,breadth,peri,area;
//	printf("Enter length and breadth of the rectangle: ");
//	scanf("%d %d",&length,&breadth);
//	peri=2*(length+breadth);
//	area=length*breadth;
//	if(area>peri)
//		printf("Area is greater than the perimeter");
//	else if(area<peri)
//		printf("Area is smaller than the perimeter");
//	else
//		printf("Area is equal to the perimeter");
//}


////(j)
//#include<stdio.h>
//int main(){
//	int x1,y1, x2,y2, x3,y3;
//	printf("Enter the coordinates(seperated with commas): ");
//	scanf("%d,%d %d,%d %d,%d",&x1,&y1,&x2,&y2,&x3,&y3);
//	printf("Coordinates: (%d,%d), (%d,%d), (%d,%d)\n",x1,y1,x2,y2,x3,y3);
//	if ((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))==0)
//		printf("Collinear!");
//	else
//		printf("Not Collinear");
//}


////(k)
//#include<stdio.h>
//#include<math.h>
//int main(){
//	int radius, xc,yc, xo, yo,length_of_ex;
//	printf("Enter coordinates of center, external point and the radius: ");
//	scanf("%d,%d %d,%d %d",&xc,&yc,&xo,&yo,&radius);
//	
//	printf("Centre: (%d,%d), Point Coordinates:(%d,%d)\nRadius: %d cm\n",xc,yc,xo,yo,radius);
//	length_of_ex=sqrt(pow((xc-xo),2)+pow((yc-yo),2));
//	if (length_of_ex>radius)
//		printf("Point is outside the circle.");
//	else if(length_of_ex<radius)
//		printf("Point is inside the circle.");
//	else
//		printf("Point is on the circle");
//}


////(l)
//#include<stdio.h>
//int main(){
//	int x,y;
//	printf("Enter the coordinates: ");
//	scanf("%d,%d",&x,&y);
//	
//	if(x==0 && y!=0){
//		printf("Point on y-axis");
//	}
//	else if(x!=0 && y==0)
//		printf("Point on x-axis");
//	else if(x==0 && y==0)
//		printf("Point on origin");
//	
//}

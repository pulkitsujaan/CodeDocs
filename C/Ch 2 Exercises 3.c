/*

Logical Operators

*/

// [D]

////(c)
//#include<stdio.h>
//int main(){
//	int i=4,j=-1,k=0,w,x,y,z;
//	w=i||j||k;
//	x=i&&j&&k;
//	y=i||j&&k;
//	z=i&&j||k;
//	printf("\nw=%d x=%d y=%d z=%d",w,x,y,z);
//}

////(d)
//#include<stdio.h>
//int main(){
//	int i=4,j=-1,k=0,y,z;
//	y=i+5&&j+1||k+2;
//	z=i+5||j+1&&k+2;
//	printf("\ny=%d z=%d",y,z);
//}

////(e)
//#include<stdio.h>
//int main(){
//	int i=-3,j=3;
//	if(!i + !j *1)
//		printf("\nMassaro");
//	else
//		printf("\nBennarivo");
//}


/* [G] */
////(a)
//#include<stdio.h>
//int main(){
//	int year;
//	printf("Enter any year ");
//	scanf("%d",&year);
//	if((year%4==0 || year%400==0) && year%7!=0)
//		printf("Leap Year!");
//	else
//		printf("Not a leap Year");
//}


////(b)
//#include<stdio.h>
//int main(){
//	char any;
//	printf("Enter anything: ");
//	scanf("%c",&any);
//	
//	if(any>=65 && any<=90)
//		printf("Capital letter!");
//	else if(any>=97 && any<=122)
//		printf("Small letter!");
//	else if(any>=48 && any<=57)
//		printf("A number!");
//	else if((any>=0 && any<=47) || (any>=58 && any<=64) || (any>=91 && any<=96) || any>=123 && any<=127)
//		printf("A Special Symbol");
//	else
//		printf("Wrong Input");
//	
//}



////(c)
//#include<stdio.h>
//int main(){
//	int hard,tensile;
//	float carbon;
//	printf("Enter Hardness, Carbon content, Tensile strength:\n");
//	scanf("%d %f %d",&hard,&carbon,&tensile);
//	if(hard>50 && carbon<0.7 && tensile>5600)
//		printf("Grade: 10");
//	else if(hard>50 && carbon<0.7 && !tensile>5600)
//		printf("Grade: 9");
//	else if(!hard>50 && carbon<0.7 && tensile>5600)
//		printf("Grade: 8");
//	else if(hard>50 && !carbon<0.7 && tensile>5600)
//		printf("Grade: 7");
//	else if(hard>50 || carbon<0.7 || tensile>5600)
//		printf("Grade: 6");
//	else if(!hard>50 && !carbon<0.7 && !tensile>5600)
//		printf("Grade: 5");
//}



////(d)
//#include<stdio.h>
//int main(){
//	int late;
//	printf("Enter the number of days you\'re late to return: ");
//	scanf("%d",&late);
//	if(late>0 && late<=5)
//		printf("Your fine is 50p");
//	else if(late>=6 && late<=10)
//		printf("Your fine is 1Rs.");
//	else if(late>=10 && late<=30)
//		printf("Your fine is 5Rs.");
//	else if(late>30)
//		printf("Your membership is cancelled....Fuck off!");
//}


////(e)
//#include<stdio.h>
//int main(){
//	int a,b,c;
//	printf("Enter the sides of triangle: ");
//	scanf("%d %d %d",&a,&b,&c);
//	if((a>=b && a>=c) && (a<(b+c)))
//		printf("Triangle Valid!!");
//	else if((b>=c && b>=a) && (b<(a+c)))
//		printf("Triangle Valid!!");
//	
//	else if((c>=b && c>=a) && (c<(a+b)))
//		printf("Triangle Valid!!"); 
//	else
//		printf("Triangle Not valid");
//}



////(f)
//#include<stdio.h>
//int main(){
//	int ab,bc,ca;
//	printf("Enter the sides of triangle: ");
//	scanf("%d %d %d",&ab,&bc,&ca);
//	
//	
//	if((ab==bc) && (bc==ca) && (ca==ab))
//		printf("Equilateral triangle\n");
//	
//	if((ab!=bc) && (bc!=ca) && (ca!=ab))
//		printf("Scalene triangle\n");
//	
//	if(((ca*ca)==((ab*ab)+(bc*bc))) || 
//	((ab*ab)==(bc*bc)+(ca*ca)) || 
//	((bc*bc)==(ab*ab)+(ca*ca)))
//		printf("Right angled Triangle\n");
//	
//	if (((ab==bc)&&(bc!=ca && ab!=ca)) || 
//	((ab==ca)&&(ab!=bc && ca!=bc)) || 
//	((bc==ca)&&(bc!=ab && ca!=ab)))
//		printf("Isosceles triangle");
//}



////(g)
//#include<stdio.h>
//int main(){
//	float time;
//	printf("Enter the time taken(in mins) by the employee to complete the work: ");
//	scanf("%f",&time);
//	
//	time=time/60.0;
//	
//	if(time<3)
//		printf("Jai ho prabhu! Bahut mast kaam krta h re tu!");
//	else if(time>=3 && time<4)
//		printf("Speed improve kijiye thoda!");
//	else if(time>=4 && time<5)
//		printf("Kal se speed classes me aa jana!");
//	else if(time>5)
//		printf("Fuck off! You\'re fired from our company!!");
//}


////(h)
//#include<stdio.h>
//int main(){
//	int stock=10000,order;
//	char credit;
//	printf("Enter the order quantity: ");
//	scanf("%d",&order);
//	printf("Is your credit OK(y/n)? ");
//	scanf("\n%c",&credit);
//	
//	if(order<=stock && credit=='y')
//		printf("Your Requirement is coming soon at your doorstep!");
//	else if(credit=='n')
//		printf("We will be right back to you!");
//	else if(credit=='y' && order>stock)
//		printf("We will deliver the stock in 10 days");
//}



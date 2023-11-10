#include<stdio.h>
int main(){
	/*while loop*/
	
	
	/*  [A]  */
	/*(a)
	int i=1;
	while(i<=10);
	{
		printf("\n%d",i);
		i++;
	}
	*/
	
	/*(b)
	int x=4;
	while(x==1)
	{
		x-=1;
		printf("\n%d",x);
		--x;
	}
	*/
	
	/*(c)
	int x=4,y,z;
	y=--x;
	z=x--;
	printf("\n%d %d %d",x,y,z);
	*/
	
	/*(d)
	int x=4,y=3,z;
	z=x-- -y;
	printf("\n%d %d %d",x,y,z);
	*/
	
	/*(e)
	while('a'<'b')
		printf("\nMalayalam is a pallindrom");
	*/
	
	/*[B]*/
	//(a)
	/*
	int hour,employee,pay;
	while(employee<=10)
	{
		printf("Enter no. of hours you worked: ");
		scanf("%d",&hour);
		hour-=40;
		pay=hour*12;
		if (hour<=0)
		{
			printf("No overtime pay...\n");
			employee++;
		}
		else
		{
			printf("Overtime Payed: %d\n",pay);
			employee++;
		}
	}
	*/
	
	//(b)
	/*
	int num,fact=1;
	printf("Enter number to find the factorial: ");
	scanf("%d",&num);
	while(num>0)
	{
		fact*=num;
		num--;
	}
	printf("Factorial: %d",fact);
	*/
	
	
	//(c)
	/*
	int base,power,num=1;
	printf("Enter two numbers(base and power respectively): ");
	scanf("%d %d",&base,&power);
	while(power>0)
	{
		num*=base;
		power--;
	}
	printf("Result: %d",num);
	*/
	
	
	//(d)
	/*
	int value=0;
	while(value<=255)
	{
		printf("%d %c\n",value,value);
		value++;
	}
	*/
	//(e)
	/*
	int count=1,rem,num,sum;
	while(count<=500)
	{
		num=count;
		sum=0;
		while(num)
		{
			rem=num%10;
			sum +=(rem*rem*rem);
			num/=10;
		}
		if(count==sum)
			printf("%d is an Armstrong Number\n",sum);
		count++;
	}
	*/
	
	//(f)
	/*
	int matches=21,comp,user;
	while(1)
	{
		printf("\nPick 1,2,3, or 4 matchsticks: ");
		scanf("%d",&user);
		if(user>4){
			printf("Invalid Choice.");
			break;
		}
		comp=5-user;
		printf("\nComputer Choosed %d Match(es)\n",comp);
		matches-=comp+user;
		printf("Matches remaining: %d\n",matches);
		if(matches==1)
		{
			printf("\nYou lost!\n");
			break;
		}
	}
	*/
	//(g)
	/*
	int pos=0,zero=0,neg=0,num;
	char choice='y';
	while(choice=='y'){
		printf("Enter a number: ");
		scanf("%d",&num);
		if(num>0)
			pos++;
		else if(num<0)
			neg++;
		else
			zero++;
		
		printf("Do you want to enter another number?(y/n) ");
		scanf(" %c",&choice);
	}
	printf("\nPositve Numbers: %d\nNegative Numbers: %d\nZeroes: %d",pos,neg,zero);
	*/
	
	//(h)
	/*
	int num,rem,oct=0,pow=1;
	printf("Enter a number: ");
	scanf("%d",&num);
	if(num<8)
		printf("%d",num);
	else if(num%8==0){
		oct=num/8;
		oct*=10;
	}
	else
	{
		while(num>8){
	    oct+= (num%8)*pow; 
	    num/=8;
	    pow*=10;
		} 
	}
	oct+=num*pow;
	printf("Octal Equivalent: %d",oct);
	*/
	
	//(i)
	
}


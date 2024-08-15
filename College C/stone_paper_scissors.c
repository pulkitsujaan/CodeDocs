/*Stone paper Scissors*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>


int GenRandNum(int n){
    srand(time(NULL));
    return rand()%n;
}

int main()
{
    int compscore=0, userscore=0;
    char userchoice, comp_choice;

    printf("ROCK - PAPER - SCISSORS\n\n\tr-rock\n\tp-paper\n\ts-scissors\n\n");
    for (int i = 0; i < 3; i++)
    {
        printf("Rock/Paper/Scissors: ");
        scanf("%c",&userchoice);
        getchar();
        comp_choice=GenRandNum(3);//0--rock, 1--paper, 2--scissors
        if ((userchoice=='r' && comp_choice==0) || (userchoice=='p' && comp_choice==1)||(userchoice=='s' && comp_choice==2))
        {
            printf("It's a Draw!\n");
        }
        else if ((userchoice=='r' && comp_choice==1))
        {
            printf("Computer Wins!(Computer choice:paper)\n");
            compscore++;

        }
        else if ((userchoice=='r' && comp_choice==2))
        {
            printf("User wins(Computer choice:scissors)\n");
            userscore++;
        }
        else if ((userchoice=='p' && comp_choice==0))
        {
            printf("User Wins!(Computer choice:rock)\n");
            userscore++;
        }
        else if ((userchoice=='p' && comp_choice==2))
        {
            printf("Computer wins!(Computer choice:scissors)\n");
            compscore++;
        }
        else if ((userchoice=='s' && comp_choice==0))
        {
            printf("Computer wins!(Computer choice:rock)\n");
            compscore++;
        }
        else if ((userchoice=='s' && comp_choice==1))
        {
            printf("User wins!(Computer choice:paper)\n");
            userscore++;
        }
    }
    if (userscore==compscore)
    {
        printf("DRAW!!");
    }
    else if (userscore>compscore)
    {
        printf("\nUser wins the Game(Total points: %d)",userscore);
    }
    else{
        printf("\nComputer wins the Game(Total points: %d)",compscore);
    }
    


    return 0;
}
/*
HTML Parser

input:
<h1>This is a heading.</h1>

Output:
This is a heading.


*/

#include <stdio.h>
#include <string.h>

void parser(char string[])
{
    int in = 0;
    int index = 0;

    // This loop removes the html tags from the string
    for (int i = 0; i < strlen(string); i++)
    {
        if (string[i] == '<')
        {
            in = 1;
            continue;
        }
        else if (string[i] == '>')
        {
            in = 0;
            continue;
        }
        if (in == 0)
        {
            string[index] = string[i];
            index++;
        }
    }
    string[index] = '\0';

    // Removing whitespaces from the string
    while (string[0] == ' ')
    {
        for (int i = 0; i < strlen(string); i++)
        {
            string[i] = string[i + 1];
        }
    }
    while (string[strlen(string) - 1] == ' ')
    {
        string[strlen(string) - 1] = '\0';
    }
}

int main()
{
    char string[50];
    gets(string);
    parser(string);
    printf(" Parsed:%s", string);
    return 0;
}
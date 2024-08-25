#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *replaceWord(const char *str, const char *oldWord, const char *newWord)
{
    char *resultString;
    int i = 0, count = 0;
    int oldWordLength = strlen(oldWord);
    int newWordLength = strlen(newWord);

    // counting number of occurences of old word
    for(i=0;str[i]!='\0';i++)
    {
        if ((strstr(&str[i], oldWord)) == &str[i])
        {
            count++;
            i = i+oldWordLength-1;
        }
    }
    // making a new string to fit in the replaced words
    resultString = (char *)malloc(i + count * (newWordLength - oldWordLength) + 1);

    i = 0;
    while (*str)
    {
        // compare the substring with result
        if (strstr(str, oldWord) == str)
        {
            strcpy(&resultString[i], newWord);
            i += newWordLength;
            str += oldWordLength;
        }
        else
        {
            resultString[i] = *str;
            i++;
            str++;
        }
    }
    resultString[i] = '\0';
    return resultString;
}
int main()
{
    FILE *ptr = NULL;
    FILE *ptr2 = NULL;
    ptr = fopen("bill.txt", "r");
    ptr2 = fopen("genbill.txt", "w");

    char str[200];
    fgets(str, 200, ptr);
    printf("The bill template is: %s\n", str);

    // call function replaceWord and generate bill
    char *newStr;
    newStr = replaceWord(str, "{{Name}}", "Aujla");
    newStr = replaceWord(newStr, "{{Product}}", "iPhone");
    newStr = replaceWord(newStr, "{{City}}", "Meerut");
    fprintf(ptr2, newStr);
    printf("The generated bill is: %s\n", newStr);

    fclose(ptr);
    fclose(ptr2);
    return 0;
}
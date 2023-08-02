#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int get_letters(string s);
int get_words(string s);
int get_sentences(string s);
int cli(int letters, int words, int sentances);


int main(void)
{
    //Read a string from user
    string s = get_string("Enter a string: ");
    //number of letters
    int letters = get_letters(s);
    //number of words
    int words = get_words(s);
    //number of sentances
    int sentances = get_sentences(s);
    //Coleman-Liau index (CLI)
    int index = cli(letters, words, sentances);


    if (index <= 1)
    {
        //if indes is less than 1 we output "Before Grade 1"
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        //if index is 16 or higher we output "Grade 16+"
        printf("Grade 16+\n");

    }
    else
    {
        //If grade is less than 16 and higer than 1 we output "Grade "+ index
        printf("Grade %i\n", index);
    }
}


int get_letters(string s)
{
    // counts the number of letters
    int l = strlen(s);
    int i, cont = 0;
    for (i = 0; i < l ; i++)
    {
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
        {
            cont++;

        }
    }
    return cont;
}
int get_words(string s)
{
    // counts the number of words
    int l = strlen(s);
    int i, cont = 1;
    for (i = 0 ; i < l; i++)
    {
        if (s[i] == ' ')
        {
            cont++;

        }
    }
    return cont;
}

int get_sentences(string s)
{
    // counts the number of sentances
    int l = strlen(s);
    int i, cont = 0;
    for (i = 0 ; i < l; i++)
    {
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            cont++;

        }
    }
    return cont;
}

int cli(int letters, int words, int sentances)
{
    //calculates Coleman-Liau index (CLI)
    float L = letters / (float) words * 100;
    float S = sentances / (float) words * 100;
    int index = (int) round(0.0588 * L - 0.296 * S - 15.8);
    return index;

}
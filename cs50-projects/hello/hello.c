#include <stdio.h>
#include <cs50.h>
#include <ctype.h>

int main(void)
{
    char *word = get_string("enter: ");
    unsigned int val = (toupper(word[0]) - 'A');
    printf("%i\n" , val);
}
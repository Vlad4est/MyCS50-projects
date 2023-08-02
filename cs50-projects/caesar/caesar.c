#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool is_number(string s);

int main(int argc, string argv[])
{
    int key = 0;
    //check if we get only one argument after ./caesar
    if (argc > 2 || argc < 2)
    {
        //exit with code 1 if user entered more than one argument afrer ./caesar
        return 1;
    }

    if (is_number(argv[1]) == true)
    {
        //if first argument  is a number convert it to int and attribute it to key
        key = atoi(argv[1]);
    }
    else
    {
        //exit with code 1 if first argument is not a number
        return 1;
    }
    string message = get_string("plaintext: ");
    char encrypted[100];
    int i;
    for (i = 0 ; i < strlen(message); i++)
    {
        if (message[i] >= 'A' &&  message[i] <= 'Z')
        {
            char c = (key + message[i] - 65) % 26 + 65;

            encrypted[i] = c;
        }
        else if (message[i] >= 'a' &&  message[i] <= 'z')
        {
            char v = (key + message[i] - 97) % 26 + 97;
            encrypted[i] = v;
        }
        else
        {
            encrypted[i] = message[i];
        }

    }
    encrypted[i] = '\n';

    printf("ciphertext: %s\n", encrypted);

}

bool is_number(string s)
{
    //check if string s contains only digits (is number)
    int i;
    for (i = 0; i < strlen(s); i++)
    {
        if (!(s[i] <= '9' && s[i] >= '0'))
        {
            //return false if s dosen't have all characters from 0 - 9 (all digits)
            return false;
        }
    }
    //return true if s is a number
    return true;

}

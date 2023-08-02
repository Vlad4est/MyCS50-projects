// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1000;
int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int k = hash(word);
    node *cursor;
    cursor = table[k];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{

    unsigned int val = 0 ;
    int i = 0;
    while (word[i] != '\0')
    {
        val += (int)toupper(word[i]) * (100 + i);
        i++;
    }
    return val % 1000;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    char word[LENGTH + 1];

    if (file == NULL)
    {
        //if file is inalid return false
        return false;
    }
    int i;
    for (i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    //while we don't reach end of file read from file
    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        int k = hash(word);
        //get key value by hasing the word

        strcpy(n->word, word);
        if (table[k] == NULL)
        {
            n->next = NULL;
            table[k] = n;
        }
        else
        {
            n->next = table[k];
            table[k] = n;
        }
        count++;
    }

    fclose(file);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{

    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *cursor;
    node *tmp;
    int i;
    for (i = 0; i < N; i++)
    {
        cursor = table[i];
        while (cursor != NULL)
        {
            //use a temporay pointer to free the memory at cursor - 1 position
            tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }

    }
    return true;
}

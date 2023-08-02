#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do{
    n = get_int("How tall(1-8)?: ");
    } while(n <= 0 || n > 8);

    char table[100][100];
    int i,j;
    for(i=0;i < n;i++)
    {
    for(j=0;j<n;j++)
    {
        //checking if table[i][j] is on secondary diagonal or bellow it
        if(i + j == n - 1 || i + j > n - 1)
        {
            table[i][j] = '#';
        }
        else
        {
            table[i][j] =' ';
        }
    }

    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%c", table[i][j]);
        }
        printf("\n");
    }


}
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include<stdbool.h>

typedef uint8_t BYTE;

#define BLOCKSIZE 512

bool isJPG(BYTE buffer[BLOCKSIZE]);


int main(int argc, char *argv[])
{
    FILE *file = fopen(argv[1], "r");
    BYTE buffer[BLOCKSIZE];
    //error out if file is not valid
    if (file == NULL)
    {
        return 1;
    }


    char filename[8];
    int count = 0;
    FILE *img;

    //we loop trought file while we didn't reach end of file
    while (fread(buffer, 1, BLOCKSIZE, file) == BLOCKSIZE)
    {
        if (isJPG(buffer))
        {
            //if we find a jpg header create a new file and start writeing block after block until we find a new jpg header
            sprintf(filename, "%03i.jpg", count);
            if (count > 0)
            {
                //if we find a new jpg header(that isn't the first) we close img file to avoid memory leak 
                fclose(img);
            }

            img = fopen(filename, "w");
            fwrite(buffer, 1, BLOCKSIZE, img);
            count ++;

        }
        else if (count > 0)
        {
            //if we dont find a new jpg header we keep writeing to the same file
            fwrite(buffer, 1, BLOCKSIZE, img);
        }

    }
    //close files to avoid memory leak
    fclose(img);
    fclose(file);
}


bool isJPG(BYTE buffer[BLOCKSIZE])
{
    //check if first 4 bytes in buffer are jpg header
    if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
    {
        return true;
    }
    return false;
}



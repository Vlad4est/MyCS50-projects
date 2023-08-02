#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    /*
    BYTE  rgbtBlue;
    BYTE  rgbtGreen;
    BYTE  rgbtRed;
    */
    int i, j;
    int mean;
    for (i = 0; i < height; i++)
    {
        mean = 0;
        for (j = 0; j < width; j++)
        {
            //calculate the medium value and assign it to each colour(blue,red,green)
            mean = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = mean;
            image[i][j].rgbtGreen = mean;
            image[i][j].rgbtRed = mean;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int i, j;

    int sepiaRed, sepiaGreen, sepiaBlue;
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            //calculate sepia values for each colour(Blue,Red,Green)
            sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            //if value is bigger then 255 assign it tge value 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            //if value is bigger then 255 assign it tge value 255

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;


        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int i, j;
    RGBTRIPLE aux;
    for (i = 0; i < height; i++)
    {
        //switch each pixel from each line (mirror like)
        for (j = 0; j < width / 2; j++)
        {
            aux = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = aux;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    /*
    BYTE  rgbtBlue;
    BYTE  rgbtGreen;
    BYTE  rgbtRed;
    */
    int i, j, x, y;
    RGBTRIPLE copyImage[height][width];
    int mRed, mGreen, mBlue, cont;


    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            mRed = 0;
            mGreen = 0;
            mBlue = 0;
            cont = 0;


            //for each pixel loop from i-1 to i+1 and j-1 to j+1 (3x3 square if not on the border) and calculate the medium value for RGB and assign it to original pixel
            for (x = i - 1; x < i + 2; x++)
            {
                for (y = j - 1; y < j + 2; y++)
                {
                    if (x < 0 || y < 0 || x > height - 1  ||  y > width - 1)
                    {
                        continue;
                    }
                    mRed += image[x][y].rgbtRed;
                    mGreen += image[x][y].rgbtGreen;
                    mBlue += image[x][y].rgbtBlue;
                    cont ++;
                }
            }
            copyImage[i][j].rgbtRed = round(mRed / (float)cont);
            copyImage[i][j].rgbtGreen = round(mGreen / (float)cont);
            copyImage[i][j].rgbtBlue = round(mBlue / (float)cont);

        }
    }

    //transfer copyImage back to image
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            image[i][j] = copyImage[i][j];
        }
    }



    return;
}

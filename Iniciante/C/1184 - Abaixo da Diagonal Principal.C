#include <stdio.h>
int main()
{
float M[12][12],soma,media;
int i,x,j;
char a;
scanf("%c",&a);
soma=0;
x=0;
    for (i=0;i<12;i++)
    {
        for (j=0;j<12;j++)
        {
        scanf("%f",&M[i][j]);
        if (x > j )
        {
             soma = soma + M[i][j];
        }

        }
        x++;
    }
    if (a == 'S')
    {
            printf("%.1f\n",soma);
    }
    else if (a == 'M')
    {
            media = soma/66;
            printf("%.1f\n",media);
    }

    else
    return 0;
}

#include <stdio.h>
int main()
{
double M[12][12],soma,media;
int i,x,y,j;
char a;
scanf("%c",&a);
soma=0;
x=0;
y=11;
    for (i=0;i<12;i++)
    {
        for (j=0;j<12;j++)
        {
        scanf("%lf",&M[i][j]);
        if (x < j && j < y)
        {
             soma = soma + M[i][j];
        }
        }
        x++;
        y--;
    }
    if (a == 'S')
    {
            printf("%.1lf\n",soma);

    }
    else if (a == 'M')
    {
            media = soma/30.0;
            printf("%.1lf\n",media);

    }

    else
    return 0;
}

#include <stdio.h>
int main()
{
float M[12][12],soma,media;
int i,x,j;
char a;
scanf("%d %c",&x,&a);
soma=0;
    for (i=0;i<12;i++)
    {
        for (j=0;j<12;j++)
        {
        scanf("%f",&M[i][j]);
        if (M[x][j] == M[i][j])
        {
             soma = soma + (M[i][j]);
        }
        }

    }
    if (a == 'S')
    {
            printf("%.1f\n",soma);

    }
    else if (a == 'M')
    {
            media = soma/12;
            printf("%.1f\n",media);

    }

    else
    return 0;
}

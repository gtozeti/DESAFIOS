#include <stdio.h>
int main()
{
float n1,n2,n3,n4,n5,n6,media,soma;
int x;
x=0;
soma=0;
scanf("%f %f %f %f %f %f",&n1,&n2,&n3,&n4,&n5,&n6);
    if(n1>0)
    {
        soma=soma+n1;
        x++;
    }
    if(n2>0)
    {
        soma=soma+n2;
        x++;
    }
    if(n3>0)
    {
        soma=soma+n3;
        x++;
    }
    if(n4>0)
    {
        soma=soma+n4;
        x++;
    }
    if(n5>0)
    {
        soma=soma+n5;
        x++;
    }
    if(n6>0)
    {
        soma=soma+n6;
        x++;
    }
    media=soma/x;
    printf("%d valores positivos\n%.1f\n",x,media);
    return 0;
}

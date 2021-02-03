#include <stdio.h>
int main()
{
int x[10],i,a;

 scanf("%d",&a);

    for (i=0;i<10;i++)
    {

            x[i]= a;
            a = a*2;

    }
     for (i=0;i<10;i++)
    {
        printf("N[%d] = %d\n",i,x[i]);
    }

    return 0;
}

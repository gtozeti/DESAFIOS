#include <stdio.h>
int main()
{
float x[100];
int i,a;

     for (i=0;i<100;i++)
    {
        scanf("%f",&x[i]);
    }
     for (i=0;i<100;i++)
    {
        if(x[i]<=10)
        {
        printf("A[%d] = %.1f\n",i,x[i]);
        }
    }

    return 0;
}

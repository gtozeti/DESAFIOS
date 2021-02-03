#include <stdio.h>
int main()
{
double x[100],a;
int i;

 scanf("%lf",&a);

    for (i=0;i<100;i++)
    {

            x[i]= a;
            a = a/2;
            printf("N[%d] = %.4lf\n",i,x[i]);

    }
    return 0;
}

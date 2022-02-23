#include <stdio.h>
int main()
{
int n1,n2,x;
x=0;
for (n1=1;n1<=5;n1++)
{
scanf("%d",&n2);
    if(n2%2==0)
    {
        x++;
    }
}
printf("%d valores pares\n",x);
return 0;
}

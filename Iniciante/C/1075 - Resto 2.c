#include <stdio.h>
int main()
{
int n1,x,resto,y;
scanf("%d",&n1);

    for (x=1;x<10000;x++)
    {
        resto=x%n1;
        if(resto==2)
            {
                printf("%d\n",x);
            }
    }
    return 0;
}

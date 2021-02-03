#include <stdio.h>
int main()
{
int x,a;
    for (a=0; ;a++)
    {
        scanf("%d",&x);
        if(x==2002)
            {
                printf("Acesso Permitido\n");
                break;
            }
            else
            {
                printf("Senha Invalida\n");
            }
    }
    return 0;
}

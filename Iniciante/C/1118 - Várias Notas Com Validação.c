#include <stdio.h>
int main()
{
float p1,p2,media;
int a,opcao;
verificar:
    for (a=0; ;a++)
    {
        scanf("%f",&p1);
        if(p1 < 0 || p1 > 10)
            {
              printf("nota invalida\n");
            }
            else
            {
                break;
            }
    }
    for (a=0; ;a++)
    {
        scanf("%f",&p2);
        if(p2 < 0 || p2 > 10)
            {
              printf("nota invalida\n");
            }
            else
            {
                break;
            }
    }
    media = (p1+p2)/2;
    printf("media = %.2f\n",media);
msg:
    printf("novo calculo (1-sim 2-nao)\n");
    scanf("%d",&opcao);
    switch (opcao)
    {
        case 1: goto verificar;
                break;
        case 2: break;
        default: goto msg;
    }
    return 0;
}

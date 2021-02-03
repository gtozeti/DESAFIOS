#include <stdio.h>
int main() {

char t;
int l, i, j,z = 11;
double s = 0.0, x[12][12];
scanf("%c", &t);

for (i = 0; i <= 11; i++)
  {
  for (j = 0; j <= 11; j++)
    {
      scanf("%lf", &x[i][j]);
      if (j > z)
      s +=x[i][j];
    }
    if (i < 5)
    z--;
    else if(i>=6)
    z++;
  }
  
if (t == 'S')
    printf("%.1f\n", s);
else
    printf("%.1f\n", s / 30);
return 0;
}

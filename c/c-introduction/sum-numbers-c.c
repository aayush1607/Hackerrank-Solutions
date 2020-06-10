#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a,b,c1,c2;
    float x,y,z1,z2;
    scanf("%d %d",&a,&b);
    scanf("%f %f",&x,&y);
    c1=a+b;
    c2=a-b;
    z1=x+y;
    z2=x-y;
    printf("%d %d\n",c1,c2);
    printf("%0.1f %0.1f",z1,z2);
    
    return 0;
}



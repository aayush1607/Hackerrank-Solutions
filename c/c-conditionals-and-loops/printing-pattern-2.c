#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n,i,j,l,min;
    scanf("%d", &n);
    l=(2)*n-1;
    for(i=0;i<l;i++){
        for(j=0;j<l;j++){
            min=i<j?i:j;
            min=min<(l-j-1)?min:l-j-1;
            min=min<(l-i-1)?min:(l-i-1);
            printf("%d ",n-min);
        }
        printf("\n");
    }
  	
    return 0;
}



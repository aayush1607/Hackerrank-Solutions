#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i=0,j,l,k,c[10];
    char s[1000],com[]="0123456789";
    scanf("%s",s);
    l=strlen(s);
    for(i=0;i<10;i++)
    {
         k=0;
        for(j=0;j<l;j++)
        {
            if(com[i]==s[j])
            {
                k+=1;
            }

        c[i]=k;
        } 
    }
    for(i=0;i<10;i++)
    {
        printf("%d ",c[i]);
    }
    return 0;
}


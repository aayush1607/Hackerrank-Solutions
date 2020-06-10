#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<cstdio>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   

    int n,q,k,l,o,p;
    scanf("%d %d",&n,&q);
    vector<int> v[n];
    for(int i=0;i<n;i++)
    {
    
        scanf("%d",&k);
    
        for(int j=0;j<k;j++)
        {
            scanf("%d",&l);
            v[i].push_back(l);
        }
        
    }
    for(int i=0;i<q;i++)
    {
        scanf("%d %d",&o,&p);
        printf("%d",v[o][p]);
        cout<<"\n";
        
    
    }

    return 0;
}



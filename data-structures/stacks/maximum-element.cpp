#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int s[100000],track[100000],top=-1,top2=-1,m;
void push(int x)
{
    if(top==-1)
    {
        top2+=1;
        track[top2]=x;
    }
    else
    {
        if(x>track[top])
        {
            top2++;
            track[top2]=x;
        }
        else
        {
        m=track[top2];
        top2++;
        track[top2]=m;
        }

    }
    top+=1;
    s[top]=x;
}

void pop()
{
    top--;
    top2--;
}

void printmax()
{
    cout<<track[top2]<<endl;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int x,n,q,i;
    cin>>n;
    for(i=0;i<n;i++)
    {
    cin>>q;
    if(q==1)
    {
        cin>>x;
        push(x);
    }
    if(q==2)
    {
        pop();
    }
    if(q==3)
    {
        printmax();
    }
    }
    return 0;
}


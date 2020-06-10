#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    if(10>n>0)
    {
        if(n==1)
        printf("one");
        if(n==2)
        printf("two");
        if(n==3)
        printf("three");
        if(n==4)
        printf("four");
        if(n==5)
        printf("five");
        if(n==6)
        printf("six");
        if(n==7)
        printf("seven");
        if(n==8)
        printf("eight");
        if(n==9)
        printf("nine");
    }
    else
    printf("Greater than 9");


    return 0;
}


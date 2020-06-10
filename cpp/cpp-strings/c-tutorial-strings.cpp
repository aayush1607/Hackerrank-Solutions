#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    int l1,l2;
    string s1,s2;
    char c;
    cin>>s1>>s2;
    l1=s1.size();
    l2=s2.size();
    cout<<l1<<" "<<l2<<endl;
    cout<<(s1+s2)<<endl;
    c=s1[0];
    s1[0]=s2[0];
    s2[0]=c;
    cout<<s1<<" "<<s2;


    return 0;
}


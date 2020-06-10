#include <iostream>
#include <sstream>
#include <cstring>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student
{
    private:
    int age,std;
    string f,l;
    public:
    void set_age(int x)
    {
        age=x;
    }
    void set_standard(int x)
    {std=x;
    }

    void set_first_name(string g)
    {
        f=g;
    }
    void set_last_name(string g)
    {
        l=g;
    }
    int get_age()
    {
        return(age);
    }
    string get_last_name()
    {
        return(l);
    }
    int get_standard()
    {return(std);}

    string get_first_name()
    {return(f);}

    void to_string()
    {cout<<age<<','<<f<<','<<l<<','<<std;}
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    st.to_string();
    
    return 0;
}



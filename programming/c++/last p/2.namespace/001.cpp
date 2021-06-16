#include <iostream>
using namespace std;
namespace korean_pig{
    void hunbin(){
        cout<<"namespace";
    }
}
int main (){
    cout<<"this is"<<endl;
    korean_pig::hunbin();
}

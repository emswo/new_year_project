#include <iostream>
void call(int & foe){
foe=30;
}
int main (){
    int a=3;
    std::cout<<a<<std::endl;
    call(a);
    std::cout<<a<<std::endl;
    return 0;
}

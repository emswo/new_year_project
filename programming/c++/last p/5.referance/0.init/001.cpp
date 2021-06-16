#include <iostream>
int main (){
    int a = 5;
    int & another_a = a;
    std::cout<<a<<" "<<another_a<<std::endl;
    a=6;
    std::cout<<a<<" "<<another_a<<std::endl;
    another_a = 15;
    std::cout<<a<<" "<<another_a<<std::endl;  
}

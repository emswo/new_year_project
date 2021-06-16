#include <iostream>
void Myfunc(void){
    std::cout<<"Myfunc(void) calld"<<std::endl;
}
void Myfunc(char c){
    std::cout<<"Myfunc(char c) calld"<<std::endl;
}
void Myfunc(int a,int b){
    std::cout<<"Myfunc(int a, int b) calld"<<std::endl;
}

int main (){
    Myfunc();
    Myfunc('A');
    Myfunc(12,13);
}
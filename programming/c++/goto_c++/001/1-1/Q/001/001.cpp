#include <iostream>
int main (){
    int total = 0;
    int in = 0;
    for(int a=0;a<5;a++){
        std::cout<<a+1<<"번째 정수 입력: "<<std::endl;
        std::cin>>in;
        total = in + total;
    }

    std::cout<<total;
}
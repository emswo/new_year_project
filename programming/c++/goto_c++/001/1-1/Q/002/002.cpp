#include <iostream>
int main (){
    char number[100];
    char name[100];
    std::cout<<"이름입력: ";
    std::cin>>name;
    std::cout<<"전번입력: ";
    std::cin>>number;
    std::cout<<name<<number;
}
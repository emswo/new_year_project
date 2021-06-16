#include <iostream>
int main (){
    int a[10]={0},i=0,ch=0,b[10]={1,2,3,4,5,6,7,8,9,0};
    while(1){
    std::cout<<"put 10 numbers"<<std::endl;
    for(i=0;i<sizeof(a)/sizeof(int);i++){
    std::cin>>a[i];
    }
    for(i=0;i<sizeof(a)/sizeof(int);i++)ch=ch+(a[i]^b[i]);
    if(ch){
        std::cout<<"No Matched"<<std::endl;
    }
    else if(ch==0)std::cout<<"Matched"<<std::endl;
    else std::cout<<"error"<<std::endl;
    }
    return 0;
}
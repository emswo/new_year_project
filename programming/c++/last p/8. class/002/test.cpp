#include <iostream>
class Date {
int year_;
int month_; // 1 부터 12 까지.
int day_; // 1 부터 31 까지.
public:
    void SetDate(int year, int month, int date){
        
    }
    void AddDay(int inc){
        std::cout << "일 더하기: " << std::endl;
        int temp;
        std::cin >> temp;
        year_+=temp;
        temp = 0;
    }
    void AddMonth(int inc){
        std::cout << "월 더하기: " << std::endl;
        int temp;
        std::cin >> temp;
        year_+=temp;
        temp = 0;
    }
    void AddYear(int inc){
        std::cout << "년도 더하기: " << std::endl;
        int temp;
        std::cin >> temp;
        year_+=temp;
        temp = 0;
    }
    void ShowDate(){

    }
private:
    void yoon(){
        if(month_==2){

        }//7월 8월에 홀짝이 나뉨
    }

};
int main (){

}
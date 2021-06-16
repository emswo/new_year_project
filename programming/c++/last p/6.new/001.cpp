#include <iostream>
int main(){
    int arr_size;
    std::cout << "array size : "; //배열 크기 입력받음
    std::cin >> arr_size; //배열 크기 입력받은걸 저장
    char *list = new char[arr_size]; //입력받은 배열 크기만큼 힙에 할당함
    for(int i=0;i<arr_size;i++){ //배열 크기만큼 입력
        std::cin>>list[i];
    }
    for(int i=0;i<arr_size;i++){ //배열 크기만큼 출력
        std::cout<<i<<"th element of list : "<<list[i]<<std::endl;
    }
    delete[] list; //할당한 메모리 제거
    return 0;
}
#include <iostream>
struct animal
    {
        char name[30]={0};
        int age;
        int health;
        int food;
        int clean;
    };

int play (animal * list){
    list->health += 10;
    list->food -= 20;
    list->clean -= 30;
}
void one_day_pass(animal *list) {
// 하루가 지나면
    list->health -= 10;
    list->food -= 30;
    list->clean -= 20;
}

int show_stat(animal *list){
    std::cout<<list->age<<std::endl;
    std::cout<<list->clean<<std::endl;
    std::cout<<list->food<<std::endl;
    std::cout<<list->health<<std::endl;
    for(int i=0;i<sizeof(list->name)/sizeof(int);i++){
    std::cout<<list->name[i];
    }
    return 0;
}
int create_animal (animal *list){
    std::cout<<"동물의 이름을 입력하시오: "<<std::endl;
    std::cin >> list->name;
    std::cout<<"동물의 나이를 입력하시오: "<<std::endl;
    std::cin >> list->age;
    list->health = 100;
    list->food = 100;
    list->clean=100;
}

int main (){
    animal *list[10];
    int animal_number = 0;
    while(1){
    std::cout<<"1. 동물 추가하기\n2. 동물 놀아주기\n3. 동물 상태보기"<<std::endl;
    int select_num = 0;
    std::cin>>select_num;
    int play_with =  0 , choice = 0;

    switch (select_num)
    {
    case 1:
        list[animal_number] = new animal;
        create_animal(list[animal_number]);
        animal_number++;
        break;
    case 2:
        std::cout<<"동물 선택: "<<std::endl;
        std::cin>>play_with;
        if(play_with<animal_number) play(list[play_with]);
        break;
    case 3:
        std::cout<<"동물 선택: "<<std::endl;
        std::cin>>choice;
        if(choice<animal_number) show_stat(list[choice]);
        break;
    
    default:
        break;
    }
    for(int i = 0;i<animal_number;i++)one_day_pass(list[i]);
    }
    for(int i = 0;i < animal_number; i ++)delete list[i];  
}
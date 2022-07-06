#include <iostream>

class human{
public:
    int height;
    float weight;
    human(int h, int w){
        height = h;
        weight = w;
    }
};

int print(int x){
    std::cout<< x <<std::endl;
}

int print(float x){
    std::cout<< x <<std::endl;
}

int main(){
    human john(180, 220);
    print(john.height);
    print(john.weight);
    return 0;
}
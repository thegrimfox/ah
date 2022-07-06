#include <iostream>

class human{
public:
    int height;
    int weight;
    int get_heigth() const{
        return height;
    }
    int get_weight() const{
        return weight;
    }
};

int main(){
    human john;
    john.height = 180;
    john.weight = 220;
    std::cout<< john.get_heigth() <<std::endl;
    std::cout<< john.get_weight() <<std::endl;
    return 0;
}
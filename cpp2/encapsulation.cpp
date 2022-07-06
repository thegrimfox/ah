#include <iostream>

class human{
private: //abstracted from the user
    int height;
    int weight;
public:
    human(int h, int w){
        height = h;
        weight = w;
    }
    int get_height() const{
        return height;
    }
    int get_weight() const{
        return weight;
    }
};

int main(){
    human john(180, 220);
    std::cout<< john.get_height() <<std::endl;
    std::cout<< john.get_weight() <<std::endl;
    return 0;
}
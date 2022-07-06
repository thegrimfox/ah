#include <iostream>

class human{
public:
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

class adult: public human{ //inherit from human class
public:
    adult(int h, int w) : human(h, w) {} //call the base class constructor from this constructor
    std::string occupation;
    std::string get_occupation() const{
        return occupation;
    }
};

int main(){
    adult john(180, 220);
    john.occupation = "lawyer";
    std::cout<< john.get_height() <<std::endl;
    std::cout<< john.get_weight() <<std::endl;
    std::cout<< john.get_occupation() <<std::endl;
    return 0; 
}
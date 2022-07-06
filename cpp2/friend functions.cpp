#include <iostream>

class human{
private:
    int weight;
public:
    human(int w){
        weight = w;
    }
    friend int get_weight(human h);
};

int get_weight(human h){
    return h.weight; //we can access the private members of the associated class thanks to the friend function
}

int main(){
    human john(220);
    std::cout<< get_weight(john) <<std::endl;
    return 0;
}
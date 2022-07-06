#include <iostream>

template <class T>
T largest(T n1, T n2){
    return (n1 > n2) ? n1 : n2;
}

int main(){
    int x, y;
    std::cout<< "enter two integers: " <<std::endl;
    std::cin >> x >> y;
    std::cout<< largest(x, y) <<std::endl;
    return 0;
}
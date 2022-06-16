#include <iostream>

int main(){
    auto x= 1;
    while (x <= 3)
    {
        //x++ primero muestra el valor y despues o incrementa
        std::cout<< x++ <<std::endl;
    }
    return 0;
}
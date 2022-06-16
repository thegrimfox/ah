#include <iostream>

int main()
{
    if(int x=4; !x) std::cout<< "x is 0" <<std::endl;
    else if(x < 0) std::cout<< "x is negative" <<std::endl;
    else{
        std::cout<< "x is positive" <<std::endl;
    }
    return 0;
}

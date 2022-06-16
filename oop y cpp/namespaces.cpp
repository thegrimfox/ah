#include <iostream>

namespace ns_1{
    void func(){
        std::cout<< "called from ns_1" <<std::endl;
    }
}

namespace ns_2{
    void func(){
        std::cout<< "called from ns_2" <<std::endl;
    }
}

int main(){
    ns_1::func();
    ns_2::func();
    return 0;
}
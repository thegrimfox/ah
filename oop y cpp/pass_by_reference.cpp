#include <iostream>

void square(int& x){
    x *= x;
    return;
}
int main(){
    int x=2;
    square(x);
    std::cout<< x <<std::endl;
    return 0;
}
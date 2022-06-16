#include <iostream>

int double_number_a(int x)
{
    return 2*x;
}
void double_number_b(int* x)
{
    *x *= 2;
}

int main(){
    auto num=5;
    std::cout<<double_number_a(num)<<std::endl;
    std::cout<<num<<std::endl;
    double_number_b(&num);
    std::cout<<num<<std::endl;
    return 0;
}
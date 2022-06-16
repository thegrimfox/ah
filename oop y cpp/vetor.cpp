#include <iostream>
#include <vector>

int main(){
    std::vector<int> v = {0,1,2,3};
    for (const int& i:v)
    {
        std::cout<< i <<std::endl;
    }
    int a[] = {4,5,6,7};
    for(int n : a){
        std::cout<< n <<std::endl;
    }
    return 0;
}
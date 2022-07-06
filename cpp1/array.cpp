#include <iostream>
#include <array>

int main()
{
    std::array<int, 5> my_array;

    for(size_t i=0;i<my_array.size();i++){
        my_array[i] = i;
    }

    std::cout <<my_array[2]<<std::endl;
    return 0;
}
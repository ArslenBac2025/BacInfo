#include <iostream>
#include <map>
#include <unordered_map>

int main() {
    std::unordered_map<char, int> mymap = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    const std::string *input = new std::string("IVIII");
    int *sum = new int {0};
    long unsigned *i = new long unsigned{0};

    while(*i < input->length()) {
        if((*i + 1 ) < input->length() && mymap[input->at(*i + 1)] > mymap[input->at(*i)]) {
            *sum += mymap[input->at(*i + 1)] - mymap[input->at(*i)];
            ++*i;
        }
        else {
            *sum += mymap[input->at(*i)];
        }
        ++*i;
    }

    std::cout << *sum << std::endl;
    delete sum;
    delete i;
    delete input;
}

#pragma once
#include<string>
#include<deque>
#include"DistributionTree.cpp"

#define ld long double

class Generator {
    private:
    int n; // vector bit length
    std::deque<bool> bits;
    std::vector<std::vector<node>> p;
    ld get_p();
    int toint();

    bool isinitialised;

    public:

    ld randfloat();
    void seed(int);
    void print_bits();
    int next();

    Generator(int, double, double);
};
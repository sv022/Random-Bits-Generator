#pragma once
#include<iostream>
#include"Generator.h"

#define ld long double

ld Generator::randfloat(){
    return (rand() / static_cast<float>(RAND_MAX));
}

int Generator::toint(){
    int s = 0;
    for (int i = this->n - 1; i >= 0; i--){
        s += (int)this->bits[i] * pow(2, (this->n - i) - 1);
    }
    return s;
}

ld Generator::get_p(){
    int j = toint();
    return this->p[this->n + 1][2 * j].trans;
}

void Generator::seed(int s){
    if (this->isinitialised) return;
    for (int i = this->bits.size() - 1; i >= 0; i--){
        this->bits[i] = s % 2;
        s /= 2;
    }
    this->isinitialised = true;
}

int Generator::next(){
    ld p0 = get_p();
    bool bit = p0 <= randfloat();
    this->bits.pop_front();
    this->bits.push_back(bit);
    //this->p = (bit ? getdistribution(this->n + 1, p0, 1 - p0) : getdistribution(this->n + 1, 1 - p0, p0));
    return (int)bit;
}

Generator::Generator(int size, double p0, double p1){
    this->n = size;
    this->isinitialised = false;

    for (int i = 0; i < size; i++)
        this->bits.push_back(false);
    this->p = getdistribution(size + 1, p0, p1);
    logfile(p);
}

void Generator::print_bits(){
    for (int i = 0; i < this->n; i++)
        std::cout << this->bits[i] << ' ';
    std::cout << '\n';
}

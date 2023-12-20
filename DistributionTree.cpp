#pragma once
#include<string>
#include<vector>
#include<cmath>
#include<fstream>

#define ld long double

struct node{
    std::string value;
    ld abs;
    ld trans;

    node(std::string value, ld abs, ld trans){
        this->value = value;
        this->abs = abs;
        this->trans = trans;
    }
    node(std::string value){
        this->value = value;
        this->abs = 0;
        this->trans = 0;
    }
};


std::string bin(int n, int length){
    std::string r;
    while (n != 0){
        r = (n % 2 == 0 ? "0" : "1") + r;
        n /= 2;
    }
    while (r.size() < length) r = "0" + r;
    return r;
}

ld g(int i, int j){ // NOTE: i, j будут использованы в будущем
    ld r = ((ld)(1 + (rand() % (9 - 1))) / 10);
    return r;
}

void logfile(std::vector<std::vector<node>> p){
    std::ofstream f("tree_log.txt");
    for (int i = 0; i < p.size(); i++){
        for (int j = 0; j < pow(2, i); j++)
            f << p[i][j].abs << ' ';
        f << '\n';
    }
    f.close();
}

std::vector<std::vector<node>> getdistribution(int n, ld a, ld b){
    std::vector<std::vector<node>> p;
    p.push_back(std::vector<node>{node("", 1, 1)});
    p.push_back(std::vector<node>{node("0", a, a), node("1", b, b)});
    if (n == 1) return p;
    for (int i = 2; i < n + 1; i++){
        std::vector<node> layer;
        for (int j = 0; j < pow(2, n); j++)
            layer.push_back(node(bin(j, i)));
        
        for (int k = 0; k < pow(2, i - 2); k++){
            long double maxp = std::min(p[i - 1][k].abs, p[i - 1][2 * k].abs);
            
            long double min_condition1 = p[i - 1][k].abs - p[i - 1][2 * k + 1].abs;
            long double min_condition2 = p[i - 1][2 * k].abs - p[i - 1][k + pow(2, (i - 2))].abs;
            long double minp;
            if (min_condition1 < 0 || min_condition2 < 0) minp = 0;
            else minp = std::max(min_condition1, min_condition2);

            layer[2 * k].abs = (maxp - minp) * g(i, k) + minp;

            layer[2 * k + 1].abs = p[i - 1][k].abs - layer[2 * k].abs;
            layer[2 * k + pow(2, i - 1)].abs = p[i - 1][2 * k].abs - layer[2 * k].abs;
            layer[2 * k + 1 + pow(2, i - 1)].abs = p[i - 1][2 * k + 1].abs - layer[2 * k + 1].abs;
        }
        for (int j = 0; j < pow(2, n); j++)
            layer[j].trans = layer[j].abs / p[i - 1][j / 2].abs;
        
        p.push_back(layer);
    }
    return p;
}

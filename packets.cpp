#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include"Generator.cpp"

using namespace std;

int randint(int a, int b){
    return a + (rand() % (b - a));
}

vector<bool> get_package(int size){
    vector<bool> package;
    for (int i = 0; i < size; i++){
        bool bit = randint(1, 10) % 2;
        package.push_back(bit);
    }
    return package;
}

void extend_package(vector<bool> &package){
    int size = package.size();
    vector<bool> package_new;
    for (int i = 0; i < size; i++)
        package_new.push_back(0);
    for (int i = 0; i < size; i++)
        package_new.push_back(package[i]);
    package = package_new;
}

void extend_package(vector<bool> &package, int size){
    vector<bool> package_new;
    for (int i = 0; i < size; i++)
        package_new.push_back(0);
    for (int i = 0; i < package.size(); i++)
        package_new.push_back(package[i]);
    package = package_new;
}


int main(){
    ld p0 = 0.4;
    ld p1 = 1 - p0;
    int seed = 61;
    int n = 5;
    int package_count = 100;
    int package_size = 8;
    Generator G(n, p0, p1);
    G.seed(seed);
    ofstream f("packets.txt");
    for (int i = 0; i < package_count; i++){
        vector<bool> package = get_package(package_size);
        bool bit = G.next();
        if (bit)
            extend_package(package);
        for (int i = 0; i < package.size(); i++)
            f << (int)package[i];
        f << '\n';
    }
}

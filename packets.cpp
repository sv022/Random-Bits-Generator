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

void extend_package(vector<bool> &package, int size){
    vector<bool> package_new;
    int p_size = package.size();
    for (int i = 0; i < size - p_size; i++)
        package_new.push_back(0);
    for (int i = 0; i < p_size; i++)
        package_new.push_back(package[i]);
    package = package_new;
}


int main(){
    ld p0 = 0.4;
    ld p1 = 1 - p0;
    int seed = 61; // начальное заполнение
    int n = 5; // глубина
    Generator G(n, p0, p1);
    G.seed(seed);

    int package_count = 100;
    int package_size = 8;
    int extend_to = 16;
    ofstream f("packets.txt");

    bool user_input = true;

    if (user_input){
        cout << "default package size:\n";
        cin >> package_size;
        cout << "extend package to size:\n";
        cin >> extend_to;
        cout << "number of packages:\n";
        cin >> package_count;
    };
    f << package_size << '\n';
    f << extend_to << '\n';
    for (int i = 0; i < package_count; i++){
        vector<bool> package = get_package(package_size);
        bool bit = G.next();
        if (bit)
            extend_package(package, extend_to);
        for (int i = 0; i < (int)package.size(); i++)
            f << (int)package[i];
        f << '\n';
    }
}

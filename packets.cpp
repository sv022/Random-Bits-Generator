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
    int package_count;
    int package_size;
    int extend_to;
    ofstream f("packets.txt");
    ifstream g("output.txt");

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
    string bits;
    getline(g, bits);
    for (int i = 0; i < package_count; i++){
        vector<bool> package = get_package(package_size);
        if (bits[i] == '1')
            extend_package(package, extend_to);
        for (int i = 0; i < (int)package.size(); i++)
            f << (int)package[i];
        f << '\n';
    }
}

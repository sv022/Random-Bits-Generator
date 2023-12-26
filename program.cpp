#include<iostream>
#include<cmath>
#include<fstream>
#include<locale.h>
#include"Generator.cpp"
#include"statistics.cpp"

using namespace std;

int randint(int a, int b){
    return a + (rand() % (b - a));
}

int main(){
    ld p0 = 0.4;
    ld p1 = 1 - p0;
    int seed = 61;
    int n = 5;
    int size = 100000;
    bool user_input = false;
    if (user_input){
        cout << "p(0):\n";
        cin >> p0;
        cout << "p(1):\n";
        cin >> p1;
        cout << "Depth:\n";
        cin >> n;
        cout << "Seed (default - 61):\n";
        cin >> seed;
        cout << "size:\n";
        cin >> size;
    };
    ofstream f("output.txt");

    Generator G(n, p0, p1, true);
    G.seed(seed);
    for(int i = 0; i < size; i++){
        f << G.next();
    }
    f.close();

    statistics::count_vectors();
    statistics::count_Hamming();
}

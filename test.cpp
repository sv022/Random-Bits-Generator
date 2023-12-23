#include<iostream>
#include<fstream>


using namespace std;

int randint(int a, int b){
    return a + (rand() % (b - a));
}

int main(){
    string text;
    ifstream f("output.txt");
    getline(f, text);
    int n = text.size();
    int c0, c1;
    for (int i = 0; i < n; i++){
        if (text[i] == '1') c1++;
        else c0++;
    }
    cout << (double)c0 / n << ' ' << (double)c1 / n;
}

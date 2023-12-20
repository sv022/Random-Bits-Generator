#include<cmath>
#include"Generator.cpp"
#include<fstream>

using namespace std;

int randint(int a, int b){
    return a + (rand() % (b - a));
}

int main(){
    ofstream f("test.txt");
    Generator G(5, 0.9, 0.1);
    G.seed(61);
    for(int i = 0; i < 50000; i++){
        f << G.next();
    }
    f.close();
}
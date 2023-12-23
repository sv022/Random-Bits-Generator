#include<cmath>
#include<fstream>
#include"Generator.cpp"
#include"statistics.cpp"

using namespace std;

int randint(int a, int b){
    return a + (rand() % (b - a));
}

int main(){
    ofstream f("output.txt");
    ld p0 = 0.7;
    ld p1 = 1 - p0;
    int seed = 61;
    int n = 5;

    Generator G(n, p0, p1, true);
    G.seed(seed);
    for(int i = 0; i < 100000; i++){
        f << G.next();
    }
    f.close();

    statistics::count_vectors();
    statistics::count_Hamming();
}

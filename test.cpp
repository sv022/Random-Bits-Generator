#include<iostream>
#include<fstream>


using namespace std;

int randint(int a, int b){
    return a + (rand() % (b - a));
}

//string text = "01010011001001011000110100011100101010100101100110010110101100101011010110011100101000110011100111011010011010100110011100100110101001001000101110001010101101011101100111001000100111011010110011011001001011001110011001010110101110010001010101100110111000100010000110010101011010010101100101010110101001010010100110010100111100110010011011010101110110011101101111011010110000101010001010100101101011100110001010101100110010110001010001011001011001010010110111011101101010010100111100111011001110101100";

int main(){
    string text;
    ifstream f("test.txt");
    getline(f, text);
    int n = text.size();
    int c0, c1;
    for (int i = 0; i < n; i++){
        if (text[i] == '1') c1++;
        else c0++;
    }
    cout << (double)c0 / n << ' ' << (double)c1 / n;
}

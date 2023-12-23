#pragma once
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>

namespace statistics {
    std::string bin(int n, int length){
        std::string r;
        while (n != 0){
            r = (n % 2 == 0 ? "0" : "1") + r;
            n /= 2;
        }
        while (r.size() < length) r = "0" + r;
        return r;
    }

    int count(std::string s, std::string target){
        int occurrences = 0;
        std::string::size_type pos = 0;
        while ((pos = s.find(target, pos )) != std::string::npos) {
            ++occurrences;
            pos += 1;
        }
        return occurrences;
    }

    void count_vectors(int length = -1){
        std::string data, temp_n;
        int n;
        std::ifstream g("output.txt");
        std::ifstream t_log("tree_log.txt");
        std::ofstream f("vectors_total.txt");
        
        getline(t_log, temp_n);
        if (length == -1) n = stoi(temp_n) - 2;
        else if (length > 0) n = length;
        else return;

        getline(g, data);
        for (int i = 0; i < pow(2, n); i++){
            std::string s = bin(i, n);
            int k = count(data, s);
            f << k << ' ';
        }

        g.close();
        t_log.close();
        f.close();
    }
    void count_Hamming(){
        std::string data, temp_n;
        int n;
        std::ifstream g("output.txt");
        std::ifstream t_log("tree_log.txt");
        std::ofstream f("vectors_Hamming.txt");
        
        getline(t_log, temp_n);
        n = stoi(temp_n) - 2;

        getline(g, data);

        std::vector<int> c;
        for (int i = 0; i <= n; i++) c.push_back(0);

        for (int i = 0; i < pow(2, n); i++){
            std::string s = bin(i, n);
            int k = count(data, s);
            c[count(s, "1")] += k;
        }
        for (int i = 0; i <= n; i++) f << c[i] << ' ';

        g.close();
        t_log.close();
        f.close();
    }
};

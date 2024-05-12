#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<string> tokenize(string str, char sep) {
    vector<string> tokens;
    string token;
    int n = str.size();
    for (int i = 0; i < n; i++) {
        if (str[i] == sep) {
            if (!token.empty()) {
                tokens.push_back(token);
                token = "";
            }
        } else {
            token.push_back(str[i]);
        }
    }
    if (!token.empty()) {
        tokens.push_back(token);
    }
    return tokens;
}

int main(int argc, char **argv) {
    ifstream f(argv[1]);
    string str;
    getline(f, str);
    vector<string> tokens = tokenize(str, ' ');
    return 0;
}
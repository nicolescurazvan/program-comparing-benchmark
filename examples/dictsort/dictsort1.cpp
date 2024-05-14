#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char **argv) {
    ifstream f(argv[1]);
    vector<string> dict;
    string line;
    int n, i;
    f >> n;
    getline(f, line);
    for (i = 0; i < n; i++) {
        getline(f, line);
        dict.push_back(line);
    }
    sort(dict.begin(), dict.end());
    f.close();
    return 0;
}
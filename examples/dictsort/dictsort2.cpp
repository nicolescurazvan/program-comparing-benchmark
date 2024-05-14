#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char **argv) {
    ifstream f(argv[1]);
    vector<string> dict[96];
    string line;
    int n, i;
    f >> n;
    getline(f, line);
    for (i = 0; i < n; i++) {
        getline(f, line);
        int index = line[0] - ' ';
        dict[index].push_back(line);
    }
    for (i = 0; i < 96; i++) {
        sort(dict[i].begin(), dict[i].end());
    }
    f.close();
    return 0;
}
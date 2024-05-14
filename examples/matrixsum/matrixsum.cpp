#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main(int argc, char **argv) {
    ifstream f(argv[1]);
    int m, n, i, j, sum = 0;
    f >> m >> n;
    vector<vector<int>> matrix(m);
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            int x;
            f >> x;
            matrix[i].push_back(x);
            sum += x;
        }
    }
    f.close();
    return 0;
}
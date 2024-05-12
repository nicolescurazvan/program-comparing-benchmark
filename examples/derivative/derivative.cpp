#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    ifstream f(argv[1]);
    int n, i;
    f >> n;
    vector<double> poly(n);
    for (i = 0; i < n; i++) {
        f >> poly[i];
    }
    for (i = 0; i < n; i++) {
        poly[i] *= n - i;
    }
    f.close();
    return 0;
}
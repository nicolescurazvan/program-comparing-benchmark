#include <stdio.h>
#include <stdlib.h>

int maxdiv(int n) {
    int *div = (int*)malloc((n + 1) * sizeof(int));
    div[0] = 1;
    div[1] = 1;
    for (int i = 2; i < n; i++) {
        div[i] = 1;
    }
    for (int i = 2; i <= n; i++) {
        for (int j = i; j <= n; j += i) {
            div[j]++;
        }
    }

    int max = 0;
    for (int i = 2; i <= n; i += 2) {
        if (div[i] > max) {
            max = div[i];
        }
    }
    return max;
}

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    int n;
    fscanf(f, "%d", &n);
    int d = maxdiv(n);
    return 0;
}
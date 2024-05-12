#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    int n, i;
    fscanf(f, "%d", &n);
    double *poly = (double*)malloc(n * sizeof(double));
    for (i = 0; i < n; i++) {
        fscanf(f, "%lf", &poly[i]);
    }

    for (int i = 0; i < n; i++) {
        poly[i] *= n - i;
    }
    free(poly);
    fclose(f);
    return 0;
}
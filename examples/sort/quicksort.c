// Program to benchmark quick sort
#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    int *arr, n, i;
    fscanf(f, "%d", &n);
    arr = (int*)malloc(n * sizeof(int));
    for (i = 0; i < n; i++) {
        fscanf(f, "%d", &arr[i]);
    }

    qsort(arr, n, sizeof(int), comp);
    free(arr);
    fclose(f);
    return 0;
}
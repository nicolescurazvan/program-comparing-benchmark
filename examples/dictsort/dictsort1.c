#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b) {
    char *str_a = *(char**)a;
    char *str_b = *(char**)b;
    return strcmp(str_a, str_b);
}

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    int n, i;
    size_t size = 0;
    char *line = NULL, **dict;
    fscanf(f, "%d", &n);
    dict = (char**)malloc(n * sizeof(char*));
    getline(&line, &size, f);
    free(line);
    line = NULL;
    for (i = 0; i < n; i++) {
        getline(&line, &size, f);
        dict[i] = strdup(line);
        free(line);
        line = NULL;
    }
    qsort((void*)dict, n, sizeof(char*), comp);
    free(dict);
    fclose(f);
    return 0;
}
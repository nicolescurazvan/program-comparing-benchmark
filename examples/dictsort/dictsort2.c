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
    int n, i, j, length[96];
    size_t size = 0;
    char *line = NULL, **dict[96];
    fscanf(f, "%d", &n);
    for (i = 0; i < 96; i++) {
        dict[i] = (char**)malloc(n * sizeof(char*));
        length[i] = 0;
    }
    getline(&line, &size, f);
    free(line);
    line = NULL;
    for (i = 0; i < n; i++) {
        getline(&line, &size, f);
        int index = line[0] - ' ';
        dict[index][length[index]] = strdup(line);
        length[index]++;
        free(line);
        line = NULL;
    }
    for (i = 0; i < 96; i++) {
        qsort(dict[i], length[i], sizeof(char), comp);
    }
    for (i = 0; i < 96; i++) {
        free(dict[i]);
    }
    fclose(f);
    return 0;
}
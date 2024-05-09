// Program to benchmark merge sort
#include <stdio.h>
#include <stdlib.h>

void mergesort(int *arr, int n) {
    if (n < 2) {
        return;
    }
    int n1 = n / 2;
    int n2 = n - n1;
    int *arr1 = malloc(n1 * sizeof(int));
    int *arr2 = malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++) {
        arr1[i] = arr[i];
    }
    for (int i = n1; i < n; i++) {
        arr2[i - n1] = arr[i];    
    }
    
    mergesort(arr1, n1);
    mergesort(arr2, n2);

    int i = 0, j = 0, k = 0;
    while (i < n1 && j < n2) {
        if (arr1[i] < arr2[j]) {
            arr[k] = arr1[i];
            i++;
        } else if (arr1[i] > arr2[j]) {
            arr[k] = arr2[j];
            j++;
        } else {
            arr[k] = arr1[i];
            arr[k + 1] = arr2[j];
            k++;
            i++;
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = arr1[i];
        k++;
        i++;
    }
    while (j < n2) {
        arr[k] = arr2[j];
        k++;
        j++;
    }
    free(arr1);
    free(arr2);
}

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    int n, i;
    fscanf(f, "%d", &n);
    int *arr = (int*)malloc(n * sizeof(int));
    for (i = 0; i < n; i++) {
        fscanf(f, "%d", &arr[i]);
    }

    mergesort(arr, n);
    free(arr);
    fclose(f);
    return 0;
}
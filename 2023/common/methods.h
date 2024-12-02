#include <math.h>
#include <stdlib.h>

/* Substring from str with start as starting index, and max_len as length */
char* substring_from_with_len(char *str, long start, long max_len) {
    char *val = malloc(max_len * sizeof(char));
    strncpy(val, str+start, max_len);
    return val;
}

/* Subtract y from x array */
void subtract(int *x, int *y, int *result) {
    int size_x = sizeof(*x)/sizeof(int);
    int size_y = sizeof(*y)/sizeof(int);
    int size = fmin(size_x, size_y);
    for (int i = 0 ; i < size ; ++i)
        result[i] = x[i] - y[i];
}

/* Free 2D array */
void free_int_2d_matrix(int **array, int rows) {
    for (int i = 0; i < rows; ++i) {
        free(array[i]);
    }
    free(array);
}

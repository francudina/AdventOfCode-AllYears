#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to convert string to set of integers
void to_int(const char *x, int *result, int *size) {
    *size = 0;
    char *token = strtok((char *)x, " ");
    while (token != NULL) {
        result[(*size)++] = atoi(token);
        token = strtok(NULL, " ");
    }
}

// Function to calculate points based on the number of elements in the set
int points(int size) {
    return size == 0 ? 0 : 1 << (size - 1);
}

int main() {
    FILE *file = fopen("2023/day_4/input.txt", "r");
    if (file == NULL) {
        perror("error opening file");
        return 1;
    }

    char line[200];
    int total = 0;

    while (fgets(line, sizeof(line), file) != NULL) {
        // Split the line into two parts separated by '|'
        char *token;
        char *cards[2];
        int card_values[2][30];  // Assuming a maximum of 10 integers in a set
        int sizes[2];

        int index = 0;
        token = strtok(line, "|");
        while (token != NULL) {
            cards[index++] = token;
            token = strtok(NULL, "|");
        }

        // Convert each part to sets of integers
        for (int i = 0; i < 2; ++i) {
            to_int(cards[i], card_values[i], &sizes[i]);
        }

        // Calculate points and update total
        total += points(sizes[0] & sizes[1]);
    }

    printf("Result: %d\n", total);
    fclose(file);

    return 0;
}

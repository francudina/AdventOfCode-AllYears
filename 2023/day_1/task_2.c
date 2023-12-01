#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "../common/structures.h"

struct KeyValuePair_StringInt lookup[] = {
        {"one", 1},
        {"two", 2},
        {"three", 3},
        {"four", 4},
        {"five", 5},
        {"six", 6},
        {"seven", 7},
        {"eight", 8},
        {"nine", 9}
};


int check_prefix(const char *line) {
    if (strlen(line) > 0 && isdigit(line[0]))
        return line[0] - '0';
    for (size_t i = 0; i < sizeof(lookup) / sizeof(lookup[0]); ++i) {
        if (strncmp(line, lookup[i].key, strlen(lookup[i].key)) == 0)
            return lookup[i].value;
    }
    return -1;
}

int main() {
    FILE *file = fopen("2023/day_1/input_2.txt", "r");
    if (file == NULL) {
        perror("error opening file");
        return 1;
    }

    int total = 0;
    char line[256];

    while (fgets(line, sizeof(line), file) != NULL) {

        const char *token = strtok(line, "\n");
        if (token == NULL)
            continue;

        int numbers[256];
        int j = 0;

        for (int i = 0; i < strlen(token); ++i) {
            int num = check_prefix(token + i);
            if (num == -1)
                continue;
            numbers[j++] = num;
        }

        int num = numbers[0] * 10 + numbers[j - 1];
        total += num;
    }

    printf("Result: %d\n", total);
    fclose(file);

    return 0;
}

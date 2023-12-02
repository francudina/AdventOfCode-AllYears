#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main() {
    FILE *file = fopen("2023/day_1/input.txt", "r");
    if (file == NULL) {
        perror("error opening file");
        return 1;
    }

    int total = 0;
    char line[256];

    while (fgets(line, sizeof(line), file) != NULL) {
        char *num_str = malloc(strlen(line) + 1);
        int j = 0;

        for (int i = 0; i < strlen(line); i++) {
            if (isdigit(line[i]))
                num_str[j++] = line[i];
        }

        num_str[j] = '\0';

        int first = num_str[0] - '0';
        int last = num_str[j - 1] - '0';

        int num = first * 10 + last;
        total += num;

        free(num_str);
    }

    printf("Result: %d\n", total);
    fclose(file);

    return 0;
}

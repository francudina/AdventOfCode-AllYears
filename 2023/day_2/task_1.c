#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "../common/methods.h"

#define RED_MAX 12
#define GREEN_MAX 13
#define BLUE_MAX 14

int find_color_value(char *set, char *color) {
    // find substring
    char *res = strstr(set, color);
    if (res == NULL)
        return 0;
    // start position
    long position = res - set;
    // find value
    char *val = substring_from_with_len(set, position-3, 2);
    int v = atoi(val);
    free(val);
    return v;
}

int main() {
    FILE *file = fopen("2023/day_2/input.txt", "r");
    if (file == NULL) {
        perror("error opening file");
        return 1;
    }

    int total = 0;
    char line[256];

    while (fgets(line, sizeof(line), file) != NULL) {

        char *id_part = strtok(line, ":");
        char *set_part = strtok(NULL, ":");

        int id_match = 1;

        char *set = strtok(set_part, ";");
        while (set != NULL) {

            int red = find_color_value(set, "red");
            int green = find_color_value(set, "green");
            int blue = find_color_value(set, "blue");

            if (red > RED_MAX || green > GREEN_MAX || blue >  BLUE_MAX) {
                id_match = 0;
                break;
            }

            set = strtok(NULL, ";");
        }

        // game has exceeded the limit
        if (id_match == 0)
            continue;

        // start after "Game " prefix, and max 3 chars
        char *id = substring_from_with_len(id_part, 5, 3);
        total += atoi(id);

        free(id);
    }

    printf("Result: %d\n", total);
    fclose(file);

    return 0;
}

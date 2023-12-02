#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "../common/structures.h"

int find_color_value(char *set, char *color) {
    // find substring
    char *res = strstr(set, color);
    if (res == NULL)
        return 0;
    // start position
    long position = res - set;
    // find value
    char *val = substring_from_with_len(set, position-3, 2);
    return atoi(val);
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

        int red_max = 0;
        int green_max = 0;
        int blue_max = 0;

        char *set = strtok(set_part, ";");
        while (set != NULL) {

            int red = find_color_value(set, "red");
            int green = find_color_value(set, "green");
            int blue = find_color_value(set, "blue");

            // find max of each value
            if (red > red_max) red_max = red;
            if (green > green_max) green_max = green;
            if (blue > blue_max) blue_max = blue;

            set = strtok(NULL, ";");
        }

        total += (red_max * green_max * blue_max);
    }

    printf("Result: %d\n", total);
    fclose(file);

    return 0;
}

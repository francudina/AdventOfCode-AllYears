#include <stdlib.h>

struct KeyValuePair_StringInt {
    const char *key;
    int value;
};

char* substring_from_with_len(char *str, long start, long max_len) {
    char *val = malloc(max_len * sizeof(char));
    strncpy(val, str+start, max_len);
    return val;
}

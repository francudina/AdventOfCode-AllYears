/* Substring from str with start as starting index, and max_len as length */
char* substring_from_with_len(char *str, long start, long max_len) {
    char *val = malloc(max_len * sizeof(char));
    strncpy(val, str+start, max_len);
    return val;
}
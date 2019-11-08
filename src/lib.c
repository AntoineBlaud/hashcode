#include <stdio.h>
#include <json-c/json.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

struct json_object *parsed_json;
char *buffer;
const int T_PRINT = 5;
const int E = 20000;
char *PATH;
int S = 0;
struct json_object *array;
int arr_SIZE;
clock_t update;
int BEST_CHOICE;
int x;
int RAND_CHOICE;
int MAX;

void readJson(char *json)
{
    FILE *f;
    f = fopen(json, "r");
    fseek(f, 0, SEEK_END); // non-portable
    int size = ftell(f);
    buffer = (char *)malloc(sizeof(char) * size);
    rewind(f);
    fread(buffer, size, 1, f);
    parsed_json = json_tokener_parse(buffer);
}
char *concat(const char *s1, const char *s2)
{
    char *result = malloc(strlen(s1) + strlen(s2) + 1); // +1 for the null-terminator
    // in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

int in(char *s1, json_object *arr)
{

    int arr_SIZE = json_object_array_length(arr);
    for (int x = 2; x < arr_SIZE; x++)
    {
        char *s2 = json_object_get_string(json_object_array_get_idx(arr, x));
        if (strcmp(s1, s2) == 0)
        {
            return 1;
        }
    }
    return 0;
}

int randint(int n)
{
    if ((n - 1) == RAND_MAX)
    {
        return rand();
    }
    else
    {
        // Supporting larger values for n would requires an even more
        // elaborate implementation that combines multiple calls to rand()
        assert(n <= RAND_MAX);

        // Chop off all of the values that would cause skew...
        int end = RAND_MAX / n; // truncate skew
        assert(end > 0);
        end *= n;

        // ... and ignore results from rand() that fall above that limit.
        // (Worst case the loop condition should succeed 50% of the time,
        // so we can expect to bail out of this loop pretty quickly.)
        int r;
        while ((r = rand()) >= end)
            ;

        return r % n;
    }
}

void saveProgress()
{
    char *p = concat(PATH, "saved.txt");
    FILE *f = fopen(p, "w");
    fprintf(f, "%s ", json_object_to_json_string(parsed_json));

    fclose(f);
}

struct json_object *copyStringArray(struct json_object *o)
{
    struct json_object *c = json_object_new_array();
    int arr_SIZE = json_object_array_length(o);
    for (int u = 0; u < arr_SIZE; u++)
    {
        char *s2 = json_object_get_string(json_object_array_get_idx(o, u));
        json_object_array_add(c, json_object_new_string(s2));
    }
    return c;
}

struct json_object *addStringArray(struct json_object *a, struct json_object *b)
{
    struct json_object *c = json_object_new_array();
    int arr_SIZE = json_object_array_length(a);
    for (int u = 0; u < arr_SIZE; u++)
    {
        char *s2 = json_object_get_string(json_object_array_get_idx(a, u));
        json_object_array_add(c, json_object_new_string(s2));
    }
    arr_SIZE = json_object_array_length(b);
    for (int u = 0; u < arr_SIZE; u++)
    {
        char *s2 = json_object_get_string(json_object_array_get_idx(b, u));
        if (in(s2, c) == 0)
            json_object_array_add(c, json_object_new_string(s2));
    }

    return c;
}
int isH(int index)
{
    struct json_object *tmp = json_object_array_get_idx(array, index);
    char *s = json_object_get_string(json_object_array_get_idx(tmp, 1));
    if (strcmp(s, "H") == 0)
        return 0;
    return 1;
}
int isV(int index)
{
    struct json_object *tmp = json_object_array_get_idx(array, index);
    char *s = json_object_get_string(json_object_array_get_idx(tmp, 1));
    if (strcmp(s, "V") == 0)
        return 0;
    return 1;
}
void config(char *path, char *dataName)
{
    PATH = path;
    json_object_object_get_ex(parsed_json, dataName, &array);
    arr_SIZE = json_object_array_length(array);
    update = clock() + T_PRINT * CLOCKS_PER_SEC;
}
void checkProgressUpdate(void)
{
    if (clock() > update)
    {
        printf("%d/%d    %d\n", x, arr_SIZE, S);
        saveProgress();
        update = clock() + T_PRINT * CLOCKS_PER_SEC;
    }
}
void permute(int pos1, int pos2)
{
    struct json_object *tmp1 = copyStringArray(json_object_array_get_idx(array, pos1));
    struct json_object *tmp2 = copyStringArray(json_object_array_get_idx(array, pos2));
    json_object_array_put_idx(array, pos1, tmp2);
    json_object_array_put_idx(array, pos2, tmp1);
}
void eval(struct json_object *im1, struct json_object *im2)
{
    int m = 0;
    int im1_SIZE = json_object_array_length(im1);
    for (int z = 2; z < im1_SIZE; z++)
    {
        char *s = json_object_get_string(json_object_array_get_idx(im1, z));
        m += in(s, im2);
        //NEW BEST SCORE
        if (m > MAX)
        {
            MAX = m;
            BEST_CHOICE = RAND_CHOICE;
        }
    }
}
void evalH2(struct json_object *im1, struct json_object *im2, struct json_object *prev)
{
    int m = 0;
    int im1_SIZE = json_object_array_length(im1);
    for (int z = 2; z < im1_SIZE; z++)
    {
        char *s = json_object_get_string(json_object_array_get_idx(im1, z));
        if (in(s, prev) == 0)
            m += in(s, im2);
        //NEW BEST SCORE
        if (m > MAX)
        {
            MAX = m;
            BEST_CHOICE = RAND_CHOICE;
        }
    }
}
/**
 * T == 0 search  H
 * T == 1  search  V
 * */
int findNextBestChoice(int t, int p)
{
    for (int y = p; y < arr_SIZE - 1; y++)
    {
        if (t == 0 && isH(y) == 0)
            return y;
        if (t == 1 && isV(y) == 0)
            return y;
    }
    return x + 1;
}
//////////////////////////////////////////////////////////////////////
//HH
void gloutonH(int inc)
{

    checkProgressUpdate();
    //struct json_object *im1 = json_object_array_get_idx(array, x);
    struct json_object *im1 = addStringArray(json_object_array_get_idx(array, x - 1), json_object_array_get_idx(array, x - 2));
    int im1_SIZE = json_object_array_length(im1);
    struct json_object *im2;
    MAX = 0;
    BEST_CHOICE = findNextBestChoice(0, x + 1);
    for (int y = x + 1; y < arr_SIZE - 2; y++)
    {
        RAND_CHOICE = y;
        if (isH(y) == 0)
        {
            im2 = json_object_array_get_idx(array, RAND_CHOICE);
            // Count occurence
            eval(im1, im2);
        }
    }
    permute(x, BEST_CHOICE);
    S += MAX;
    x += 1;
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////

void gloutonVV(int inc)
{

    checkProgressUpdate();
    //struct json_object *im1 = addStringArray(json_object_array_get_idx(array, x - 1), json_object_array_get_idx(array, x -2));
    struct json_object *im1 = json_object_array_get_idx(array, x - 1);
    struct json_object *im2;
    int im1_SIZE = json_object_array_length(im1);
    MAX = 0;
    BEST_CHOICE = findNextBestChoice(1, x + 1);
    for (int y = x + 1; (y < (x + E) && y < arr_SIZE - 2); y++)
    {
        RAND_CHOICE = y;
        if (isV(y) == 0)
        {
            im2 = json_object_array_get_idx(array, RAND_CHOICE);
            // Count occurence
            eval(im1, im2);
        }
    }
    permute(x, BEST_CHOICE);
    x += 1;
    // Save Previous state
    struct json_object *prev = copyStringArray(json_object_array_get_idx(array, BEST_CHOICE));
    MAX = 0;
    BEST_CHOICE = findNextBestChoice(0, x + 1);
    for (int y = x + 1; (y < (x + E) && y < arr_SIZE - 2); y++)
    {
        RAND_CHOICE = y;
        if (isV(y) == 0)
        {
            im2 = json_object_array_get_idx(array, RAND_CHOICE);
            // Count occurence
            evalH2(im1, im2, prev);
        }
    }
    permute(x, BEST_CHOICE);

    S += MAX;
    x += 1;
}

void mainHVV(void)
{
    // PLACE H FIRST
    permute(0, findNextBestChoice(0, 0));
    x = 1;
    while (x < arr_SIZE - 3)
    {
        gloutonVV(0);
        gloutonH(0);
    }
    saveProgress();
    printf("%d\n", S);
}

void main(void)
{
    readJson("Hashcode/data/data1/in.txt");
    config("Hashcode/data/data1/", "array");
    mainHVV();
}
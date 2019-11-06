#include <stdio.h>
#include <json-c/json.h>
#include <unistd.h>
#include <time.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

struct json_object *parsed_json;
char *buffer;
const int T_PRINT = 10;
char *PATH;
int S = 0;
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
    // char *p = concat(PATH, "out.txt");
    //FILE *out = fopen(p, "a");
    int arr_SIZE = json_object_array_length(arr);
    int n = 0;
    for (int x = 2; x < arr_SIZE; x++)
    {
        char *s2 = json_object_get_string(json_object_array_get_idx(arr, x));
        if (strcmp(s1, s2) == 0)
        {
            //fprintf(out, "Same: %s  %s\n", s1, s2);
            n += 1;
        }
    }
    //fclose(out);
    return n;
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

void saveProgress(struct json_object *arr, int MAX)
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

void glouton(char *path, char *dataName)
{
    PATH = path;
    struct json_object *array;
    struct json_object *best;
    json_object_object_get_ex(parsed_json, dataName, &array);
    int arr_SIZE = json_object_array_length(array);
    clock_t update = clock() + T_PRINT * CLOCKS_PER_SEC;
    for (int x = 0; x < arr_SIZE - 2; x++)
    {
        if (clock() > update)
        {
            printf("%d/%d    %d\n", x, arr_SIZE, S);
            saveProgress(array, x - 2);
            update = clock() + T_PRINT * CLOCKS_PER_SEC;
        }
        struct json_object *im1 = json_object_array_get_idx(array, x);
        int MAX = 0;
        int BEST_CHOICE = x + 1;
        for (int y = x + 1; y < arr_SIZE - 1; y++)
        {
            //int RAND_CHOICE = y + randint(arr_SIZE - y - 1);
            int RAND_CHOICE = y;
            struct json_object *im2 = json_object_array_get_idx(array, RAND_CHOICE);
            // Count occurence
            int im1_SIZE = json_object_array_length(im1);
            int m = 0;
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
        struct json_object *tmp1 = copyStringArray(json_object_array_get_idx(array, x + 1));
        struct json_object *tmp2 = copyStringArray(json_object_array_get_idx(array, BEST_CHOICE));
        json_object_array_put_idx(array, x + 1, tmp2);
        json_object_array_put_idx(array, BEST_CHOICE, tmp1);
        S += MAX;
    }
}
void compareImages(json_object *im1, json_object *im2)
{
}

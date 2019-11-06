#include <stdio.h>
#include <json-c/json.h>
#include <unistd.h>

void readJson(char *json);
int in(char *s1, json_object *arr1);
void glouton(char *outStats, char *dataName);
void compareImages(json_object *im1, json_object *im2);
int randint(int n);
void saveProgress(struct json_object *arr, int MAX);
void main(void);
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * login() {
    char * username = (char *)malloc(32);
    printf("Username: ");
    scanf("%s", username);
    return username;
}

int main() {
    char * username = login();
    printf("User: %s\n", username);
}
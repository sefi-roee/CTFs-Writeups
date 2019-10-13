#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc != 2)
        return -1;

    time_t t = atol(argv[1]);

    srand(t);

    for (int i = 0; i < 30; i++)
        printf("%d\t", rand() & 0xF);
    printf("\n");

    return 0;
}
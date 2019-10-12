#include <stdio.h>

int main() {
    extern int asm4(char *);
    int ret = asm4("picoCTF_e341d");

    printf("0x%x\n", ret);

    return 0;
}
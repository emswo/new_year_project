#include <stdio.h>
int main (){
    const char* string = "ggggqwer d v g";
    //const char* string1 = "asdffghj";
    //const char* string2 = "safa";
    //const char* string3 = "ggggqwer";
    char dest[100] = {0};
    char dest2[100] = {0};
    
    sscanf(string, "%*s %s %s %*s", dest,dest2);
    
    printf("%s\n", dest);
    printf("%s\n", dest2);
        while(1);
    return 0;
}
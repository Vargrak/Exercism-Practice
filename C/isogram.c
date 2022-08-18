#include "isogram.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define ALLOC_SIZE 32

bool is_isogram(char phrase[])
{
    if (phrase == NULL) return false;

    char *read, *write, *write_address;
    char *used_chars;
    used_chars = (char *)calloc(ALLOC_SIZE, sizeof(char));
    write_address = used_chars;

    //for every char in the phrase
    for (read = phrase; *read != '\0'; read++)
    {
        //check if it exists in used_chars
        for (write = used_chars; *write != '\0'; write++)
        {
            if ((*read >= 'a' && *read <= 'z') || (*read >= 'A' && *read <= 'Z'))
            {
                if ((*read == *write) || (*read == (*write - 32)) || (*read == (*write + 32))) return false;
            }
        }

        //append to used_chars
        if (*read != '\0') *write_address = *read;
        write_address++;
    }

    return true;
}
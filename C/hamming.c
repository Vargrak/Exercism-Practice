#include "hamming.h"
#include <stdio.h>


int compute(const char *lhs, const char *rhs)
{
    int hamming_num = 0;
    while (1)
    {
        if (*lhs != *rhs) hamming_num++;
        lhs++;
        rhs++;
        if (*rhs == '\0' || *lhs == '\0')
        {
            if (*rhs == '\0' && *lhs == '\0') return hamming_num;
            return -1;
        }
    }
}
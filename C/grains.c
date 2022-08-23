#include "grains.h"
#include <stdio.h>
#include <math.h>

uint64_t square(uint8_t index)
{
    if (index > 64 || index < 1) return 0;
    return (uint64_t)(pow(2, (double)index)/2);
}

uint64_t total(void)
{
    return (uint64_t)(pow(2, 64)-1);
}
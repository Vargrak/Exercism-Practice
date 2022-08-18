#include "resistor_color.h"

int color_code(resistor_band_t color)
{
    return color;
}

resistor_band_t *colors()
{
    static resistor_band_t group[10];
    for (resistor_band_t current = BLACK; current <= WHITE; current++)
    {
        group[current] = current;
    }

    return group;
}


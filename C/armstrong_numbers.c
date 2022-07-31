#include "armstrong_numbers.h"
#include <math.h>
bool is_armstrong_number(int candidate)
{
    int sum = 0;
    int digit_count = 0;
    int temp = candidate;
    
    while (temp != 0)
    {
        temp /= 10;
        digit_count++;
    }

    temp = candidate;
    while (temp != 0)
    {
        int digit = temp % 10;
        sum += pow(digit, digit_count);
        temp /= 10;
    }
    return sum == candidate;
}
using System;
using System.Collections.Generic;
// WIP - Issues with bit shifting and reversed on some byte values
public static class VariableLengthQuantity
{
    public static uint[] Encode(uint[] numbers)
    {
        List<uint> encoded_VLQ = new List<uint>();
        if (numbers[0] == 0)
            return numbers;
        
        uint temp = 0;
        foreach (uint number in numbers)
            temp += number;
        

        uint msb = 0x00;
        while (temp > 0)
        {
            uint encoded_number = (msb ^ (temp & 0x7F));
            temp >>= 7;
            Console.WriteLine(Convert.ToString(encoded_number, 2));
            encoded_VLQ.Insert(0, encoded_number);
            if (msb == 0x00)
                msb = 0x80;
        }
        return encoded_VLQ.ToArray();
    }

    public static uint[] Decode(uint[] bytes)
    {
        throw new NotImplementedException("You need to implement this function.");
    }
}
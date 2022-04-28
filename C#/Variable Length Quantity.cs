using System;
using System.Collections.Generic;
public static class VariableLengthQuantity
{
    public static uint[] Encode(uint[] numbers)
    {
        Array.Reverse(numbers);
        List<uint> encoded_VLQ = new List<uint>();
        
        uint temp = 0;
        foreach (uint number in numbers)
        {
            if (number != 0)
            {
                temp = number;
                uint msb = 0b00000000;
                while (temp > 0)
                {
                    uint encoded_number = (msb ^ (temp & 0b01111111));
                    temp >>= 7;
                    encoded_VLQ.Insert(0, encoded_number);
                    if (msb == 0x00)
                        msb = 0b10000000;
                }
            }
            else
                encoded_VLQ.Insert(0, number);
        }
        return encoded_VLQ.ToArray();
    }

    public static uint[] Decode(uint[] bytes)
    {
        if (bytes[bytes.Length - 1] != 0 && bytes[bytes.Length - 1] != 127)
            throw new InvalidOperationException("Last byte error");

        List<uint> decoded_VLQ = new List<uint>();
        uint temp = 0;
        foreach (uint byte_value in bytes)
        {
            temp <<= 7;
            temp |= (byte_value & 0b01111111);
            if ((byte_value & 0b10000000) == 0)
            {
                decoded_VLQ.Add(temp);
                temp = 0;
            }
        }
        Array.Reverse(decoded_VLQ.ToArray());
        return decoded_VLQ.ToArray();
    }
}
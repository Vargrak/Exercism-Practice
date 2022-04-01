using System;
using System.Linq;

public static class TelemetryBuffer
{
    public static byte[] ToBuffer(long reading)
    {

        byte[] buffer = new byte[9];

        //buffer is 9 bytes long. The first byte contains the type's byte size e.g. 8 bytes for long. If it is a signed type, the number is 256 - the number of bytes.
        if (reading >= 0)
        {
            //ulong
            if (reading > long.MaxValue)
            {
                buffer[0] = (byte)(8);
                BitConverter.GetBytes(reading).CopyTo(buffer, 1);
                return buffer;
            }
            //long
            else if (reading > uint.MaxValue)
            {
                buffer[0] = (byte)(256 - 8);
                BitConverter.GetBytes(reading).CopyTo(buffer, 1);
                return buffer;
            }
            else if (reading > int.MaxValue)
            {
                buffer[0] = (byte)(4);
                BitConverter.GetBytes(reading).CopyTo(buffer, 1);
                return buffer;
            }
            else if (reading > ushort.MaxValue)
            {
                buffer[0] = (byte)(256 - 4);
                BitConverter.GetBytes(reading).CopyTo(buffer, 1);
                return buffer;
            }
            else
            {
                buffer[0] = (byte)(2);
                BitConverter.GetBytes(reading).CopyTo(buffer, 1);
                return buffer;
            }
        }
        else if (reading < 0)
        {
            if (reading < int.MinValue)
            {
                buffer[0] = (byte)(256 - 8);
                BitConverter.GetBytes(reading).CopyTo(buffer, 1);
                return buffer;
            }

            //casting need here else it takes up too much of the buffer
            //no idea why it doesn't need this for the positive numbers
            else if (reading < short.MinValue)
            {
                buffer[0] = (byte)(256 - 4);
                BitConverter.GetBytes((int)reading).CopyTo(buffer, 1);
                return buffer;
            }
            else
            {
                buffer[0] = (byte)(256 - 2);
                BitConverter.GetBytes((short)reading).CopyTo(buffer, 1);
                return buffer;
            }
        } 
        else
        {
            return null;
        }    
    }

    public static long FromBuffer(byte[] buffer)
    {
        if ((256 - buffer[0]) == 8)
        {
            return BitConverter.ToInt64(buffer, 1);
        }
        else if ((256 - buffer[0]) == 4)
        {
            return BitConverter.ToInt32(buffer, 1);
        }
        else if ((256 - buffer[0]) == 2)
        {
            return BitConverter.ToInt16(buffer, 1);
        }
        else if (buffer[0] == 8)
        {
            return BitConverter.ToInt64(buffer, 1);
        }
        else if (buffer[0] == 4)
        {
            return BitConverter.ToUInt32(buffer, 1);
        }
        else if (buffer[0] == 2)
        {
            return BitConverter.ToUInt16(buffer, 1);
        }
        else
        {
            return 0;
        }

    }
}

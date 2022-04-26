using System;
using System.Collections.Generic;
using System.Linq;

public class SpiralMatrix
{
    public static int[,] GetMatrix(int size)
    {
        int x = 1;
        int y = 1;
        int xbound = size + 1;
        int ybound = size + 1;
        int xboundMin = 0;
        int yboundMin = 0;
        int direction = 1;
        Dictionary<int, Tuple<int, int>> spiral = new Dictionary<int, Tuple<int, int>>();
        while (spiral.Count < (size * size))
        {
            if ( x < xbound && y < ybound && x > xboundMin && y > yboundMin && !spiral.ContainsValue(new Tuple<int, int>(x, y)))
            {
                spiral.Add(spiral.Count + 1, new Tuple<int, int>(x, y));
            }
            if (direction == 1 && y + 1 < ybound && !spiral.ContainsValue(new Tuple<int, int>(x, y + 1)))
            {
                y++;
            }
            else if (direction == 2 && x + 1 < xbound && !spiral.ContainsValue(new Tuple<int, int>(x + 1, y)))
            {
                x++;
            }
            else if (direction == 3 && y - 1 > yboundMin && !spiral.ContainsValue(new Tuple<int, int>(x, y - 1)))
            {
                y--;
            }
            else if (direction == 4 && x - 1 > xboundMin && !spiral.ContainsValue(new Tuple<int, int>(x - 1, y)))
            {
                x--;
            }
            else
            {
                direction++;
                if (direction == 5)
                {
                    direction = 1;
                    xbound--;
                    ybound--;
                    xboundMin++;
                    yboundMin++;
                }
            }
        }
        int[,] matrix = new int[size, size];
        foreach (int key in spiral.OrderBy(x => x.Value).Select(x => x.Key).ToList())
        {
            matrix[spiral[key].Item1 - 1, spiral[key].Item2 - 1] = key;
        }
        return matrix;
    }
}
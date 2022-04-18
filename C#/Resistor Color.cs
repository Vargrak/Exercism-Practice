using System;
using System.Collections.Generic;
using System.Linq;

public static class ResistorColor
{
    public static Dictionary<int, string> ColorDict = new Dictionary<int, string>()
    {
        {0, "black"},
        {1, "brown"},
        {2, "red"},
        {3, "orange"},
        {4, "yellow"},
        {5, "green"},
        {6, "blue"},
        {7, "violet"},
        {8, "grey"},
        {9, "white"}
    };

    public static int ColorCode(string color) => ColorDict.First(val => val.Value == color).Key;

    public static string[] Colors() => ColorDict.Values.ToArray();
}
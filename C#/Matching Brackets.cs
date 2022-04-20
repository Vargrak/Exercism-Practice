using System;
using System.Collections.Generic;

public static class MatchingBrackets
{
    public static bool IsPaired(string input)
    {
        Stack<string> order = new Stack<string>();
        Dictionary<string, string> braceTable = new Dictionary<string, string>()
        {
            { "{", "}" },
            { "[", "]" },
            { "(", ")" }
        };
        foreach (char c in input)
        {
            if (braceTable.ContainsKey(c.ToString()))
            {
                order.Push(c.ToString());
            }
            else if (braceTable.ContainsValue(c.ToString()))
            {
                if (order.Count == 0)
                {
                    return false;
                }
                if (braceTable[order.Pop()] != c.ToString())
                {
                    return false;
                }
            }
        }
        return order.Count == 0;
    }
}

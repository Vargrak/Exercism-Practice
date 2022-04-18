using System;
using System.Collections.Generic;

public static class NucleotideCount
{
    public static Dictionary<char, int> Count(string sequence)
    {
        Dictionary<char, int> Tally = new Dictionary<char, int>
        {
            {'A', 0},
            {'C', 0},
            {'G', 0},
            {'T', 0}
        };
        foreach (char c in sequence)
        {
            if (Tally.ContainsKey(c))
            {
                Tally[c]++;
            }
            else
            {
                throw new ArgumentException("Invalid nucleotide in sequence.");
            }
        }
        return Tally;
    }
}
using System;
using System.Text;


public static class Identifier
{
    public static string Clean(string identifier)
    {
        if (string.IsNullOrEmpty(identifier))
        {
            return identifier;
        }
        
        var dashIsPresent = false;

        StringBuilder sb = new StringBuilder();
        foreach (char c in identifier)
        {

                if (' '.Equals(c))
                {
                    sb.Append("_");
                }
                else if (char.IsControl(c))
                {
                    sb.Append("CTRL");
                }
                else if ('-'.Equals(c))
                { 
                    dashIsPresent = true;
                }
                else if (dashIsPresent == true)
                { 
                    sb.Append(char.ToUpperInvariant(c));
                    dashIsPresent = false;
                }
                else if (char.IsLetter(c) & !(c >= 'α' && c <= 'ω'))
                { 
                    sb.Append(c);
                }
            }
        
    string cleaned = sb.ToString();

    return cleaned;

    }
}
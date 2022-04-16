using System;
using System.Text.RegularExpressions;
using System.Collections.Generic;

public class LogParser
{
    public bool IsValidLine(string text)
    {
        return Regex.IsMatch(text, @"^(\[TRC\])|^(\[ERR\])|^(\[DBG\])|^(\[INF\])|^(\[WRN\])|^(\[FTL\])");
    }

    public string[] SplitLogLine(string text)
    {
        return Regex.Split(text, @"<\**\^*-*=*>");
    }

    public int CountQuotedPasswords(string lines)
    {
        return Regex.Matches(lines, @""".*password.*""", RegexOptions.Multiline | RegexOptions.IgnoreCase).Count;
    }

    public string RemoveEndOfLineText(string line)
    {
        return Regex.Replace(line, @"end-of-line\w*", "");
    }

    public string[] ListLinesWithPasswords(string[] lines)
    {
        List<string> result = new List<string>();
        foreach (string line in lines)
        {
            if (Regex.IsMatch(line, @"password\S+", RegexOptions.IgnoreCase))
            {
                result.Add($"{Regex.Match(line, @"password\S+", RegexOptions.IgnoreCase)}: {line}");
            }
            else
            {
                result.Add($"--------: {line}");
            }
        }
        return result.ToArray();
    }
}

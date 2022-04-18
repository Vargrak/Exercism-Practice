using System;

public static class LogAnalysis 
{
    // TODO: define the 'SubstringAfter()' extension method on the `string` type
    public static string SubstringAfter(this string str, string substr)
    {
        return str.Substring(str.IndexOf(substr) + substr.Length);
    }

    // TODO: define the 'SubstringBetween()' extension method on the `string` type
    public static string SubstringBetween(this string str, string substr1, string substr2)
    {
        return str.Substring(str.IndexOf(substr1) + substr1.Length, str.IndexOf(substr2) - str.IndexOf(substr1) - substr1.Length);
    }
    
    // TODO: define the 'Message()' extension method on the `string` type
    public static string Message(this string str)
    {
        return str.SubstringAfter(": ");
    }

    // TODO: define the 'LogLevel()' extension method on the `string` type
    public static string LogLevel(this string str)
    {
        return str.SubstringBetween("[", "]"); 
    }
}
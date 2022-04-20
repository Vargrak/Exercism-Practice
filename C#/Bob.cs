using System;

public static class Bob
{
    public static string Response(string statement)
    {
        return statement switch
        {
            _ when statement.ToUpper() == statement & statement.ToLower() != statement => (statement.EndsWith("?")) ? "Calm down, I know what I'm doing!" : "Whoa, chill out!",
            _ when statement.Trim().EndsWith("?")=> "Sure.",
            _ when statement.Trim() == "" => "Fine. Be that way!",
            _ => "Whatever."
        };
    }
}
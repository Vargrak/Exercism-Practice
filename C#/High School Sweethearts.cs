using System;
using System.Globalization;

public static class HighSchoolSweethearts
{
    public static string DisplaySingleLine(string studentA, string studentB) => $"{studentA.PadLeft(29, ' ')} ♡ {studentB.PadRight(29, ' ')}";
    
    public static string DisplayBanner(string studentA, string studentB)
    {
       string heart = @"
     ******       ******
   **      **   **      **
 **         ** **         **
**            *            **
**                         **
**     {0} +  {1}    **
 **                       **
   **                   **
     **               **
       **           **
         **       **
           **   **
             ***
              *
        ";
        return string.Format(heart, studentA, studentB);
    }

    public static string DisplayGermanExchangeStudents(string studentA
        , string studentB, DateTime start, float hours) => $"{studentA} and {studentB} have been dating since {start.ToString("dd.MM.yyyy")} - that's {hours.ToString("0,000.00", CultureInfo.CreateSpecificCulture("de-DE"))} hours"; 
}

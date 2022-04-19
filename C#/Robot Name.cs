using System;
using System.Threading;
using System.Text;
using System.Collections.Generic;


public class Robot
{
    public Robot()
    {
        this.Name = NameGen();
    }

    public string Name;

    public static List<string> robotNames = new List<string>();

    public static string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public string NameGen()
    {
        Random rnd = new Random();
        StringBuilder sb = new StringBuilder();
        string name = sb.Append(letters[rnd.Next(0, letters.Length)]).Append(letters[rnd.Next(0, letters.Length)]).Append(rnd.Next(0, 9)).Append(rnd.Next(0, 9)).Append(rnd.Next(0, 9)).ToString();
        if (robotNames.Contains(name))
        {
            return NameGen();
        }
        else
        {
            robotNames.Add(name);
            return name;
        }
    }

    public void Reset()
    {
        this.Name = NameGen();
    }
}
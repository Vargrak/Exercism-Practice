using System;

public static class PlayAnalyzer
{
    public static string AnalyzeOnField(int shirtNum)
    {
        return shirtNum switch
        {
            1 => "goalie",
            2 => "left back",
            3 or 4 => "center back",
            5 => "right back",
            6 or 7 or 8 => "midfielder",
            9 => "left wing",
            10 => "striker",
            11 => "right wing",
            _ => throw new ArgumentOutOfRangeException("No such player"),
        };
    }

    public static string AnalyzeOffField(object report)
    {
        return report switch
        {
            int => $"There are {report} supporters at the match.",
            string => $"{report}",
            Foul f => $"{f.GetDescription()}",
            Injury i => $"Oh no! {i.GetDescription()} Medics are on the field.",
            Incident n => n.GetDescription(),
            Manager m when m.Club != null => $"{m.Name} ({m.Club})",
            Manager m when m.Club == null => $"{m.Name}",
            _ => throw new ArgumentException("Invalid report"),
        };
    }
}
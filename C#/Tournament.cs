using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

public static class Tournament
{   
    public static void Tally(Stream inStream, Stream outStream)
    {
        // Team Name Key - Value Tuple (Wins, Losses, Draws)
        Dictionary<string, List<int>> teams = new Dictionary<string, List<int>>();
        using (StreamReader read = new StreamReader(inStream))
        using (StreamWriter write = new StreamWriter(outStream))
            {
                foreach (string line in read.ReadToEnd().Split('\n'))
                {
                    if (line.Length == 0)
                        break;
                        
                    string[] input = line.Split(';');

                    switch (input[2])
                    {
                        case "win":
                            if (teams.ContainsKey(input[0]))
                            {
                                teams[input[0]][0]++;
                            }
                            else
                            {
                                teams.Add(input[0], new List<int> { 1, 0, 0 });
                            }
                            if (teams.ContainsKey(input[1]))
                            {
                                teams[input[1]][1]++;
                            }
                            else
                            {
                                teams.Add(input[1], new List<int> { 0, 1, 0 });
                            }
                            break;
                        case "loss":
                            if (teams.ContainsKey(input[0]))
                            {
                                teams[input[0]][1]++;
                            }
                            else
                            {
                                teams.Add(input[0], new List<int> { 0, 1, 0 });
                            }
                            if (teams.ContainsKey(input[1]))
                            {
                                teams[input[1]][0]++;
                            }
                            else
                            {
                                teams.Add(input[1], new List<int> { 1, 0, 0 });
                            }
                            break;
                        case "draw":
                            if (teams.ContainsKey(input[0]))
                            {
                                teams[input[0]][2]++;
                            }
                            else
                            {
                                teams.Add(input[0], new List<int> { 0, 0, 1 });
                            }
                            if (teams.ContainsKey(input[1]))
                            {
                                teams[input[1]][2]++;
                            }
                            else
                            {
                                teams.Add(input[1], new List<int> { 0, 0, 1 });
                            }
                            break;
                    }
                }

                write.Write("Team                           | MP |  W |  D |  L |  P");

                if (teams.Count > 0)
                {
                    foreach (KeyValuePair<string, List<int>> team in teams.OrderByDescending(x => x.Value[0]).ThenBy(x => x.Value[1]).ThenBy(x => x.Key))
                    {
                        write.Write($"\n{team.Key.PadRight(31)}|  {team.Value[0]+team.Value[1]+team.Value[2]} |  {team.Value[0]} |  {team.Value[2]} |  {team.Value[1]} |{((team.Value[0] * 3) + team.Value[2]).ToString().PadLeft(3)}");
                    }
                }
            }
    }
}

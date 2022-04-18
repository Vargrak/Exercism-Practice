using System;
using System.Collections.Generic;
using System.Linq;

public class HighScores
{
    public List<int> scoreList;

    public HighScores(List<int> list)
    {
        this.scoreList = list;
    }

    public List<int> Scores() => scoreList;

    public int Latest() => scoreList[scoreList.Count - 1];

    public int PersonalBest() => scoreList.Max();

    public List<int> PersonalTopThree() => scoreList.OrderByDescending(x => x).Take(3).ToList();
}
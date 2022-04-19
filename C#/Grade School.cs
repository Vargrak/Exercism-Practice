using System;
using System.Collections.Generic;
using System.Linq;

public class GradeSchool
{
    public Dictionary<int, List<string>> roster = new Dictionary<int, List<string>>();

    public void Add(string student, int grade)
    {
        if (!roster.ContainsKey(grade))
        {
            roster.Add(grade, new List<string>());
        }
        roster[grade].Add(student);
    }

    public IEnumerable<string> Roster()
    {
        foreach (var key in roster.Keys.OrderBy(x => x))
        {
            foreach (var student in roster[key].OrderBy(x => x))
            {
                yield return student;
            }
        }
    }

    public IEnumerable<string> Grade(int grade)
    {
        if (!roster.ContainsKey(grade))
        {
            return new List<string>();
        }
        return roster[grade].OrderBy(x => x);
    }
}
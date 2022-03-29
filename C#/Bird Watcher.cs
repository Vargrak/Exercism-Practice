using System;

class BirdCount
{
    private int[] birdsPerDay;
    
    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        int[] LWBirds = {0, 2, 5, 3, 7, 8, 4};
        return LWBirds;
    }

    public int Today()
    {
        return this.birdsPerDay[birdsPerDay.Length - 1];
    }

    public void IncrementTodaysCount()
    {
        this.birdsPerDay[birdsPerDay.Length - 1]++;
    }

    public bool HasDayWithoutBirds()
    {
        if (Array.Exists(birdsPerDay, x => x == 0))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public int CountForFirstDays(int numberofDays)
    {
        int count = 0;
        for (int i = 0; i < numberofDays; i++)
        {
            count += this.birdsPerDay[i];
        }
        return count;
    }

    public int BusyDays()
    {
        int count = 0;
        for (int i = 0; i < this.birdsPerDay.Length; i++)
        {
            if (this.birdsPerDay[i] >= 5)
            {
                count++;
            }
        }
        return count;
    }
}
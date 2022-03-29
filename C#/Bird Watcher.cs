using System;

class BirdCount
{
    private int[] birdsPerDay;

    private int[] birdsLastWeek = new int[0, 2, 5, 3, 7, 8, 4];

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        return this.birdsLastWeek;
    }

    public int Today()
    {
        
    }

    public void IncrementTodaysCount()
    {

    }

    public bool HasDayWithoutBirds()
    {

    }

    public int BusyDays()
    {

    }
}
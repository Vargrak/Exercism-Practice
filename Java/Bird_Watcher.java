
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() 
    {
        return this.birdsPerDay;
    }

    public int getToday() 
    {
        if (this.birdsPerDay.length == 0)
            return 0;
        return this.birdsPerDay[this.birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() 
    {
        birdsPerDay[birdsPerDay.length - 1]++;
    }

    public boolean hasDayWithoutBirds() {
        for (int i = 0; i < birdsPerDay.length; i++)
        {
            if (birdsPerDay[i] == 0)
                return true;

        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) 
    {
        int count = 0;
        if (numberOfDays > birdsPerDay.length)
        {
            if (numberOfDays <= 0)
                return 0;
    
            numberOfDays = birdsPerDay.length;
        }
        


        for (int i = 0; i < numberOfDays; i++)
        {
            count += birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() 
    {
        int busyDays = 0;
        for(int i = 0; i < birdsPerDay.length; i++)
        {
            if (birdsPerDay[i] >= 5)
                busyDays++;   
        }
        return busyDays;
    }
}

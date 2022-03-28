using System;

static class AssemblyLine
{
    public static double SuccessRate(int speed)
    {
        switch (speed)
        {
            case 0:
                return 0.00;
            case 1: case 2: case 3: case 4:
                return 1.00;
            case 5: case 6: case 7: case 8:
                return 0.90;
            case 9:
                return 0.80;
            case 10:
                return 0.77;
            default:
                return 0.00;
        }
    }
    
    public static double ProductionRatePerHour(int speed)
    {
        return SuccessRate(speed) * (speed * 221);
    }

    public static int WorkingItemsPerMinute(int speed)
    {
        return (int)(ProductionRatePerHour(speed) / 60);
    }
}
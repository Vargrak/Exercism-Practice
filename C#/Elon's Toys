using System;

class RemoteControlCar
{
    //Fields
    private int DistanceTraveled = 0;

    private int BatteryPercentage = 100;

    public static RemoteControlCar Buy()
    {
        return new RemoteControlCar();
    }

    public string DistanceDisplay()
    {
        return $"Driven {DistanceTraveled} meters";
    }

    public string BatteryDisplay()
    {
        if (BatteryPercentage != 0)
        {
            return $"Battery at {BatteryPercentage}%";
        }

        return "Battery empty";
    }

    public void Drive()
    {
        if (BatteryPercentage != 0)
        {
            DistanceTraveled += 20;
            BatteryPercentage -= 1;
        }
    }
}
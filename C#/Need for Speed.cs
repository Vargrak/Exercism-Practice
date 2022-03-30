using System;

class RemoteControlCar
{
    public int Speed;

    public int BatteryDrain;

    public int BatteryCapacity;

    public int distanceTotal;

    // TODO: define the constructor for the 'RemoteControlCar' class
    public RemoteControlCar(int Speed, int BatteryDrain)
    {
        this.Speed = Speed;
        this.BatteryDrain = BatteryDrain;
        this.BatteryCapacity = 100;
        this.distanceTotal = 0;
    }

    public bool BatteryDrained()
    {
        if (this.BatteryCapacity < this.BatteryDrain)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public int DistanceDriven()
    {
        return this.distanceTotal;
    }

    public void Drive()
    {
        if (!(this.BatteryDrained()))
        {
            this.distanceTotal += this.Speed;
            this.BatteryCapacity -= this.BatteryDrain;
        }
    }

    public static RemoteControlCar Nitro()
    {
        return new RemoteControlCar(50, 4);
    }
}

class RaceTrack
{
    // TODO: define the constructor for the 'RaceTrack' class
    public int distance;

    public RaceTrack(int distance)
    {
        this.distance = distance;
    }

    public bool TryFinishTrack(RemoteControlCar car)
    {
        while (!(car.BatteryDrained()))
        {
            car.Drive();
        }
        if (car.DistanceDriven() >= this.distance)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

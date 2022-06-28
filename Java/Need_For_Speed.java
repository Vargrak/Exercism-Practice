class NeedForSpeed 
{
    public int speed;
    public int distanceTotal;
    public int battery;
    public int batteryDrain;

    public NeedForSpeed(int speed, int batteryDrain)
    {
        this.speed = speed;
        this.distanceTotal = 0;
        this.batteryDrain = batteryDrain;
        this.battery = 100;
    }

    public boolean batteryDrained() 
    {
        return this.battery == 0;
    }

    public int distanceDriven() 
    {
        return this.distanceTotal;
    }

    public void drive() 
    {
        if (!batteryDrained())
        {
            distanceTotal += speed;
            battery -= batteryDrain;
        }
    }

    public static NeedForSpeed nitro() 
    {
        return new NeedForSpeed(50, 4);
    }
}

class RaceTrack 
{

    int trackLength;

    public RaceTrack(int trackLength)
    {
        this.trackLength = trackLength;
    }

    public boolean tryFinishTrack(NeedForSpeed car) 
    {
        while (car.battery != 0)
        {
            car.drive();
        }

        return car.distanceTotal >= this.trackLength;
    }
}

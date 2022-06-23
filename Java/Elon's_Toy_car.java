public class ElonsToyCar 
{

    int distance;
    int battery;

    public ElonsToyCar()
    {
        distance = 0;
        battery = 100;
    }

    public static ElonsToyCar buy() 
    {
        return new ElonsToyCar();
    }

    public String distanceDisplay() 
    {
        return "Driven "  + Integer.toString(distance) + " meters";
    }

    public String batteryDisplay() 
    {
        if (this.battery == 0)
        {
            return "Battery empty";
        }
        return "Battery at " + Integer.toString(battery) + "%";
    }

    public void drive() 
    {
        if (this.battery >= 1)
        {
            this.battery -= 1;
            this.distance += 20;
        }
    }
}

using System;

public class Clock
{
    public int hours;
    public int minutes;

    public Clock(int hours, int minutes)
    {
        this.hours = hours;
        this.hours += minutes / 60;
        this.minutes = minutes % 60;
        Boundary_Pass();
    }

    public Clock Add(int minutesToAdd)
    {
        return new Clock(hours, minutes + minutesToAdd);
    }

    public Clock Subtract(int minutesToSubtract)
    {
        return Add(-minutesToSubtract);
    }

    public void Boundary_Pass()
    {
        while (this.hours < 0)
        {
            this.hours += 24;
        }
        while (this.hours > 23)
        {
            this.hours -= 24;
        }
        while (this.minutes < 0)
        {
            this.minutes += 60;
            this.hours -= 1;
        }
        while (this.minutes > 59)
        {
            this.minutes -= 60;
            this.hours += 1;
        }
        if (this.hours < 0 || this.hours > 23 || this.minutes < 0 || this.minutes > 59)
        {
            Boundary_Pass();
        }
    }

    public interface IEquitable
    {
        bool Equals(object obj);
    }

    public override bool Equals(object obj)
    {
        return this.hours == ((Clock)obj).hours && this.minutes == ((Clock)obj).minutes;
    }

    public override string ToString()
    {
        return $"{this.hours:D2}:{this.minutes:D2}";
    }
}

using System;

public class SpaceAge
{
    public int seconds;

    public SpaceAge(int seconds)
    {
        this.seconds = seconds;
    }

    public double OnEarth() => (double)this.seconds / 31557600;

    public double OnMercury() => Math.Round(OnEarth() / 0.2408467, 2);

    public double OnVenus() => Math.Round(OnEarth() / 0.61519726, 2);

    public double OnMars() => Math.Round(OnEarth() / 1.8808158, 2);

    public double OnJupiter() => Math.Round(OnEarth() / 11.862615, 2);

    public double OnSaturn() => Math.Round(OnEarth() / 29.447498, 2);

    public double OnUranus() => Math.Round(OnEarth() / 84.016846, 2);

    public double OnNeptune() => Math.Round(OnEarth() / 164.79132, 2);
}
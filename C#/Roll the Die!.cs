using System;

public class Player
{
    Random Random = new Random();
    public int RollDie()
    {
        return Random.Next(1, 18);
    }

    public double GenerateSpellStrength()
    {
        return Random.NextDouble() * 100;
    }
}

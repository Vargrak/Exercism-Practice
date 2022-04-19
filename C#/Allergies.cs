using System;
using System.Collections.Generic;

public enum Allergen
{
    Eggs = 0b00000001,
    Peanuts = 0b00000010,
    Shellfish = 0b00000100,
    Strawberries = 0b00001000,
    Tomatoes = 0b00010000,
    Chocolate = 0b00100000,
    Pollen = 0b01000000,
    Cats = 0b10000000
}

public class Allergies
{
    public List<Allergen> allergies;

    public Allergies(int mask)
    {
        this.allergies = new List<Allergen>();
        foreach (Allergen allergen in Enum.GetValues(typeof(Allergen)))
        {
            if ((mask & (int)allergen) == (int)allergen)
            {
                this.allergies.Add(allergen);
            }
        }
    }

    public bool IsAllergicTo(Allergen allergen)
    {
        return this.allergies.Contains(allergen);
    }

    public Allergen[] List()
    {
        return this.allergies.ToArray();
    }
}
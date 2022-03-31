using System;

abstract class Character
{

    public string characterType;

    protected Character(string characterType)
    {
        this.characterType = characterType;
    }

    public abstract int DamagePoints(Character target);

    public virtual bool Vulnerable()
    {
        return false;
    }


    public override string ToString()
    {
        return $"Character is a {characterType}";
    }
}

class Warrior : Character
{
    public Warrior() : base("Warrior")
    {
       
    }

    public override int DamagePoints(Character target)
    {
        if (target.Vulnerable())
        {
            return 10;
        }
        else
        {
            return 6;
        }
    }
}

class Wizard : Character
{
    public bool preparedSpell;

    public Wizard() : base("Wizard")
    {
        this.preparedSpell = false;
    }

    public override int DamagePoints(Character target)
    {
        if (preparedSpell)
        {
            return 12;
        }
        else
        {
            return 3;
        }
    }

    public void PrepareSpell()
    {
        this.preparedSpell = true;
    }

    public override bool Vulnerable()
    {
        if (this.preparedSpell)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
}
using System;

class WeighingMachine
{

    public int Precision;

    public WeighingMachine(int precision)
    {
        this.Precision = precision;
    }

    private double weight;
    public double Weight
    {
        get { return weight; }
        set { 

            weight = value switch

                {
                    _ when value < 0 => throw new ArgumentOutOfRangeException("Weight cannot be negative"),
                    _ => value
                };
            }
    }
    public string DisplayWeight
    {
        get { 
                return $"{Math.Round((weight + -TareAdjustment), Precision).ToString("0." + new string('0', Precision))} kg"; 
            }
    }
    public double TareAdjustment { get; set; } = 5;

}


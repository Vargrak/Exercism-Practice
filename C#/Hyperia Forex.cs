using System;

public struct CurrencyAmount
{
    private decimal amount;
    private string currency;

    public CurrencyAmount(decimal amount, string currency)
    {
        this.amount = amount;
        this.currency = currency;
    }

    //check if the currency is valid
    public static bool IsSameCurrency(CurrencyAmount a, CurrencyAmount b) => a.currency == b.currency ? true : throw new ArgumentException("Currencies must be the same");

    //equality operators
    public static bool operator ==(CurrencyAmount a, CurrencyAmount b) =>  IsSameCurrency(a, b) && (a.amount == b.amount);

    public static bool operator !=(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a, b) && (a.amount != b.amount);
    
    //comparison operators
    public static bool operator <(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a, b) && a.amount < b.amount;

    public static bool operator >(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a, b) && a.amount > b.amount;

    public static bool operator <=(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a, b) && a.amount <= b.amount;

    public static bool operator >=(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a, b) && a.amount >= b.amount;

    //arithmetic operators  (addition, subtraction, multiplication, division)                                                                                  //digusting
    public static CurrencyAmount operator +(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a,b) ? new CurrencyAmount(a.amount + b.amount, a.currency) : throw new ArgumentException("Currencies must be the same");

    public static CurrencyAmount operator -(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a,b) ? new CurrencyAmount(a.amount - b.amount, a.currency) : throw new ArgumentException("Currencies must be the same");

    public static CurrencyAmount operator *(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a,b) ? new CurrencyAmount(a.amount * b.amount, a.currency) : throw new ArgumentException("Currencies must be the same");

    public static CurrencyAmount operator /(CurrencyAmount a, CurrencyAmount b) => IsSameCurrency(a,b) ? new CurrencyAmount(a.amount / b.amount, a.currency) : throw new ArgumentException("Currencies must be the same");

    //currency first with decimal
    public static CurrencyAmount operator +(CurrencyAmount a, decimal b) => new CurrencyAmount(a.amount + b, a.currency);

    public static CurrencyAmount operator -(CurrencyAmount a, decimal b) => new CurrencyAmount(a.amount - b, a.currency);

    public static CurrencyAmount operator *(CurrencyAmount a, decimal b) => new CurrencyAmount(a.amount * b, a.currency);

    public static CurrencyAmount operator /(CurrencyAmount a, decimal b) => new CurrencyAmount(a.amount / b, a.currency);

    //decimal first with currency
    public static CurrencyAmount operator +(decimal a, CurrencyAmount b) => new CurrencyAmount(a + b.amount, b.currency);

    public static CurrencyAmount operator -(decimal a, CurrencyAmount b) => new CurrencyAmount(a - b.amount, b.currency);

    public static CurrencyAmount operator *(decimal a, CurrencyAmount b) => new CurrencyAmount(a * b.amount, b.currency);

    public static CurrencyAmount operator /(decimal a, CurrencyAmount b) => new CurrencyAmount(a / b.amount, b.currency);

    //conversion operators
    public static implicit operator decimal(CurrencyAmount a) => (decimal)a.amount;

    public static implicit operator double(CurrencyAmount a) => (double)a.amount;
}

using System;
using System.Globalization;

public enum Location
{
    NewYork,
    London,
    Paris
}

public enum AlertLevel
{
    Early,
    Standard,
    Late
}

public static class Appointment
{
    public static TimeZoneInfo NY = TimeZoneInfo.FindSystemTimeZoneById("Eastern Standard Time");
    public static TimeZoneInfo London = TimeZoneInfo.FindSystemTimeZoneById("GMT Standard Time");
    public static TimeZoneInfo Paris = TimeZoneInfo.FindSystemTimeZoneById("Central European Standard Time");

    public static DateTime ShowLocalTime(DateTime dtUtc) => dtUtc.ToLocalTime();

    public static DateTime Schedule(string appointmentDateDescription, Location location)
    {
        return location switch
        {
            Location.NewYork => TimeZoneInfo.ConvertTimeToUtc(DateTime.Parse(appointmentDateDescription), NY),
            Location.London => TimeZoneInfo.ConvertTimeToUtc(DateTime.Parse(appointmentDateDescription), London),
            Location.Paris => TimeZoneInfo.ConvertTimeToUtc(DateTime.Parse(appointmentDateDescription), Paris),
            _ => throw new ArgumentException("Invalid location")
        };
    }

    public static DateTime GetAlertTime(DateTime appointment, AlertLevel alertLevel)
    {
        return alertLevel switch
        {
            AlertLevel.Early => appointment.AddHours(-24),
            AlertLevel.Standard => appointment.AddHours(-1).AddMinutes(-45),
            AlertLevel.Late => appointment.AddMinutes(-30),
            _ => throw new ArgumentException("Invalid alert level")
        };
    }

    public static bool HasDaylightSavingChanged(DateTime dt, Location location)
    {
        return location switch
        {
            Location.NewYork => !(NY.IsDaylightSavingTime(dt).Equals(NY.IsDaylightSavingTime(dt.AddDays(-7)))),
            Location.London => !(London.IsDaylightSavingTime(dt).Equals(London.IsDaylightSavingTime(dt.AddDays(-7)))),
            Location.Paris => !(Paris.IsDaylightSavingTime(dt).Equals(Paris.IsDaylightSavingTime(dt.AddDays(-7)))),
            _ => throw new ArgumentException("Invalid location")
        };
    }

    public static DateTime NormalizeDateTime(string dtStr, Location location)
    {
        try
        {
            return location switch
            {
                Location.NewYork => DateTime.Parse(dtStr, CultureInfo.CreateSpecificCulture("en-US")),
                Location.London => DateTime.Parse(dtStr, CultureInfo.CreateSpecificCulture("en-GB")),
                Location.Paris => DateTime.Parse(dtStr, CultureInfo.CreateSpecificCulture("fr-FR")),
                _ => DateTime.MinValue
            };
        }
        catch
        {
            return DateTime.MinValue;
        }
    }
}

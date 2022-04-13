public class RemoteControlCar
{
    public RemoteControlCar()
    {
        CurrentSponsor = "";
        Telemetry = new CarTelemetry(this);
    }
    public enum SpeedUnits
    {
        MetersPerSecond,
        CentimetersPerSecond
    }

    public struct Speed
    {
        public decimal Amount { get; }
        public SpeedUnits SpeedUnits { get; }

        public Speed(decimal amount, SpeedUnits speedUnits)
        {
            Amount = amount;
            SpeedUnits = speedUnits;
        }

        public override string ToString()
        {
            return SpeedUnits switch
            {
                SpeedUnits.CentimetersPerSecond => $"{Amount} centimeters per second",
                _ => $"{Amount} meters per second"
            };
        }
    }

    public string CurrentSponsor { get; private set; }
    public ITelemetry Telemetry { get; private set; }

    public Speed currentSpeed;

    public string GetSpeed() => currentSpeed.ToString();

    public void SetSponsor(string sponsorName) => CurrentSponsor = sponsorName;

    public void SetSpeed(Speed speed) => currentSpeed = speed;

    public interface ITelemetry
    {
        public void Calibrate();
        public bool SelfTest();
        public void ShowSponsor(string sponsorName);
        public void SetSpeed(decimal amount, string unitsString);
    }

    public class CarTelemetry : ITelemetry
    {
        public CarTelemetry(RemoteControlCar car) => Car = car;

        public RemoteControlCar Car { get; }
        public string unitsString { get; set; }
        public SpeedUnits SpeedUnits { get; set; }

        public void Calibrate(){}

        public bool SelfTest() =>true;
        
        public void ShowSponsor(string sponsorName) => Car.SetSponsor(sponsorName);

        public void SetSpeed(decimal amount, string unitsString="")
        {
            SpeedUnits speedUnits = unitsString switch
            {
                "cps" => SpeedUnits.CentimetersPerSecond,
                _ => SpeedUnits.MetersPerSecond
            };
            Car.SetSpeed(new Speed(amount, speedUnits));
        }
    }
}



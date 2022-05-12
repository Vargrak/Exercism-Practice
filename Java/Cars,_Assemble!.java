public class CarsAssemble {


    static final double carsPerIncrement = 221;

    public double productionRatePerHour(int speed) 
    {
        switch (speed) {
            case 1: case 2: case 3: case 4:
               return (carsPerIncrement * speed);
            case 5: case 6: case 7: case 8:
               return (carsPerIncrement * speed) * 0.9;
            case 9:
                return (carsPerIncrement * speed) * 0.8;
            case 10:
                return (carsPerIncrement * speed) * 0.77;
            default:
                return 0;
        }
    }

    public int workingItemsPerMinute(int speed) 
    {
        return (int) productionRatePerHour(speed) / 60;
    }
}

public class LogLevels {
    
    public static String message(String logLine) 
    {
        String[] split = logLine.split(":");
        return split[1].trim();
    }

    public static String logLevel(String logLine) 
    {
        String[] split = logLine.split(":");
        return split[0].replaceAll("[\\p{Ps}\\p{Pe}]", "").trim().toLowerCase();
    }

    public static String reformat(String logLine) 
    {
        String[] split = logLine.split(":");
        StringBuilder sb = new StringBuilder();
        sb.append(split[1].trim());
        sb.append(" (");
        sb.append(split[0].replaceAll("[\\p{Ps}\\p{Pe}]", "").trim().toLowerCase());
        sb.append(")");
        return sb.toString();
    }
}

using System;

enum LogLevel
{
    Trace,
    Debug,
    Info,
    Warning,
    Error,
    Fatal,
    Unknown
}

static class LogLine
{
    public static LogLevel ParseLogLevel(string logLine)
    {
        string temp = logLine.Split(':')[0].Trim('[', ']', '<', '>');

        return temp switch
        {
            "TRC" => LogLevel.Trace,
            "DBG" => LogLevel.Debug,
            "INF" => LogLevel.Info,
            "WRN" => LogLevel.Warning,
            "ERR" => LogLevel.Error,
            "FTL" => LogLevel.Fatal,
            _ => LogLevel.Unknown,
        };
    }

    public static string OutputForShortLog(LogLevel logLevel, string message)
    {
        return logLevel switch
        {
            LogLevel.Trace => $"1:{message}",
            LogLevel.Debug => $"2:{message}",
            LogLevel.Info => $"4:{message}",
            LogLevel.Warning => $"5:{message}",
            LogLevel.Error => $"6:{message}",
            LogLevel.Fatal => $"42:{message}",
            _ => $"0:{message}",
        };
    }
}
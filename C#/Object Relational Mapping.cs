using System;

public class Orm : IDisposable
{
    public void Dispose() => database.Dispose();

    private Database database;

    public Orm(Database database) => this.database = database;

    public void Begin()
    {
        try
        {
            database.BeginTransaction();
        }
        catch
        {
            Dispose();
        }
    }

    public void Write(string data)
    {
        try
        {
            database.Write(data);
        }
        catch
        {
            Dispose();
        }
    }

    public void Commit()
    {
        try
        {
            database.EndTransaction();
        }
        catch
        {
            Dispose();
        }
    }
}

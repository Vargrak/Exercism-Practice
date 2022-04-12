using System;
using System.Collections.Generic;

public struct Coord
{
    public Coord(ushort x, ushort y)
    {
        X = x;
        Y = y;
    }

    public ushort X { get; }
    public ushort Y { get; }
}

public struct Plot
{
    public Coord Coord1;
    public Coord Coord2;
    public Coord Coord3;
    public Coord Coord4;

    public Plot(Coord coord1, Coord coord2, Coord coord3, Coord coord4)
    {
        Coord1 = coord1;
        Coord2 = coord2;
        Coord3 = coord3;
        Coord4 = coord4;
    }

    public bool Equals(Plot other)
    {
        return Coord1.Equals(other.Coord1) && Coord2.Equals(other.Coord2) && Coord3.Equals(other.Coord3) && Coord4.Equals(other.Coord4);
    }
}

public class ClaimsHandler
{
    List<Plot> PlotsList = new List<Plot>();

    public void StakeClaim(Plot plot) => PlotsList.Add(plot);

    public bool IsClaimStaked(Plot plot) => PlotsList.Contains(plot);

    public bool IsLastClaim(Plot plot) => plot.Equals(PlotsList[PlotsList.Count - 1]);

    public Plot GetClaimWithLongestSide()
    {
        Plot longestSidePlot = PlotsList[0];
        foreach (Plot plot in PlotsList)
        {
            if (plot.Coord1.X > longestSidePlot.Coord1.X || plot.Coord1.Y > longestSidePlot.Coord1.Y ||
                plot.Coord2.X > longestSidePlot.Coord2.X || plot.Coord2.Y > longestSidePlot.Coord2.Y ||
                plot.Coord3.X > longestSidePlot.Coord3.X || plot.Coord3.Y > longestSidePlot.Coord3.Y ||
                plot.Coord4.X > longestSidePlot.Coord4.X || plot.Coord4.Y > longestSidePlot.Coord4.Y)
            {
                longestSidePlot = plot;
            }       
        }
        return longestSidePlot;
    }
}

using System;
namespace Day2;
public class Day2
{
    static void Report()
    {
        Console.WriteLine($"{tracks.Count}");
    }
    static void Report(string id) {
        int i = tracks.IndexOf(id);
        if (i >= 0) Console.WriteLine($"{id}:{speeds[i]} km");
        else Console.WriteLine($"{id} not found");
    }
}
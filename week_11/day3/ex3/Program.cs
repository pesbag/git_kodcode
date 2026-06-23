using System;
namespace Day3;
class Day3
{
    enum TrackStatus { Active, Lost, Intercepted }
    static void Main()
    {
        TrackStatus st = TrackStatus.Active;
        Console.WriteLine(st);
        if(st==TrackStatus.Active)
            Console.WriteLine("Track is Active");
    }
}
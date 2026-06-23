using System;
namespace Day3;
class Day3
{
    static void Main()
    {
        double? speed = null;
        Console.WriteLine(speed.HasValue);
        Console.WriteLine(speed ?? -1);
        speed = 412.5;
        if(speed.HasValue)
            Console.WriteLine(speed.Value);


    }
}
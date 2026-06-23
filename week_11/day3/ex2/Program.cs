using System;
namespace day3;
class ex2
{
    static bool FindSpeed(string id, out double speed)
    {
        speed = 0;
        if(id=="TR-1")
        { speed = 420.5;return true;}
        return false;
    }
    static void Main() {
        //double s = 0.0;
    if(FindSpeed("TR-1",out double s))
            Console.WriteLine($"found{s}");
     else
            Console.WriteLine("not found");
            }
}
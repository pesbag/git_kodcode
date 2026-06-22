using System;
namespace Day2;
class ex1
{
    static void Main(){
        int[] sectorIds = new int[3];
        sectorIds[0] = 10;
        sectorIds[1] = 20;
        sectorIds[2] = 30;
        List<double> speeds = new List<double>();
        speeds.Add(412.5);
        speeds.Add(95.0);
        speeds.Remove(95.0);
        Console.WriteLine(speeds.Count);
      }
}
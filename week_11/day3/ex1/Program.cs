using System;
namespace Day3;
class excersie() {
        static void TryDouble(int n)
        { n = n * 2; }
        static void AddOne(List<int> x)
        { x.Add(1); }
            
    static void Main()
    {
        int x = 10;
        TryDouble(x);
        Console.WriteLine(x);
        List<int> list = new List<int>();
        AddOne(list);
        Console.WriteLine(list.Count);
    }
}
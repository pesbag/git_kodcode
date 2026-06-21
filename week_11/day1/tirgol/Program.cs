using System;
namespace Demo;
class Tirgol
{
    static void Main()
    {
        string sentence = "Error converting";
        Console.WriteLine("Please enter a speed");
        string s = Console.ReadLine();
        if (double.TryParse(s, out double speed))
        {
            if (speed <80)
                   sentence = "slow";
            else if (speed >= 80 && speed <= 120)
                sentence = "cruise";
            else
                sentence = "fast";
            Console.WriteLine($"The speed is {speed} and the sentence is {sentence}");
        }
        else
            Console.WriteLine(sentence);
    }
}
using System;
using System.Linq;
namespace Demo;
class Radar
{
    static string cutter(string s) {
        string newString = "";
        int prefix = 0;
        int suffix = s.Length - 1;
        while (prefix < suffix && char.IsWhiteSpace(s[prefix]))
            prefix += 1;
        while (prefix < suffix && char.IsWhiteSpace(s[suffix]))
            suffix -= 1;
        newString = s.Substring(prefix, suffix - prefix + 1);
        return newString;
    }
    static void Main()
    {
        string[] statusArr = {"cruising", "turning", "stopped","accelerating"};
        Console.WriteLine("Please enter the radar data:");
        Console.WriteLine("Please enter an UNIQUE integer Track ID");
        bool isInteger = false;
        int TrackId=0;
        double speed=0;
        double head = 0;
        string status = "";
        string category = "";
        while (!isInteger)
        {
            string numberForObj = Console.ReadLine();
            string new_number =cutter(numberForObj);
            if (int.TryParse(new_number, out TrackId))
                isInteger = true;
            else
                Console.WriteLine("Error, the input TrackId is not a valid integer. Please try again");
        }

        isInteger = false;
        Console.WriteLine("Please enter the vehicle Speed (in double)");
        while (!isInteger)
        {
            string speedMoving = Console.ReadLine();
            string newSpeed = cutter(speedMoving);
            if (double.TryParse(newSpeed, out speed))
            {
                if (speed > 0)
                {
                    isInteger = true;
                }
                else Console.WriteLine("Error, speed should be positive! please try again");
            }
            else
                Console.WriteLine("Error, the input Speed is not a valid double. Please try again");
        }

        isInteger = false;
        Console.WriteLine("Please enter the vehicle Heading (in degrees, should be between 0 to 360)");
        while (!isInteger)
        {
            string headMoving = Console.ReadLine();
            string newHeadMoving = cutter(headMoving);
            if (double.TryParse(newHeadMoving, out head))
            {
                if (head > 0 && head <=359)
                {
                    isInteger = true;
                }
                else Console.WriteLine("Error, head should be between 0 to 360, please try again");
            }
            else
                Console.WriteLine("Error, the input speed is not a valid double. Please try again");
        }

        isInteger = false;
        Console.WriteLine("Please enter the vehicle status it should be one of the following statment:" +
            "\"cruising\", \"turning\", \"stopped\",\"accelerating\"");
        while (!isInteger)
        {
            string movingStatus = Console.ReadLine();
            status = cutter(movingStatus);
            if (statusArr.Contains(status))
                isInteger = true;
            else
                Console.WriteLine("Error, the input of status vehicle is not a valid. Please try again");
        }
        if (speed < 70)
            category = "low";
        else if (speed < 130)
            category = "medium";
        else if (speed < 200)
            category = "high";
        else category = "fast";

        Console.WriteLine("=== Track Report ===");
        Console.WriteLine($"Track ID: {TrackId}");
        Console.WriteLine($"Speed: {speed} km/h ({category})");
        Console.WriteLine($"Heading: {head} degrees");
        Console.WriteLine($"Status: {status}");
        Console.WriteLine($"Division Demo 1: 90/30= {90/30}(int)| {90.0/30.0:F1}(double)");
        Console.WriteLine($"Division Demo 2: 250/60= {250/60}(int)| {250.0/60.0}(double)");
        
    }


}
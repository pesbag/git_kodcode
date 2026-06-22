using System;
using System.Linq;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace fleetEx;

class Fleet()
{
    static List<int> idLst = new List<int>();
    static List<int> speedLst = new List<int>();
    static List<int> headLst = new List<int>();
    static string cutter(string s)
    {
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
    static int getData(string dataType)
    {
        Console.WriteLine($"Please enter {dataType} of track");
        bool isLegal = false;
        int legalData = 0;
        bool heading = false;
        while (!isLegal)
        {
            string id = Console.ReadLine();
            string cleandata = cutter(id);
            if (int.TryParse(cleandata, out legalData))
            {
                
                heading = isHeading(dataType, legalData);
                if (heading)
                    continue;
                else if (legalData < 0)
                    Console.WriteLine($"Error the {dataType} should be positive, please try again");
                else
                    isLegal = true;
            }
            else
                Console.WriteLine($"Error {dataType} shold not contain any characters, please try again");
        }
        return legalData;
    }
    static bool isHeading(string s,int data)
    {
        if (s == "heading"){
            if (data > 359 || data < 0)
            {
                Console.WriteLine("Error heading should be between 0 to 360");
                return true;
            }
        }
        return false;
    }
    static void add(int id, int speed, int head)
    {
        idLst.Add(id);
        speedLst.Add(speed);
        headLst.Add(head);
        Console.WriteLine("Add items successfully");
    }

    static void remove_by_id(List<int> lst,int id) {
        int index = lst.IndexOf(id);
        if (index == -1)
        {
            Console.WriteLine("Error: Track ID not found.");
            return;
        }
        idLst.RemoveAt(index);
        speedLst.RemoveAt(index);
        headLst.RemoveAt(index);
        Console.WriteLine("Removed successfully");
    }
    //static string find_by_id(List<int> lst,int id){
    //    int exists = lst.IndexOf(id);
    //    if (index == -1) ;
    //    }
    static void Main()
    {
        string[] commandArr = {"add","remove","find","list","filter","summarize","stop"};
        int legalId;
        int legalSpeed;
        int legalHead;
        bool loopContinue = true;
        string command = "";
        string cleanCommand = "";
        Console.WriteLine("Please enter one from the following commands: \"add\",\"remove\",\"find\",\"list\",\"filter\",\"summarize\",\"stop\"");
        while (loopContinue){
            command = Console.ReadLine();
            cleanCommand = cutter(command);
            if (commandArr.Contains(cleanCommand))
            {
                if (cleanCommand == "stop")
                    loopContinue = false;

                else if (cleanCommand == "list")
                {
                    if(idLst.Count==0)
                        Console.WriteLine("Error: list is empty cannot print it");
                    for (int i = 0; i < idLst.Count; i++)
                    {
                        Console.WriteLine($"The list of tracks: [id:{idLst[i]} speed:{speedLst[i]} head:{headLst[i]}]");
                    }
                }
                else
                {
                    legalId = getData("id");
                    if (cleanCommand == "add")
                    {
                        legalSpeed = getData("speed");
                        legalHead = getData("heading");
                        add(legalId, legalSpeed, legalHead);
                        continue;

                    }
                    if (cleanCommand == "remove")
                    {
                        remove_by_id(idLst,legalId);
                        continue;
                    }
                    //if (cleanCommand == "find")
                    //{
                    //    find_by_id(legalId);
                    //    continue;
                    //}
                    //Console.WriteLine($"The id is: {legalId}");
                    //Console.WriteLine($"The speed is {legalSpeed}");
                    //Console.WriteLine($"The head is: {legalHead}");
                }
            }
            else Console.WriteLine("Error! command not found, please try again");
        }
    }
}
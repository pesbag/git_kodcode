using System;
using System.Linq;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace fleetEx;

class Fleet()
{
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
    static void add(List<int> lst, int data)
    { 
        lst.Add(data);
        Console.WriteLine("Add items successfully");
    }

    static void remove_by_id(List<int> idLst,List<int> speedLst,List<int> headLst, int id) {
        int index = idLst.IndexOf(id);
        if (index == -1)
        {
            Console.WriteLine("Error: Track ID not found");
            return;
        }
        idLst.RemoveAt(index);
        speedLst.RemoveAt(index);
        headLst.RemoveAt(index);
        Console.WriteLine("Removed successfully");
    }
    static string find_by_id(List<int> idLst, List<int> speedLst, List<int> headLst, int id)
    {
        int exists = idLst.IndexOf(id);
        if (exists == -1)
        {
            Console.WriteLine("Error: ID was not found");
            return "";
        }
        string obj = $"The list of tracks: [id:{idLst[exists]} speed:{speedLst[exists]} head:{headLst[exists]}]";
        return obj;
    }
    static double calcAvgSpeed(List<int> speedLst) {
        double sum = 0;
        if (speedLst.Count == 0)
            return 0;
        for(int i = 0; i < speedLst.Count; i++)
        {
            sum += speedLst[i];
        } 
        return sum / (double)speedLst.Count();
    }

    static  List<string>  filterTrack(List<int> idLst, List<int> speedLst, List<int> headLst,int threshold)
    {
        List<string> result = new List<string>();
        for(int i = 0; i < idLst.Count; i++)
        {
            if (speedLst[i]>threshold) {
                result.Add($"[id:{idLst[i]} speed:{speedLst[i]} head:{headLst[i]}]");
            }
        }
        return result;
    }
    static string findFastest(List<int> idLst,List<int> speedLst,List<int> headLst)
    {
        int maxSpeed = -1;
        foreach (int s in speedLst)
        {
            if (s > maxSpeed)
                maxSpeed = s;
        }
        int index = speedLst.IndexOf(maxSpeed);
        int fastestId = idLst[index];
        string result = find_by_id(idLst, speedLst, headLst, fastestId);
        return result;
    }
    static void Main()
    {
        List<int> idLst = new List<int>();
        List<int> speedLst = new List<int>();
        List<int> headLst = new List<int>();
        string[] commandArr = {"add","remove","find","list","filter","summarize","stop"};
        int legalId;
        int legalSpeed;
        int legalHead;
        bool duplicate = false;
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
                        Console.WriteLine($"[id:{idLst[i]} speed:{speedLst[i]} head:{headLst[i]}]");
                    }
                }
                else if (cleanCommand == "summarize")
                {
                    Console.WriteLine($"total track: {idLst.Count}, average speed {calcAvgSpeed(speedLst)}, fastest track{findFastest(idLst, speedLst, headLst)})");
                }
                else
                {
                    legalId = getData("id");
                    if (cleanCommand == "add")
                        duplicate = false;
                    {
                        if (idLst.Count > 0)
                        {
                            foreach(int n in idLst)
                            {
                                if (legalId == n)
                                {
                                    Console.WriteLine("Error duplicate key id found, please try again");
                                    duplicate = true;
                                }
                            }
                        }
                        if (duplicate)
                            continue;
                        legalSpeed = getData("speed");
                        legalHead = getData("heading");
                        add(idLst,legalId);
                        add(speedLst, legalSpeed);
                        add(headLst, legalHead);
                        continue;

                    }
                    if (cleanCommand == "remove")
                    {
                        remove_by_id(idLst,speedLst,headLst,legalId);
                        continue;
                    }
                    if (cleanCommand == "find")
                    {
                        string result=find_by_id(idLst, speedLst, headLst,legalId);
                        Console.WriteLine(result);
                        continue;
                    }
                    if (cleanCommand == "filter")
                    {
                        List<string> result =filterTrack(idLst, speedLst, headLst, 85);
                        Console.WriteLine(result);
                    }
                }
            }
            else Console.WriteLine("Error! command not found, please try again");
        }
    }
}
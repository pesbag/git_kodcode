using System;
namespace Day3;

enum enumClassification { Friendly, Hostile, Unidentified }
enum enumCommand { add, update, show, exit }
class Transmision
{

    static void getTrans(List<int> idLst, List<string> classificationLst, List<double?> signalLst)
    {
        bool validItems = true;
        int id;
        string classification;
        double? strength;
        id = getId(idLst);
        strength = getStrength();
        classification = getClassification();
        idLst.Add(id);
        classificationLst.Add(classification);
        signalLst.Add(strength);
        //Console.WriteLine($"id is {id}");
        //Console.WriteLine($"strength is {strength}");
        //Console.WriteLine($"classification is {classification}");


    }

    static string getClassification()
    {
        string classification;
        string newClassification = "";
        bool isValid = false;
        Console.WriteLine("Please enter calssifiction 'Friendly', 'Hostile', 'Unidentified'");
        while (!isValid)
        {
            bool found = false;
            classification = Console.ReadLine();
            newClassification = classification.Trim().ToLower();
            foreach (enumClassification c in Enum.GetValues(typeof(enumClassification)))
            {
                if (c.ToString().ToLower() == newClassification)
                {
                    found = true;
                }
            }
            if (found)
                isValid = true;
            else
                Console.WriteLine("Error unvalid classification please try again");
        }
        return newClassification;
    }
    static double? getStrength()
    {
        bool isValid = false;
        double strength = 0.0;
        string strengthInput;
        Console.WriteLine("please enter strength");

        while (!isValid)
        {
            strengthInput = Console.ReadLine();
            if (string.IsNullOrEmpty(strengthInput))
                return null;
            if (double.TryParse(strengthInput, out strength))
            {
                if (strength <= 0)
                {
                    Console.WriteLine("Error: strength should be positive");
                }
                else
                    isValid = true;
            }
            else
                Console.WriteLine("Error: strength should not contain any characters");
        }
        return strength;
    }

    static void showTransmmision(List<int> idLst, List<string> classificationLst, List<double?> signalLst)
    {
        if (idLst.Count == 0)
        {
            Console.WriteLine("Error transmition list is empty, cannot print it");
        }
        else
        {
            for (int i = 0; i < idLst.Count; i++)
            {
                Console.WriteLine($"[id:{idLst[i]},classification:{classificationLst[i]},signal strength: {signalLst[i]}]");
            }
        }
    }

        static int getId(List<int> idLst)
        {
            string idInput;
            int validId = 0;
            bool isValidId = false;
            Console.WriteLine("Please enter transmission id");
            while (!isValidId)
            {
                idInput = Console.ReadLine();
                if (validateId(idInput, idLst, out validId))
                {
                    isValidId = true;
                }
            }
            return validId;
        }

        //static bool validateTrans(double transmission) { }

        static bool validateId(string id, List<int> idLst, out int validId)
        {
            if (int.TryParse(id, out validId))
            {
                if (validId <= 0)
                {
                    Console.WriteLine("Error: id should be positive");
                    return false;
                }
                else if (!idExists(validId, idLst))
                {
                    return false;
                }
                else return true;
            }
            else { Console.WriteLine("Error: id should not contain any characters"); return false; }
        }
        static bool idExists(int id, List<int> lst)
        {
            int index = lst.IndexOf(id);
            if (index != -1)
            {
                Console.WriteLine("Error: duplicate id found, please try again");
                return false;
            }
            return true;
        }
        static void updateTransById() { }
        static void readTrans() { }
        static void exit() { }
        static string showMenu()
        {
            bool validCommand = true;
            bool found = false;
            string cleanCommand = "";
            while (validCommand)
            {
                Console.WriteLine("Please chose command from the next options:" +
                    "'add', 'update', 'show', 'exit'");
                string command = Console.ReadLine();
                cleanCommand = command.Trim().ToLower();
                foreach (enumCommand c in Enum.GetValues(typeof(enumCommand)))
                {
                    if (cleanCommand == c.ToString())
                    {
                        found = true;
                        break;
                    }
                }
                if (found == true)
                    validCommand = false;
                else
                    Console.WriteLine("Error, unvalid input, please try again");
            }
            return cleanCommand;
        }
        static void Main()
        {
            List<int> idLst = new List<int>();
            List<string> classificationLst = new List<string>();
            List<double?> signalLst = new List<double?>();
            bool isValid = true;
            string chose;
            while (isValid)
            {
                chose = showMenu();
                switch (chose)
                {
                    case "add":
                        getTrans(idLst, classificationLst, signalLst);
                        break;
                    case "show":
                        showTransmmision(idLst, classificationLst, signalLst);
                        break;
                    case "exit":
                        isValid = false;
                        Console.WriteLine("exit from the program...");
                        break;
                }

            }
        }
}



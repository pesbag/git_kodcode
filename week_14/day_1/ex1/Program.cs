using System;
using System.Text.Json;
using System.Xml.Linq;
using static System.Net.Mime.MediaTypeNames;
public class MissingInputException : Exception
{
    public MissingInputException(string message) : base(message) { }
}
public class MissingArgumentException : Exception
{
    public MissingArgumentException(string message) : base(message) { }
}
public class InvalidPriority : Exception
{
    public InvalidPriority(string message):base(message) {}
}
public class InvalidID : Exception
{
    public InvalidID(string message) : base(message) { }
}
public class MissingJsonFile : Exception
{
    public MissingJsonFile(string message) : base(message) {}
}


public class lineParser
{
    const int numberOfElemntInRaw=3;
    enum statusEnum { COMMS, IMAGERY, SIGNAL };
    public createReportObj lineParse(string rawLine)
    {
        string[] data = rawLine.Split(" ", StringSplitOptions.RemoveEmptyEntries);
        if (data.Length != numberOfElemntInRaw)
            throw new MissingArgumentException("Error missing argument in row");
        if (!int.TryParse(data[0], out int id) || id < 0)
            throw new InvalidID("Error invalid id enter: int should be  positiveinteger");
        if (!int.TryParse(data[2], out int priority) || priority < 0)
            throw new InvalidPriority("Error invalid priority, should be positive integer");
        //if(statusEnum.COMMS.ToString()!=)
        return new createReportObj(id, data[1],priority);
    }
}
public class openFile 
{
    lineParser _parser;
    createReportObj reportObj;
    convertToJson _convert;
    public string Path { get; }
    public string Output { get; }
    public openFile(string path,string output) {
        if (string.IsNullOrWhiteSpace(path)|| string.IsNullOrWhiteSpace(output))
        {
            throw new MissingArgumentException("Error missing path of input or  output");
        }
        Path = path;
        Output = output;
    }
    public void extractLines() 
    {
        int lineCounter = 1;
        try
        {
            using StreamReader reader = new StreamReader(Path);
            using var writer = new StreamWriter(Output);
            string? line;
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine($"line {lineCounter} was readed");
                lineCounter += 1;
                try {
                    reportObj = _parser.lineParse(line);
                    Console.WriteLine(line);
                    string converted = _convert.StringToStringLIkeJson(reportObj);
                    string jsonLine = JsonSerializer.Serialize(converted);
                    writer.WriteLine(jsonLine);
                }
                catch (Exception ex) {
                    Console.WriteLine(ex.Message);
                }
            }
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine($"Error file int path {Path} was not found");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"generic error: {ex.Message}");
        }
        finally
        {
            Console.WriteLine("Finish to order the lines");
        }
    }
}
public class convertToJson
{
    public string StringToStringLIkeJson(createReportObj report)
    {
        var reportObj = new
        {
            id = report.Id,
            status=report.Category,
            priorty=report.Priority
        };
        string jsonResult=JsonSerializer.Serialize(reportObj);
        Console.WriteLine($"json created successfully: {jsonResult}");
        return jsonResult;
    }
    public void writeToFile(string result) { }
}
public class createReportObj
{
    public int Id { get; }
    public string Category { get; }
    public int Priority { get; }
    public createReportObj(int id, string category, int priority) 
    {
        Id = id;
        Category = category;
        Priority = priority;
    }      
}
class Program
{
    public static void Main() 
    {
        try
        {
            openFile file = new openFile("w4d1_field_reports_input.txt","output.json");
            file.extractLines();
        }
        catch (MissingArgumentException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}
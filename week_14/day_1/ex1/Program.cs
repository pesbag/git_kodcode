using System;
using System.Text.Json;
using System.Xml.Linq;
using static System.Net.Mime.MediaTypeNames;
public class MissingInputException : Exception
{
    public MissingInputException(string message) : base(message) { }
}
public class InvalidCategory : Exception
{
    public InvalidCategory(string message) : base(message) { }
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
public class JsonFileException : Exception
{
    public JsonFileException(string message) : base(message) { }
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
        if (statusEnum.COMMS.ToString() != data[1] && statusEnum.SIGNAL.ToString() != data[1] && statusEnum.IMAGERY.ToString() != data[1])
            throw new InvalidCategory("Error invalid category. should be SIGNAL,COMMS,IMAGERY");
            return new createReportObj(id, data[1],priority);
    }
}
public class fileProcesor 
{
    lineParser _parser;
    createReportObj reportObj;
    convertToJson _convert;
    public string Path { get; }
    public string OutputPath { get; }
    public fileProcesor(string path,string outputpath) {
        if (string.IsNullOrWhiteSpace(path)|| string.IsNullOrWhiteSpace(outputpath))
        {
            throw new MissingArgumentException("Error missing path of input or  output");
        }
        Path = path;
        OutputPath = outputpath;
        _parser = new lineParser();
        _convert = new convertToJson();
    }
    public void extractLines() 
    {
        int lineCounter = 0;
        int exceptionCounter = 0;
        try
        {
            using StreamReader reader = new StreamReader(Path);
            using StreamWriter writer = new StreamWriter(OutputPath);
            string? line;
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine($"line {lineCounter} was readed");
                lineCounter += 1;
                try {
                    reportObj = _parser.lineParse(line);
                    Console.WriteLine(line);
                    string converted = _convert.StringToJson(reportObj.Id,reportObj.Category,reportObj.Priority);
                    writer.WriteLine(converted);
                }
                catch (MissingArgumentException ex) {
                    exceptionCounter += 1;
                    Console.WriteLine(ex.Message);
                }
                catch (InvalidID ex) {
                    exceptionCounter += 1;
                    Console.WriteLine(ex.Message);
                }
                catch (InvalidPriority ex) {
                    exceptionCounter += 1;
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
            Console.WriteLine($"Finish to order the lines. total lines={lineCounter},exception={exceptionCounter},accepted={lineCounter-exceptionCounter}");
        }
    }
    public void reloadAndPrintJson()
    {
        try
        {
            if (!File.Exists(OutputPath))
            {
                throw new JsonFileException("Error json file not found");
            }
            using StreamReader reader = new StreamReader(OutputPath);
            string? line;
            while ((line = reader.ReadLine()) != null) 
            {
                createReportObj? report = JsonSerializer.Deserialize<createReportObj>(line);
                if(report!=null)
                    Console.WriteLine($"Reloaded Object - ID: {report.Id}, Status: {report.Category}, Priority: {report.Priority}");
            }
        }
        catch (JsonFileException ex) { Console.WriteLine(ex.Message); }
        catch (Exception ex) { Console.WriteLine($"Reload Error: {ex.Message}"); }
    }
}
public class convertToJson
{
    public string StringToJson(int id,  string category, int priority)
    {
        var reportObj = new
        {
            Id = id,
            status=category,
            priorty=priority
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
            Console.WriteLine("run the good txt file");
            fileProcesor process = new fileProcesor("w4d1_field_reports_input.txt", "output.json");
            process.extractLines();
            Console.WriteLine("run the corrupt json file");
            fileProcesor corruptProcessor = new fileProcesor("field_reports_input.txt", "w4d1_reports_corrupted.json");
            corruptProcessor.reloadAndPrintJson();
        }
        catch (MissingArgumentException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}
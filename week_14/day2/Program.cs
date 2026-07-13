using System;
using System.Text.Json;
namespace day2;
//public class 
public class Report
{
    public int Id { init; get; }
    public string? Category { init; get; }
    public int Priority { init; get; }
    public string? Zone { init; get; }
    public int SignalStrength { init; get; }
    public string? Shift { init; get; }
    public Report() { }
    public Report(int  id, string category,int priority,string zone,int siganl,string shift) {
        Id = id;
        Category = category;
        Priority = priority;
        Zone = zone;
        SignalStrength = siganl;
        Shift = shift;

    }
    public override string ToString()
    {
        return $"Id: {Id}, Category: {Category}, Priority: {Priority}, Zone: {Zone}, Signal: {SignalStrength}, Shift: {Shift}";
    }
}
public class OpenFile
{
    public List<Report> loadFile(string path)
    {
        string allLines = "";
        try
        {
            allLines= File.ReadAllText(path);
            List<Report> reportObj = JsonSerializer.Deserialize<List<Report>>(allLines) ?? [];
            return reportObj;
        }
        catch (FileNotFoundException ex)
        {
            Console.WriteLine("Error to found th file: ",ex.Message);
        }
        return new List<Report>();
    }
}
//public class ConvertToObj { }
public class ClassA
{
    public int totalReports(List<Report> reports)
    {
        return reports.Count();
    }
    public List<int> idOfSignal(List<Report> reports)
    {
        return reports.Where(r => r.Category == "Signal").Select(r => r.Id).ToList();
    }
    public List<int> idOfHigherPriority(List<Report> reports)
    {
        return reports.Where(r => r.Priority >= 4).Select(r=>r.Id).ToList();
    }
    public List<int> idListOfNightNorth(List<Report> reports)
    {
        return reports.Where(r=>r.Shift=="Night" && r.Zone=="North").Select(r=>r.Id).ToList();
    }
    public List<(int Id, int Priority)> idAndPriority(List<Report> reports)
    {

        return reports.Where(r => r.Category == "COMMS")
            .Select(r => (r.Id, r.Priority )).ToList();

    }
    public List<int> signalrange(List<Report> reports) 
    {
        return reports.Where(r => r.SignalStrength >=70 && r.SignalStrength <= 90).Select(r => r.Id).ToList();
    }
    public List<int> idNotInWest(List<Report> reports)
    {
        return reports.Where(r => r.Zone != "West").Select(r => r.Id).ToList();
    }
}
public class ClassB
{
    public List<int> HighestPriority(List<Report> reports) {
        return reports.OrderBy(r => r.Priority).Select(r=>r.Id).ToList();
    }
    public List<int> orderByZoneAndPriority(List<Report> reports)
    {
        return reports.OrderBy(r => r.Priority).ThenByDescending(r => r.Priority).Select(r => r.Id).ToList();
    }
    public List<int> StrongestSignal(List<Report> reports)
    {
        return reports.OrderBy(r => r.SignalStrength).Select(r => r.Id).Take(3).ToList();
    }
    public List<int> LowestSignal(List<Report> reports)
    {
        return reports.OrderByDescending(r => r.SignalStrength).Select(r => r.Id).Take(2).ToList();
    }
    public List<int> skipped5Hiest(List<Report> reports){
        var start = reports.OrderByDescending(r => r.Priority).Select(r=>r.Id).Skip(5).ToList();
        return start;
    }
    public List<int> idImagery(List<Report> reports)
    {
        return reports.OrderBy(r=>r.SignalStrength).Where(r=>r.Category=="IMAGERY").Select(r=>r.Id).ToList();
    }
}
public class ClassC
{
    public int priority5(List<Report> reports)
    {
        return reports.Count(r => r.Priority == 5);
    }
    public double avgSignal(List<Report> reports)
    {
        return reports.Average(r => r.SignalStrength);
    }
    public int strongest(List<Report> reports)
    {
        return reports.Max(r => r.SignalStrength);
    }
    public int weakest(List<Report> reports)
    {
        return reports.Where(r => r.Category == "Signal").Sum(r => r.Priority);
    }
    public double avgPriority(List<Report> reports) {
        return reports.Where(r => r.Zone == "South").Average(r => r.Priority);
    }
    public int distinctZone(List<Report> reports) {
        return reports.Select(r => r.Zone).Distinct().Count();
    }
    public List<string> category(List<Report> reports)
    {
        return reports.Where(r => r.Category != null).Select(r => r.Category!).Distinct().OrderByDescending(x=>x).ToList();
    }
}
public class Program
{
    public static void Main()
    {
        OpenFile file = new OpenFile();
        List<Report> content = file.loadFile("W4D2_reports.json");
        //foreach(Report s in content)
        //{
        //    Console.WriteLine(s.ToString());
        //}
        ClassA a = new ClassA();
        Console.WriteLine($"Part a Q1: {a.totalReports(content)}");
        Console.WriteLine($"Part a Q2: {string.Join(", ", a.idOfSignal(content))}");
        Console.WriteLine($"Part a Q3: {string.Join(", ", a.idOfHigherPriority(content))}");
        Console.WriteLine($"Part a Q4: {string.Join(", ", a.idListOfNightNorth(content))}");
        Console.WriteLine($"Part a Q5: {string.Join(", ", a.idAndPriority(content))}");
        Console.WriteLine($"Part a Q6: {string.Join(", ",a.signalrange(content))}");
        Console.WriteLine($"Part a Q7: {string.Join(", ",a.idNotInWest(content))}");

        ClassB b = new ClassB();
        Console.WriteLine($"Part b Q8 : {string.Join(", ",b.HighestPriority(content))}");
        Console.WriteLine($"Part b Q9 : {string.Join(", ", b.orderByZoneAndPriority(content))}");
        Console.WriteLine($"Part b Q10 : {string.Join(", ", b.StrongestSignal(content))}");
        Console.WriteLine($"Part b Q11 : {string.Join(", ", b.LowestSignal(content))}");
        Console.WriteLine($"Part b Q12 : {string.Join(", ", b.skipped5Hiest(content))}");
        Console.WriteLine($"Part b Q13 : {string.Join(", ", b.idImagery(content))}");

        ClassC c = new ClassC();
        Console.WriteLine($"Part c Q14 : {string.Join(", ", c.priority5(content))}");
        Console.WriteLine($"Part c Q15 : {string.Join(", ", c.avgSignal(content))}");
        Console.WriteLine($"Part c Q16 : {string.Join(", ", c.strongest(content))}");
        Console.WriteLine($"Part c Q17 : {string.Join(", ", c.weakest(content))}");
        Console.WriteLine($"Part c Q18 : {string.Join(", ", c.avgPriority(content))}");
        Console.WriteLine($"Part c Q19 : {string.Join(", ", c.distinctZone(content))}");
        //Console.WriteLine($"Part c Q20 : {string.Join(", ", c.HighestPriority(content))}");
    }
}
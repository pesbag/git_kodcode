using System;
namespace ImageMetaDataManagerWrong;

class ImageMetaDataManager
{
    public int Id { get; set; }
    public double CloudCover { get; set; }
    public string Sensor { get; set; }

    public ImageMetaDataManager(int id,double cloudCover,string sensor) {
        Id = id;
        CloudCover=cloudCover;
        Sensor = sensor;

    }
    public bool IsValid()
    {
        return CloudCover >= 0 && CloudCover <= 100;
    }
    public string Format()
        =>$"Image: {Id} cloud: {CloudCover}";
    public void SaveToFile(string path) 
    {
        System.IO.File.WriteAllText(path, Format());
    }
    public int score() {
        int BasePriority;
        switch (Sensor) {
            case "EO":
                BasePriority = 60;
                break;
            case "SAR":
                BasePriority = 100;
                break;
            case "IR":
                BasePriority = 40;
                break;
            default:
                BasePriority = 0;
                break;
        }
        return BasePriority - (int)CloudCover;
    }
    public static void Main()
    {
        ImageMetaDataManager u = new ImageMetaDataManager(2,45,"EO");
        Console.WriteLine(u.Format());
        Console.WriteLine(u.score());
        ImageMetaDataManager u1 = new ImageMetaDataManager(5, 55, "SAR");
        Console.WriteLine(u.score());
        ImageMetaDataManager u2 = new ImageMetaDataManager(8, 75, "IR");
        Console.WriteLine(u.score());
    }

}
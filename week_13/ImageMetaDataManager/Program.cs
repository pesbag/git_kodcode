using ImageMetaDataManagerright;
using System;
using System.Collections.Generic;
using System.IO;
namespace ImageMetaDataManagerWrong{

    class ImageMetaDataManager
    {
        public int Id { get; set; }
        public double CloudCover { get; set; }
        public string Sensor { get; set; }

        public ImageMetaDataManager(int id, double cloudCover, string sensor)
        {
            Id = id;
            CloudCover = cloudCover;
            Sensor = sensor;

        }
        public bool IsValid()
        {
            return CloudCover >= 0 && CloudCover <= 100;
        }
        public string Format()
            => $"Image: {Id} cloud: {CloudCover}";
        public void SaveToFile(string path)
        {
            System.IO.File.WriteAllText(path, Format());
        }
        public int score()
        {
            int BasePriority;
            switch (Sensor)
            {
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
            ImageMetaDataManager u = new ImageMetaDataManager(2, 45, "EO");
            Console.WriteLine(u.Format());
            Console.WriteLine(u.score());
            ImageMetaDataManager u1 = new ImageMetaDataManager(5, 55, "SAR");
            Console.WriteLine(u1.Format());
            Console.WriteLine(u1.score());
            ImageMetaDataManager u2 = new ImageMetaDataManager(8, 75, "IR");
            Console.WriteLine(u2.score());
        }

    }
}








namespace ImageMetaDataManagerright
{
    public abstract class SatelliteImage
    {
        public int Id { get; set; }
        public double CloudCover { get; set; }
        public abstract string SensorType { get; }
        public abstract int Score();
        public SatelliteImage(int id, double cloudCover)
        {
            if (cloudCover < 0 || cloudCover > 100)
            {
                throw new ArgumentOutOfRangeException("CloudCover must be between 0 and 100");
            }
            Id = id;
            CloudCover = cloudCover;
        }
    }

    public class SARImage : SatelliteImage
    {
        public override string SensorType => "SAR";

        public SARImage(int id, double cloudCover) : base(id, cloudCover) { }

        public override int Score() => 100 - (int)CloudCover;
    }

    public class EOImage : SatelliteImage
    {
        public override string SensorType => "EO";

        public EOImage(int id, double cloudCover) : base(id, cloudCover) { }

        public override int Score() => 60 - (int)CloudCover;
    }

    public class IRImage : SatelliteImage
    {
        public override string SensorType => "IR";

        public IRImage(int id, double cloudCover) : base(id, cloudCover) { }

        public override int Score() => 40 - (int)CloudCover;
    }
    public class ImageFormatter
    {
        public string Format(SatelliteImage image)
        {
            return $"Image {image.Id}: {image.CloudCover}% cloud [{image.SensorType}]";
        }
    }

    public class ImageFileStore
    {
        private readonly ImageFormatter _formatter = new();

        public void SaveToFile(string path, SatelliteImage image)
        {
            string logLine = _formatter.Format(image);
            File.WriteAllText(path, logLine);
        }
    }

    public class Repository<T> where T : SatelliteImage
    {
        private readonly List<T> _items = new();
        public void Add(T item) => _items.Add(item);
        public T Get(int i) => _items[i];
        public IEnumerable<T> GetAll() => _items;
    }
    class Program
    {
        public static void Main()
        {
            Repository<SatelliteImage> repo = new Repository<SatelliteImage>();
            ImageFormatter formatter = new ImageFormatter();
            repo.Add(new SARImage(1, 20));
            repo.Add(new EOImage(2, 10));
            repo.Add(new IRImage(3, 5));
            try
            {
                repo.Add(new SARImage(4, 150));
            }
            catch (ArgumentOutOfRangeException ex)
            {
                Console.WriteLine($"Managed to block invalid construction: {ex.Message}");
            }

            Console.WriteLine("\n--- Processing Images ---");
            int totalScore = 0;
            foreach (var img in repo.GetAll())
            {
                string formatted = formatter.Format(img);
                int score = img.Score();
                totalScore += score;

                Console.WriteLine($"{formatted} , Score: {score}");
            }

            Console.WriteLine($"\nTotal System Score: {totalScore}");
        }
    }
}

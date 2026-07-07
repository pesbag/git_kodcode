using System;
using System.Collections.Generic;
using System.IO;
namespace day3Refactor
{
    public abstract class SatelliteImage
    {
        public int Id { get; init; }
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
    public interface IDatabaseStore
    {
        void Save(SatelliteImage img);
    }
    class MemoryStore : IDatabaseStore
    {
        private readonly List<SatelliteImage> _store = new List<SatelliteImage>();
        public void Save(SatelliteImage img)
        {
            _store.Add(img);
        }
        public int Count => _store.Count;
    }
    class DiskStore: IDatabaseStore
        {
        public void Save(SatelliteImage img) { }
        }
    class ImageProcessor
    {
        private readonly IDatabaseStore _store;
        public ImageProcessor(IDatabaseStore store) => _store = store;
        public void handle(SatelliteImage img) => _store.Save(img);
    }

    class ImagePipeLine
    {
        public SatelliteImage? StateImage;

        private readonly MemoryStore _memStore = new MemoryStore();
        //private readonly 
        public void ShowList(IEnumerable<SatelliteImage> imgs)
        {
            foreach (SatelliteImage i in imgs)
            {
                int scoreCalc = i.Score();
                _memStore.Save(i);
            }
        }
        //public int StoredCount => _memStore.Count;
    }
    //class MemoryStore
    //{
    //    private readonly List<SatelliteImage> _store = new List<SatelliteImage>();
    //    public void Save(SatelliteImage img)
    //    {
    //        _store.Add(img);
    //    }
    //    public int Count
    //        => _store.Count();
    //}

    public class SARImage : SatelliteImage, IScoreable
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
    public class QuickLookImage : SatelliteImage
    {
        public QuickLookImage(int id, double cloudCover) : base(id, cloudCover) { }
        public override string SensorType => "QuiqLookImage";
        public override int Score()
        => 0;
    }
    public class ImageFormatter
    {
        public string Format(SatelliteImage image)
        {
            return $"Image {image.Id}: {image.CloudCover}% cloud {image.SensorType}";
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
    public interface IScoreable
    {
        int Score();
    }
    public interface IRetaskable
    {
        void Retask();
    }
    public interface ICalibrateable
    {
        void CalibrateThermal();
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
            ImagePipeLine pipeline = new ImagePipeLine();
            repo.Add(new SARImage(1, 20));
            repo.Add(new EOImage(2, 10));
            //repo.Add(new QuickLookImage(5,6));
            repo.Add(new IRImage(3, 5));
            //repo.Add(new QuickLookImage(5, 3));
            try
            {
                repo.Add(new SARImage(4, 150));
            }
            catch (ArgumentOutOfRangeException ex)
            { Console.WriteLine(ex.Message); }
            finally
            {
                Console.WriteLine("Enter to finally");
            }

            Console.WriteLine("processing images");
            //int totalScore = 0;
            pipeline.ShowList(repo.GetAll());
            //foreach (var img in repo.GetAll())
            //{
            //    string formatted = formatter.Format(img);
            //    int score = img.Score();
            //    totalScore += score;

            //    Console.WriteLine($"{formatted} , Score: {score}");
            //}

            //Console.WriteLine($"\nTotal System Score: {totalScore}");

            //Console.WriteLine($"Total images stored: {pipeline.StoredCount}");
        }
    }
}
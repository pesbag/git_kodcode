//using System.Collections.Generic;
using System;
namespace ex1
{
    class Track
    {
        public int Id { get; }
        public double Speed { get; set; }
        public Track(int id, double speed)
        {
            Id = id;
            Speed = speed;
        }

        public override string ToString()
        {
            return $"In Track: id:{Id}, speed:{Speed}";
        }
    }
    class Aircraft : Track
    {
        public double Altitude { get; }
        public Aircraft(int id, double speed, double altitude)
            : base(id, speed)
        {
            Altitude = altitude;
        }
        public override string ToString()
        {
            return $"In Aircarft: id:{Id}, speed:{Speed}, altitude:{Altitude}";
        }
    }
   }
    namespace ex3
    {
        abstract class Track
        {
            public int Id { get; }
            public double Speed { get; set; }
            protected Track(int id, double speed)
            {
                Id = id;
                Speed = speed;
            }
            public abstract string Describe();
        }
        class Aircraft : Track
        {
            public double Altitude { get; }
            public Aircraft(int id, double speed, double altitude)
                : base(id, speed) => Altitude = altitude;
            public override string Describe()
                => $"Aircraft {Id} at {Altitude} ft, {Speed} kn";
        }
        class Vessel : Track
        {
            public Vessel(int id, double speed) : base(id, speed) { }

            public override string Describe()
            => $"Vessel {Id}, {Speed} kn";
        }
    



class Program
    {
        public static void Main()
        {
            ex3.Aircraft a = new ex3.Aircraft(1, 420, 30000);
            //ex3.Aircraft b = new ex3.Aircraft(1, 324, 4343);
            //Console.WriteLine($"id:{a.Id}, speed:{a.Speed}, speed:{a.Altitude}");
            ex3.Vessel c = new ex3.Vessel(1, 300);
            ex3.Track[] allArr = {a,c,new ex3.Aircraft(1,2,3)};
            for (int i = 0; i < allArr.Length; i++)
            {
                Console.WriteLine(allArr[i].Describe());
            }

            List<ex3.Track> all = new List<ex3.Track>()
            {
            new ex3.Aircraft(1, 420, 30000),
            new ex3.Vessel(2, 18),
            new ex3.Aircraft(3, 510, 41000)
            };
            foreach (ex3.Track t in all)
                Console.WriteLine(t.Describe());
            Console.WriteLine(a);
        }
    }
}

using System;
namespace classes { 

    class Track
    {
        public int Id;
        public double Speed;
        public double Heading;
        public Track(int id,double speed,double heading)
        {
            Id = id;
            Speed = speed;
            Heading = heading;
        }
        public Track(int id): this(id, 0.0, 0.0) { }
    }
}
namespace ex4
{ 
    
        class Track
        {
            private double _heading;
            public int Id { get; }
            public double Speed { get; set; }
            public double Heading
            {
                get => _heading;
                set
                {
                    if (value < 0 || value > 359)
                        _heading = 0;
                    else
                        _heading = value;
                }
            }
            public Track(int id,double speed,double heading)
            {
                Id = id;
                Speed = speed;
                Heading = heading;
            }
        public override string ToString()
            => $"Track {Id}: {Speed} kn, heading: {Heading}";
        }
    }
    class Tirgol
    {
        static void Main()
        {
            classes.Track full = new classes.Track(17, 412.5,270);
            classes.Track quick = new classes.Track(8);
            Console.WriteLine($"quick:{quick.Id} , full:{full.Speed} kn");
            ex4.Track t = new ex4.Track(17, 412.5, 270);
            Console.WriteLine(t);
            t.Heading = 999;
            Console.WriteLine(t.Heading);
        }
    }

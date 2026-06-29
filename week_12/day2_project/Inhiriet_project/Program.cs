using System;
namespace project;

abstract class Platform
{
    private int _TrackId;
    private double _SpeedKnots;
    private double _Heading;
    public int TrackId
    {
        get => _TrackId;
        private set
        {
            if (value < 0)
                Console.WriteLine("Error TrackId should be a positive nunber");
            else _TrackId = value;
        }
    }
    public double SpeedKnots
    {
        get => _SpeedKnots;
        set 
        {
            if (value < 0)
                _SpeedKnots = 0;
            else _SpeedKnots =value;
        }
    }
    public double Heading
    {
        get => _Heading;
        set
        {
            if (value < 0 || value > 359)
                _Heading = 0;
            else _Heading = value;
        }
    }
    public abstract string StatusLine();
    public abstract bool IsTrackable();
    protected Platform(int trackId, double speedKnots, double heading)
    {
        Heading=heading;
        SpeedKnots = speedKnots;
        TrackId = trackId;
    }
    public abstract override string ToString();
}
class AirPlatform:Platform {
    private double _AltitudeFeet; //{ get; }
    public double AltitudeFeet
    {
        get => _AltitudeFeet;
        private set
        {
            if (value < 0)
                _AltitudeFeet = 100;
            else _AltitudeFeet = value;

        }
    }
    public AirPlatform(int trackId, double speedKnots, double heading, double altitudeFeet)
        : base(trackId, speedKnots, heading) => AltitudeFeet = altitudeFeet;
    public override bool IsTrackable()
    {
        if(AltitudeFeet>100 && AltitudeFeet < 60000 && SpeedKnots>0){
            return true;
        }
        return false;
    }
    public override string StatusLine()
    {
        return "In AirPlatform";
    }
    public override string ToString()
    {
        return $"TrackId: {TrackId}, SpeedKnots: {SpeedKnots},Heading: {Heading}";
    }
}
class SeaPlatform : Platform
{
    private double _DeepMeters;
    public double DeepMeters
    {
        get => _DeepMeters;
        set
        {
            if (value > 0)
                _DeepMeters = 0;
            else _DeepMeters = value;
        }
    }
    public SeaPlatform(int trackId, double speedKnots, double heading, double deepMeters)
        : base(trackId, speedKnots, heading) => DeepMeters = deepMeters;
    public override bool IsTrackable()
    {
        if(DeepMeters>0 && DeepMeters < 300)
        {
            return true;
        }
        return false;
    }
    public override string StatusLine()
    {
        return "In SeaPlatform";
    }
    public override string ToString()
    {
        return $"TrackId: {TrackId}, SpeedKnots: {SpeedKnots},Heading: {Heading}";
    }
}

class GraoundPlatform : Platform {
    private string _TerrainType;
    public string TerrainType
    {
        get => _TerrainType;
        private set
        {
            if (string.IsNullOrWhiteSpace(value))
                Console.WriteLine("Error: TerriranType cannot be empty");
            else _TerrainType = value;
        }
    }
    public GraoundPlatform(int trackId, double speedKnots, double heading, string terrainType)
        : base(trackId, speedKnots, heading) => TerrainType = terrainType;
    public override string StatusLine()
    {
        return "In GraoundPlatform";
    }
    public override bool IsTrackable()
    {
        if (string.Equals(_TerrainType, "tunnel", StringComparison.OrdinalIgnoreCase))
        {
            return true;
        }
        return false;
    }
    public override string ToString()
    {
        return $"TrackId: {TrackId}, SpeedKnots: {SpeedKnots},Heading: {Heading}";
    }
}

class main
{
    public static void Main()
    {
        List<Platform> lst = new List<Platform>();
        AirPlatform obj1 = new AirPlatform(1,100,90,20000);
        SeaPlatform obj2 = new SeaPlatform(2,120,270,50);
        GraoundPlatform obj3 = new GraoundPlatform(3,50,0,"tunnel");
        AirPlatform obj4 = new AirPlatform(4, 80,90, 50);
        SeaPlatform obj5 = new SeaPlatform(5, 130, 370, 400);
        GraoundPlatform obj6 = new GraoundPlatform(6, 350, -3, "river");
        lst.Add(obj1); lst.Add(obj2); lst.Add(obj3); lst.Add(obj4); lst.Add(obj5); lst.Add(obj6);
        for(int i = 0; i < lst.Count; i++)
        {
            Console.WriteLine($"StatusLine: {lst[i].StatusLine()}, IsTrackable: {lst[i].IsTrackable()}");
        }
    }
}
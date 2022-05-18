#[derive(Debug)]
//Struct for Converting Seconds to Years (Earth)
pub struct Duration
{
    earth_year: f64,
}

impl Duration
{
    //Constructor, seconds to years
    pub fn from(seconds: i32) -> Duration
    {
        Duration { earth_year: seconds as f64 / 31557600.0 }
    }
}

pub trait Planet 
{
    //Base fn for years on planet
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year
    }
}

pub struct Mercury;
pub struct Venus;
pub struct Earth;
pub struct Mars;
pub struct Jupiter;
pub struct Saturn;
pub struct Uranus;
pub struct Neptune;

//Implements earth year divided by modifier of orbital period for each planet
impl Planet for Mercury {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 0.2408467
    }
}
impl Planet for Venus {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 0.61519726
    }
}
impl Planet for Earth {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year
    }
}
impl Planet for Mars {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 1.8808158
    }
}
impl Planet for Jupiter {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 11.862615
    }
}
impl Planet for Saturn {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 29.447498
    }
}
impl Planet for Uranus {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 84.016846
    }
}
impl Planet for Neptune {
    fn years_during(d: &Duration) -> f64 
    {
        d.earth_year / 164.79132
    }
}

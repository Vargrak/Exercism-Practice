use std::fmt;

pub struct Clock
{
    hours: i32,
    minutes: i32,
}

impl Clock {
    //Constructor
    pub fn new(hours: i32, minutes: i32) -> Self 
    {
        //Modifiable Clock instance with hours and minutes
        let mut new_clock = Clock
        {
            hours: hours,
            minutes: minutes,
        };
        //Pass instance over loop to adjust time till it is in normal bounds
        new_clock.clock_boundary();
        return new_clock;
    }

    pub fn add_minutes(&self, minutes: i32) -> Self 
    {
        //Immutable passed to function, so new instance is created with modified minutes which is adjusted by the bounds checker.
        return Clock::new(self.hours, self.minutes + minutes)
    }

    pub fn clock_boundary(&mut self)
    {
        //Adjust hours and minutes to be in normal bounds
        while (self.hours < 0)
        {
            self.hours += 24;
        }
        while (self.hours > 23)
        {
            self.hours -= 24;
        }
        while (self.minutes < 0)
        {
            self.minutes += 60;
            self.hours -= 1;
        }
        while (self.minutes > 59)
        {
            self.minutes -= 60;
            self.hours += 1;
        }
        //If not in normal bounds, recursively calls itself
        if (self.hours < 0 || self.hours > 23 || self.minutes < 0 || self.minutes > 59)
        {
            self.clock_boundary()
        }
    }

    pub fn to_string(&self) -> String
    {
        //String format to hh:mm
        format!("{:02}:{:02}", self.hours, self.minutes)
    }
}

impl PartialEq for Clock
{
    fn eq(&self, other: &Clock) -> bool
    {
        //Equality check by string comparison
        self.to_string() == other.to_string()
    }
}

impl fmt::Debug for Clock
{
    fn fmt(&self, f: &mut fmt::Formatter) -> Result<(), fmt::Error>
    {
        //Debug is same as string
        write!(f, "{}", self.to_string())
    }
}

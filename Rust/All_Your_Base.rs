#[derive(Debug, PartialEq)]
pub enum Error {
    InvalidInputBase,
    InvalidOutputBase,
    InvalidDigit(u32),
}

//Base conversion entry point
pub fn convert(number: &[u32], from_base: u32, to_base: u32) -> Result<Vec<u32>, Error> 
{
    //Check that both bases and the number array are valid inputs
    match validity_check(number, from_base, to_base)
    {
        //Pass validity_check error up to caller or continue if nothing matches
        Err(e) => return Err(e),
        _ if number.iter().fold(0, |x, y| x + y) == 0 => return Ok(vec![0]),
        _ if number.len() == 0 => return Ok(vec![0]),
        _ => (),
    };

    //Convert the number array to base 10 number
    let mut sum = to_decimal(number, from_base);

    //Convert the base 10 number to the desired output base as array
    return Ok(to_arbitary_base(sum, to_base));
}

pub fn to_decimal(number: &[u32], from_base: u32) -> u32
{
    let mut len = number.len() as u32;
    let mut sum = 0;

    //Formula (n * b ^ (len - 1)), where n is the number and b is the base. Decrementing len going down the array
    for n in number
    {
        len -= 1;
        let temp = n * from_base.pow(len);
        sum += temp;
    }

    return sum;
}

pub fn to_arbitary_base(mut sum: u32, to_base: u32) -> Vec<u32>
{
    let mut result = vec![] as Vec<u32>;

    
    // Remainder added to array, then divided by the base. Repeat till the sum is exhausted.
    while sum > 0
    {
        let mut remainder = sum % to_base;
        sum /= to_base;
        result.push(remainder);
    }

    result.reverse();
    return result;
}

pub fn validity_check(number: &[u32], from_base: u32, to_base: u32) -> Result<u32,Error>
{
    return match number
    {
        // If any value is >= from_base in the array number, return InvalidDigit and grab that number to return
        _ if number.iter().any(|x| *x >= from_base) => Err(Error::InvalidDigit(*number.iter().find(|x| **x >= from_base).unwrap())),
        _ if from_base < 2 => Err(Error::InvalidInputBase),
        _ if to_base < 2 => Err(Error::InvalidOutputBase),
        _ => Ok(0),
    };
}
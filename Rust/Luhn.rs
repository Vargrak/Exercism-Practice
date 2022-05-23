/// Check a Luhn checksum.
pub fn is_valid(code: &str) -> bool 
{
    //Removes whitespace
    let code_fmt = code.replace(" ", "");
    
    //Passes to other functions
    return match valid_input(&code_fmt)
    {
        true => return valid_checksum(&code_fmt),
        _ => false
    }
}

pub fn valid_input(code: &String) -> bool
{
    //Checks if the string is longer than 1 and contains only digits
    return (code.len() > 1) && (code.chars().all(|c| c.is_digit(10)));
}

pub fn valid_checksum(code: &String) -> bool
{
    //Grabs the string and turns it into a char array
    return code
        .chars()
        //Reverse the array
        .rev()
        //Iterate over the array and give the index with the variable
        .enumerate()
        .fold(0, |acc, (i, c)|
        {
            //Char to int unwrapping
            let mut digit = c.to_digit(10).unwrap();
            //If the index (i) is not even, double the digit (and subtract 9 if it's over 9)
            if i % 2 == 1
            {
                digit *= 2;
                if digit > 9
                {
                    digit -= 9;
                }
            }
            acc + digit
            //If the accumulator mod 10 is 0, the code is valid
        }) % 10 == 0;
}
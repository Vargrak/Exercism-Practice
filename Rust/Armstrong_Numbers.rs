pub fn is_armstrong_number(num: u32) -> bool 
{
    let mut sum = 0;
    for n in num.to_string().chars()
    {
        let mut x = n.to_digit(10).unwrap();
        x = x.pow(num.to_string().len() as u32);
        sum += x;
    }
    sum == num
}

pub fn reverse(input: &str) -> String 
{
    let mut reversed: String = input.chars().rev().collect();
    return reversed;
}

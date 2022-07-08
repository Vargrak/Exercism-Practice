pub fn collatz(num: u64) -> Option<u64>
{

    if num == 0
    { return None; }

    let mut n: u64 = num;
    let mut i: u64 = 0;
    while n > 1
    {
        i = i + 1;
        n = match Some(n).unwrap()
        {
            _ if n % 2 == 0 => match n.checked_div(2)
                {
                    Some(n) => n,
                    None => return None
                }
            _ => match n.checked_mul(3)?.checked_add(1)
                {
                    Some(n) => n,
                    None => return None
                }
        };
        
    }
    return Some(i);
}

pub fn nth(n: u32) -> u32 
{
    let mut primes = vec![];
    let mut i = 2;

    while primes.len() <= n as usize
    {
        if primes.iter().any(|&x| i % x == 0) == false
        {
            primes.push(i);
        }

        i = i + 1;
    }

    return primes[primes.len() - 1] as u32;
}

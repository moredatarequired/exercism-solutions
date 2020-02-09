fn has_factors(n: u32, values: &[u32]) -> bool {
    for v in values {
        if n % v == 0 {
            return true;
        }
    }
    false
}

pub fn nth(n: u32) -> u32 {
    let mut primes: Vec<u32> = vec![];
    let mut num = 2u32;
    while primes.len() <= (n as usize) {
        while has_factors(num, &primes) {
            num += 1;
        }
        primes.push(num)
    }
    *primes.last().unwrap()
}

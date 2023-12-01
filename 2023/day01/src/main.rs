fn main_first_part() {
    let mut nbr: u32 = 0;
    for line in std::fs::read_to_string("input").unwrap().lines() {
        let first = line.as_bytes()[line.find(|c: char| {return c.is_numeric(); }).unwrap()];
        let last = line.as_bytes()[line.rfind(|c: char| {return c.is_numeric(); }).unwrap()];
        // println!("{} | {}", first - 48, last - 48);
        nbr += (first - 48) as u32 * 10 + (last - 48) as u32;
    }
    println!("{}", nbr);
}

static ARR: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

fn main() {
    let mut nbr: u32 = 0;
    for line in std::fs::read_to_string("input").unwrap().lines() {
        let mut firstp = line.find(|c: char| {return c.is_numeric(); }).unwrap_or(line.len() - 1);
        let mut first = line.as_bytes()[firstp] - 48;
        let mut lastp = line.rfind(|c: char| {return c.is_numeric(); }).unwrap_or(std::u32::MIN as usize);
        let mut last = line.as_bytes()[lastp] - 48;
        for (i, elem) in ARR.iter().enumerate() {
            let possible_first_position = line.find(*elem).unwrap_or(std::u32::MAX as usize);
            let possible_last_position = line.rfind(*elem).unwrap_or(std::u32::MIN as usize);
            if firstp > possible_first_position {
                first = i as u8 + 1;
                firstp = possible_first_position;
            }
            if lastp < possible_last_position {
                last = i as u8 + 1;
                lastp = possible_last_position;
            }
        }
        nbr += first as u32 * 10 + last as u32;
    }
    println!("{}", nbr);
}

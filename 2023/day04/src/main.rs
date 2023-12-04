fn part1() {
    let mut total = 0;
    for line in std::fs::read_to_string("input").unwrap().lines() {
        let sline = line.split(':').collect::<Vec<&str>>();
        let numbers = sline[1].split('|').collect::<Vec<&str>>();
        let winning_numbers = numbers[0].split(' ').filter(|x| !x.is_empty()).map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();
        let my_numbers = numbers[1].split(' ').filter(|x| !x.is_empty()).map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();
        let mut curr_card = 0;
        for winning_number in &winning_numbers {
            for my_number in &my_numbers {
                if winning_number == my_number {
                    if curr_card == 0 { curr_card = 1; }
                    else { curr_card *= 2; }
                }
            }
        }
        // println!("{}", curr_card);
        total += curr_card;
    }
    println!("{}", total);
}

fn part2() {
    let mut scratchcard_amount: Vec<usize> = vec![0; 200];
    for (i, line) in std::fs::read_to_string("input").unwrap().lines().enumerate() {
        let sline = line.split(':').collect::<Vec<&str>>();
        let numbers = sline[1].split('|').collect::<Vec<&str>>();
        let winning_numbers = numbers[0].split(' ').filter(|x| !x.is_empty()).map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();
        let my_numbers = numbers[1].split(' ').filter(|x| !x.is_empty()).map(|x| x.parse::<usize>().unwrap()).collect::<Vec<usize>>();
        let mut winning_number_amout = 0;
        for winning_number in &winning_numbers {
            for my_number in &my_numbers {
                if winning_number == my_number {
                    winning_number_amout += 1;
                }
            }
        }
        scratchcard_amount[i] += 1;
        for j in 1..winning_number_amout + 1 {
            scratchcard_amount[i + j] += scratchcard_amount[i];
        }
    }
    println!("{}", scratchcard_amount.iter().sum::<usize>());
}

fn main() {
    part1();
    part2();
}

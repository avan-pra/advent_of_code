static MAX_RED: u32 = 12;
static MAX_GREEN: u32 = 13;
static MAX_BLUE: u32 = 14;

fn check_game1(game_str: Vec<&str>) -> bool {
    for ball_show in game_str {
        let cshow = ball_show.split(",").collect::<Vec<&str>>();
        for ball in cshow {
            let balls = ball.strip_prefix(" ").unwrap().split(" ").collect::<Vec<&str>>();
            let ball_amount = balls[0].parse::<u32>().unwrap();
            match balls[1] {
                "red" => {
                    if ball_amount <= MAX_RED { continue; }
                    else { return false; }
                }
                "green" => {
                    if ball_amount <= MAX_GREEN { continue; }
                    else { return false; }
                }
                "blue" => {
                    if ball_amount <= MAX_BLUE { continue; }
                    else { return false; }
                }
                _ => { println!("ERROR !"); }
            }
        }
    }
    return true;
}

fn main_1() {
    let mut possible_game = 0;

    for game in std::fs::read_to_string("input").unwrap().lines() {
        let a = game.split(":").collect::<Vec<&str>>();
        let game_id = a[0].strip_prefix("Game ").unwrap().parse::<u32>().unwrap();
        let game_str = a[1].split(";").collect::<Vec<&str>>();
        if check_game1(game_str) {
            possible_game += game_id;
        }
        
    }
    println!("{}", possible_game);
}

fn check_game(game_str: Vec<&str>) -> u32 {
    let mut red_amount = 0;
    let mut green_amount = 0;
    let mut blue_amount = 0;
    for ball_show in game_str {
        let cshow = ball_show.split(",").collect::<Vec<&str>>();
        for ball in cshow {
            let balls = ball.strip_prefix(" ").unwrap().split(" ").collect::<Vec<&str>>();
            let ball_amount = balls[0].parse::<u32>().unwrap();
            match balls[1] {
                "red" => {
                    red_amount = std::cmp::max(red_amount, ball_amount);
                }
                "green" => {
                    green_amount = std::cmp::max(green_amount, ball_amount);
                }
                "blue" => {
                    blue_amount = std::cmp::max(blue_amount, ball_amount);
                }
                _ => { println!("ERROR !"); }
            }
        }
    }
    return red_amount * green_amount * blue_amount;
}

fn main() {
    let mut total_power = 0;

    for game in std::fs::read_to_string("input").unwrap().lines() {
        let a = game.split(":").collect::<Vec<&str>>();
        let game_id = a[0].strip_prefix("Game ").unwrap().parse::<u32>().unwrap();
        let game_str = a[1].split(";").collect::<Vec<&str>>();
        let power = check_game(game_str);
        total_power += power;
    }
    println!("{}", total_power);
}

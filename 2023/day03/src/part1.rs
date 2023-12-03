static WIDTH: usize = 140;
static HEIGHT: usize = 140;

fn check_surrounding(map: &Vec<&[u8]>, i: usize, j: usize) -> bool {
    let symbols = [b'+', b'-', b'*', b'/', b'%', b'@', b'&', b'#', b'$', b'='];
    for k in -1..2 { 
        for l in -1..2 {
            let rx: i32 = j as i32 + k;
            let ry: i32 = i as i32 + l;

            if rx >= 0 && ry >= 0 && rx < WIDTH as i32 && ry < HEIGHT as i32 && symbols.contains(&map[ry as usize][rx as usize]) {
                return true;
            }
        }
    }

    return false
}

pub fn part1() {
    let lines = std::fs::read_to_string("input").unwrap();
    let map = lines.lines().map(|f| f.as_bytes()).collect::<Vec<&[u8]>>();
    let arr_number = (48..58).collect::<Vec<u8>>();
    let mut total = 0;

    let mut i = 0;
    let mut j = 0;
    loop {
        let mut c_number_size = 0;
        let mut valid_nbr = false;
        while arr_number.contains(&map[i][j + c_number_size]) {
            if !valid_nbr {
                valid_nbr = check_surrounding(&map, i, c_number_size + j);
            }
            c_number_size += 1;
            if j + c_number_size >= WIDTH {
                break;
            }
        }
        if c_number_size > 0 && valid_nbr {
            let nbr = std::str::from_utf8(&map[i][j..j+c_number_size]).unwrap().parse::<u32>().unwrap();
            total += nbr;
        }
        j += c_number_size + 1;
        if j >= WIDTH {
            j = 0;
            i += 1;
        }
        if i >= HEIGHT {
            break;
        }
    }
    println!("{}", total);
}

static WIDTH: usize = 140;
static HEIGHT: usize = 140;

fn check_surrounding(map: &Vec<&[u8]>, i: usize, j: usize) -> Option<(usize, usize)> {
    let symbols = [b'*'];
    for k in -1..2 { 
        for l in -1..2 {
            let rx: i32 = j as i32 + k;
            let ry: i32 = i as i32 + l;

            if rx >= 0 && ry >= 0 && rx < WIDTH as i32 && ry < HEIGHT as i32 && symbols.contains(&map[ry as usize][rx as usize]) {
                return Some((ry as usize, rx as usize));
            }
        }
    }

    return None;
}

fn part2() {
    let lines = std::fs::read_to_string("input").unwrap();
    let map = lines.lines().map(|f| f.as_bytes()).collect::<Vec<&[u8]>>();
    let arr_number = (48..58).collect::<Vec<u8>>();
    let mut total = 0;
    let mut n_positio: Vec<[u32; 3]> = vec![];

    let mut i = 0;
    let mut j = 0;
    loop {
        let mut c_number_size = 0;
        // there's no star on 0;0 anyway
        let mut star_pos = (0, 0);
        while arr_number.contains(&map[i][j + c_number_size]) {
            if star_pos == (0, 0) {
                match check_surrounding(&map, i, c_number_size + j) {
                    Some(v) => { star_pos = v; }
                    None => {}
                }
            }
            c_number_size += 1;
            if j + c_number_size >= WIDTH {
                break;
            }
        }
        if c_number_size > 0 && star_pos != (0, 0) {
            let nbr = std::str::from_utf8(&map[i][j..j+c_number_size]).unwrap().parse::<u32>().unwrap();
            match n_positio.iter().position(|e| e[1] as usize == star_pos.0  && e[2] as usize == star_pos.1) {
                Some(v) => { 
                    total += n_positio[v][0] * nbr;
                }
                None => { n_positio.push([nbr, star_pos.0 as u32, star_pos.1 as u32]); }
            }
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

mod part1;

fn main() {
    part1::part1();
    part2()
}

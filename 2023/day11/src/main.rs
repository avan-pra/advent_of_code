fn part1() {
    let mut galaxy_map: Vec<Vec<usize>> = vec![];
    let mut c_galaxy = 1;

    for line in std::fs::read_to_string("input").unwrap().lines() {
        let mut c_galaxy_line: Vec<usize> = vec![];
        for char in line.chars() {
            if char == '#' { c_galaxy_line.push(c_galaxy); c_galaxy += 1; }
            else if char == '.' { c_galaxy_line.push(0); }
        }
        galaxy_map.push(c_galaxy_line);
    }

    let mut i = 0;
    while i < galaxy_map.len() {
        if galaxy_map[i].iter().all(|x| *x == 0) {
            let v: Vec<Vec<usize>> = vec![vec![0; galaxy_map[0].len()]];
            galaxy_map.splice(i..i, v.iter().cloned());
            i += 1;
        }
        i += 1;
    }
    i = 0;
    while i < galaxy_map[0].len() {

        if galaxy_map.iter().all(|x| x[i] == 0) {
            let v: Vec<usize> = vec![0; 1];
            for j in 0..galaxy_map.len() {
                galaxy_map[j].splice(i..i, v.iter().cloned());
            }
            i += 1;
        }
        i += 1;
    }

    let mut gpos: Vec<(usize, usize)> = vec![];
    for i in 0..galaxy_map.len() {
        for j in 0..galaxy_map[i].len() {
            if galaxy_map[i][j] != 0 {
                gpos.push((i, j));
            }
        }
    }

    let mut res = 0;
    for i in 0..gpos.len() {
        for j in i+1..gpos.len() {
            res += (gpos[i].0 as i32 - gpos[j].0 as i32).abs() + (gpos[i].1 as i32 - gpos[j].1 as i32).abs();
        }
    }
    println!("{}", res);
}

fn part2() {
    let mut gpos: Vec<((usize, usize), (usize, usize))> = vec![];
    let mut galaxy_map: Vec<Vec<usize>> = vec![];

    for (i, line) in std::fs::read_to_string("input").unwrap().lines().enumerate() {
        let mut c_galaxy_line: Vec<usize> = vec![];
        for (j, char) in line.chars().enumerate() {
            if char == '#' { gpos.push(((i, j), (i, j))); c_galaxy_line.push(103); }
            else if char == '.' { c_galaxy_line.push(0); }
        }
        galaxy_map.push(c_galaxy_line);
    }

    let mut i = 0;
    while i < galaxy_map.len() {
        if galaxy_map[i].iter().all(|x| *x == 0) {
            for elem in gpos.iter_mut() {
                if elem.0.0 > i {
                    elem.1.0 += 1000000 - 1;
                }
            }
        }
        i += 1;
    }
    i = 0;
    while i < galaxy_map[0].len() {
        if galaxy_map.iter().all(|x| x[i] == 0) {
            for elem in gpos.iter_mut() {
                if elem.0.1 > i {
                    elem.1.1 += 1000000 - 1;
                }
            }
        }
        i += 1;
    }

    let mut res: i128 = 0;
    for i in 0..gpos.len() {
        for j in i+1..gpos.len() {
            res += (gpos[i].1.0 as i128 - gpos[j].1.0 as i128).abs() + (gpos[i].1.1 as i128 - gpos[j].1.1 as i128).abs();
        }
    }

    println!("{}", res);
}

fn main() {
    part1();
    part2();
}

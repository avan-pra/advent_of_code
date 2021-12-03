use std::fs::File;
use std::io::{self, BufReader};
use std::io::prelude::*;

fn main() -> io::Result<()> {
    let f = File::open("./src/data")?;
    let f = BufReader::new(f);

    let mut datas: Vec<i32> = Vec::new();

	for line in f.lines() {
		datas.push(line.unwrap().parse::<i32>().unwrap())
	}

	for data in &datas {
		for data2 in &datas {
			for data3 in &datas {
				if data + data2 + data3 == 2020 {
					println!("{}", data * data2 * data3);
				}
			}
		}
	}

    Ok(())
}

use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
	let f = File::open("./src/data")?;
	let f = BufReader::new(f);

	let mut x = 0;
	let mut y = 0;
	let mut aim = 0;

	for line in f.lines() {
		let str: String = line.unwrap();
		let str_split: Vec<&str> = str.split(" ").collect();
		let action = str_split[0];
		let amount: i32 = str_split[1].parse().unwrap();
		match action {
			"forward" => {
				x += amount;
				y += amount * aim;
			},
			"down" => aim += amount,
			"up" => aim -= amount,
			_ => {}
		}
	}

	println!("{}", x * y);

	Ok(())
}
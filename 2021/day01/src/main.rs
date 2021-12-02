use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("./src/data")?;
    let f = BufReader::new(f);

	let mut arr: [i32; 2000] = [0; 2000];
	let mut arr2: [i32; 2000] = [0; 2000];
	let mut i = 0;

    for line in f.lines() {
		let nbr_as_string: String = line.unwrap();
		arr[i] = nbr_as_string.parse::<i32>().unwrap();
		i += 1;
    }

	i = 1;
	while i + 1 < 2000 {
		arr2[i - 1] = arr[i - 1];
		arr2[i - 1] += arr[i];
		arr2[i - 1] += arr[i + 1];
		i += 1;
	}

	i = 1;
	let mut count = 0;
	while i < 2000 {
		if arr2[i] > arr2[i - 1] {
			count += 1;
		}
		i += 1;
	}
	println!("{}", count);

    Ok(())
}

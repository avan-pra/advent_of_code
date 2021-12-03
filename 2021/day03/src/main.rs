use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn count_byte(i: u8, arr: Vec<String>) -> Vec<i32> {
	let mut ret = Vec::new();
	
	let mut o_count = 0;
	let mut i_count = 0;
	for element in arr {
		if element.as_bytes()[i as usize] == 48 {
			i_count += 1;
		}
		else {
			o_count += 1;
		}
	}
	ret.push(o_count);
	ret.push(i_count);

	return ret;
}

fn remove_if(i: u8, arr: &mut Vec<String>, count: Vec<i32>) {
	let mut j: i32 = 0;
	if count[0] != count[1] {
		while (j as usize) < arr.len() {										// invert the result
			if arr[j as usize].as_bytes()[i as usize] == if count[1] > count[0] { 48 } else { 49 } {
				arr.remove(j as usize);
				j -= 1;
			}
			j += 1;
		}
	}
	else {
		while (j as usize) < arr.len() {			// turn to 48
			if arr[j as usize].as_bytes()[i as usize] == 49 {
				arr.remove(j as usize);
				j -= 1;
			}
			j += 1;
		}
	}
}

fn main() -> io::Result<()> {
	let f = File::open("./src/data")?;
	let f = BufReader::new(f);

	let mut columns: Vec<String> = Vec::new();

	for line in f.lines() {
		columns.push(line.unwrap());
	}

	let mut tmp: Vec<String> = columns.clone();
	let mut count: Vec<i32>;

	for i in 0..12 {
		count = count_byte(i, tmp.to_vec());
		if tmp.len() == 1 {
			break;
		}
		else {
			remove_if(i, &mut tmp, count.to_vec())
		}
	}

	println!("{}", tmp.len());
	println!("{}", isize::from_str_radix(&tmp[0], 2).unwrap());

	Ok(())
}
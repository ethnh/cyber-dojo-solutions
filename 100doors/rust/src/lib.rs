#![cfg_attr(feature = "strict", deny(warnings))]

/*

100 doors in a row are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it).
The second time you only visit every 2nd door (door #2, #4, #6, ...).
The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?

[Source http://rosettacode.org]

*/

pub fn generate_doors() -> Vec<bool> {
    vec![false; 100] // create a vector of 100 false's
}

pub fn walk_through(doors: Vec<bool>, count: i32) -> Vec<bool> {
    let mut doors_new = doors.clone();
    for (current, value) in doors.iter().enumerate() {
        if current % (count as usize) == 0 {
            doors_new[current] = !value;
        }
    }
    //println!("count {:?} value {:?}", count, doors_new);
    doors_new
}

pub fn walk_through_100_doors() -> bool {
    let mut doors = generate_doors();
    for i in 1..101 {
        println!("{:?}", i);
        doors = walk_through(doors, i);
    }
    println!("{:?}", doors);
    true
}

pub fn main() {
    let _lol = walk_through_100_doors();
}

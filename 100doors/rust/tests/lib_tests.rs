#![cfg_attr(feature = "strict", deny(warnings))]

use hiker;

#[test]
fn doors_all_false() {
    for door in hiker::generate_doors() {
        assert!(!door); // assert door == false
    }
}

#[test]
fn number_of_doors() {
    assert_eq!(hiker::generate_doors().len(), 100);
}

#[test]
fn doors_all_true_on_first_pass() {
    for door in hiker::walk_through(hiker::generate_doors(), 1) {
        assert!(door); // assert door == true
    }
}

#[test]
fn half_of_doors_false_on_second_pass() {
    let mut doors = hiker::generate_doors();
    doors = hiker::walk_through(doors, 1);
    doors = hiker::walk_through(doors, 2);
    let count_true = doors.into_iter().filter(|x| x == &true).count();
    assert_eq!(count_true, 50);
}
// I don't think any more testing would be useful, not sure what else to add

#[test]
fn this_is_not_an_actual_test_i_just_want_to_see_the_answer() {
    assert!(hiker::walk_through_100_doors())
}

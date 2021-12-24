#![cfg_attr(feature = "strict", deny(warnings))]

use christmas;

#[test]
fn test_initial_strings_is_none() {
    let carol = christmas::Carol::new();
    let empty_vec_string: Vec<String> = vec![];
    assert_eq!(carol._get_carol(), &empty_vec_string);
    let zero: u8 = 0;
    assert_eq!(carol._get_day(), &zero);
}

#[test]
fn test_day_one() {
    let mut carol = christmas::Carol::new();
    carol.next_day_of_christmas(&String::from("A partridge in a pear tree."));

    let day_one_vec: Vec<String> = vec![String::from("A partridge in a pear tree.")];
    assert_eq!(carol._get_carol(), &day_one_vec);
    let one: u8 = 1;
    assert_eq!(carol._get_day(), &one);
    let day_one_str = "First";
    assert_eq!(carol._get_day_as_str(), day_one_str);
}

#[test]
fn sing_me_a_carol() {
    // !! just run through the carol
    let mut carol = christmas::Carol::new();
    carol.next_day_of_christmas(&String::from("A partridge in a pear tree."));
    carol.next_day_of_christmas(&String::from("Two turtle doves"));
    carol.next_day_of_christmas(&String::from("Three french hens"));
    carol.next_day_of_christmas(&String::from("Four calling birds"));
    carol.next_day_of_christmas(&String::from("Five golden rings"));
    carol.next_day_of_christmas(&String::from("Six geese a-laying"));
    carol.next_day_of_christmas(&String::from("Seven swans a-swimming"));
    carol.next_day_of_christmas(&String::from("Eight maids a-milking"));
    carol.next_day_of_christmas(&String::from("Nine ladies dancing"));
    carol.next_day_of_christmas(&String::from("Ten lords a-leaping"));
    carol.next_day_of_christmas(&String::from("Eleven pipers piping"));
    carol.next_day_of_christmas(&String::from("Twelve drummers drumming"));
}

#![cfg_attr(feature = "strict", deny(warnings))]

const LETTER_PAIRS: [(&str, &str); 20] = [
    ("B", "O"),
    ("X", "K"),
    ("D", "Q"),
    ("C", "P"),
    ("N", "A"),
    ("G", "T"),
    ("R", "E"),
    ("T", "G"),
    ("Q", "D"),
    ("F", "S"),
    ("J", "W"),
    ("H", "U"),
    ("V", "I"),
    ("A", "N"),
    ("O", "B"),
    ("E", "R"),
    ("F", "S"),
    ("L", "Y"),
    ("P", "C"),
    ("Z", "M"),
];
pub fn can_make_word(word: &str) -> bool {
    let mut word = word.to_uppercase();
    for (a, b) in LETTER_PAIRS.iter() {
        println!("{} {}", a, b);
        if word.contains(a) {
            word = word.replacen(a, "", 1);
            continue;
            // We can only use one of the letters in the pair
        }
        if word.contains(b) {
            word = word.replacen(b, "", 1);
            continue;
            // Just to make it match the other case
        }
    }
    word.is_empty()
}

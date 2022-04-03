#![cfg_attr(feature = "strict", deny(warnings))]

// ---- Testing Outline ----
//
// 1. Major Tests: (Test the behaviour of the library, or test any requirements outlined in README.md)
//    - Test that the library is able to actually solve the abc problem
//    - Test against the problems in README.md
// 2. Minor Tests: (Per-function tests, implementation-specific. Not BDD, so can be replaced if implementation changes.)
//    - Example: Test that sort_characters_by_frequency() returns a correctly sorted vec.
//
// ---- End of Test Outline ----

// Task
// Write a function that takes a string (word) and determines whether the word can be spelled with the given collection of blocks.
// The rules are simple:
// 1.Once a letter on a block is used that block cannot be used again
// 2.The function should be case-insensitive
// 3.Show the output on this page for the following 7 words in the following example

use abc::*;

#[test]
fn test_can_make_word() {
    // Test that the library is able to actually solve the abc problem
    assert_eq!(can_make_word("A"), true);
    assert_eq!(can_make_word("BARK"), true);
    assert_eq!(can_make_word("BOOK"), false);
    assert_eq!(can_make_word("TREAT"), true);
    assert_eq!(can_make_word("COMMON"), false);
    assert_eq!(can_make_word("SQUAD"), true);
    assert_eq!(can_make_word("CONFUSE"), true);
}

#![cfg_attr(feature = "strict", deny(warnings))]

use abc;

#[test]
fn life_the_universe_and_everything() {
    assert_eq!(1, abc::answer());
}

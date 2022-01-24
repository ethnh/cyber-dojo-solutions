#![cfg_attr(feature = "strict", deny(warnings))]
use std::collections::HashMap;

pub struct Carol {
    day: u8,
    carol: Vec<String>,
}
impl Default for Carol {
    fn default() -> Self {
        Self::new()
    }
}

impl Carol {
    pub fn new() -> Carol {
        Carol {
            day: 0,
            carol: vec![],
        }
    }
    pub fn _get_day(&self) -> &u8 {
        // Would not be called normally,
        // self.day should only be modified and read by functions
        // Could be useful though
        &self.day
    }
    pub fn _get_day_as_str(&self) -> &str {
        let week_day = HashMap::from([
            (1, "First"),
            (2, "Second"),
            (3, "Third"),
            (4, "Fourth"),
            (5, "Fifth"),
            (6, "Sixth"),
            (7, "Seventh"),
            (8, "Eigth"),
            (9, "Ninth"),
            (10, "Tenth"),
            (11, "Eleventh"),
            (12, "Twelveth"),
        ]);
        match week_day.get(&self.day) {
            Some(day) => day,
            None => "There are no days beyond the twelveth",
        }
    }
    pub fn _get_carol(&self) -> &Vec<String> {
        // Would not be called normally,
        // self.carol should only be modified and read by functions
        // Could be useful though
        &self.carol
    }
    pub fn next_day_of_christmas(&mut self, line: &str) {
        self.carol.push(line.to_string());
        self.day += 1;
        if self.day > 12u8 {
            panic!("there aren't 13 days?!");
        }
        let day_as_str = self._get_day_as_str();
        println!("On the {} day of Christmas", day_as_str);
        println!("My true love gave to me:");
        for line in self.carol.iter().rev() {
            println!("{}", line);
        }
        println!(); // line spacing
    }
}

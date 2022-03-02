#!/bin/python3

# plan:
# can_make_word(word) -
#   check for any issues w/ word (optional)
#   call get_needed_pairs w/ get_needed_pairs
#   get_needed_pairs(word) -
#       find every pair that has a letter in the word
#   sort by least used letter and remove needed pairs until word is reconstructed
#   check if word reconstructed successfully


letter_pairs_from_readme = (
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
)

all_letters_available = ""
for letter_a, letter_b in letter_pairs_from_readme:
    all_letters_available += letter_a + letter_b


def sort_by_least_occurring(word: str) -> list[str]:
    # First, count the number of times each letter occurs
    # Second, in order from least to most, append the letters
    #  into a list, in the order that they were originally in
    #  (ex: "WOOD" -> "WDOO", "WOAH" -> "WOAH")
    letters = list(word)
    letters_count = {letter: 0 for letter in letters}
    for letter in letters:
        letters_count[letter] += 1

    order = "".join(
        [
            letter * count
            for (letter, count) in sorted(
                letters_count.items(), key=lambda item: item[1]
            )
        ]
    )
    # Join and then list to negate the effects of letter*count,
    #  ['a'*3] == ['aaa'], where we want ['a', 'a', 'a']
    return list(order)


def get_needed_pairs(word, letter_pairs) -> list:
    letter_pairs_needed = []
    for pair in letter_pairs:
        if (pair[0] in word) or (pair[1] in word):
            letter_pairs_needed.append(pair)
            # append to letter_pairs_needed if either letter is in the word
    return letter_pairs_needed


def reassemble_word(letters_to_use: list[tuple[str]], word_to_make: str) -> str:
    return ""  # TODO


def can_make_word(word: str) -> bool:
    word = word.upper()
    for letter in word:
        if letter not in all_letters_available:
            return False
    reconstructed = ""
    # TODO
    return reconstructed == word

#!/bin/python3

letter_pairs_from_readme = (
    # Copied from README.md
    # Edited to fit the format of the problem
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


def can_reassemble_word(letters_to_use: list[tuple[str]], word_to_make: str) -> bool:
    # reassemble_word(letters_to_use, word_to_make) -
    #   for each letter in word_to_make,
    #   find the corresponding letter in letters_to_use
    #   remove the letter from letters_to_use
    #   append the letter to the new word

    # This is of the complexity O(n^2) I believe -
    # Very complex double-for loop, but at this size, it's not a big deal
    word_to_make = "".join(sort_by_least_occurring(word_to_make))
    for letter in word_to_make:
        for pair in letters_to_use:
            if letter in pair:
                # replace with placeholder to indicate removed
                #  if word_to_make.remove is used, it would mess up for loop
                word_to_make = word_to_make.replace(letter, ".", 1)
                letters_to_use.remove(pair)
                break
    # remove placeholder letters
    word_to_make = word_to_make.replace(".", "")
    if len(word_to_make) == 0:
        return True

    return False


def can_make_word(word: str) -> bool:
    if len(word) == 0:
        return True
    # can_make_word(word) -
    #   check for any issues w/ word (optional)
    #   call get_needed_pairs w/ get_needed_pairs
    #   get_needed_pairs(word) -
    #       find every pair that has a letter in the word
    #   sort by least used letter and remove needed pairs until word is reconstructed
    #   check if word reconstructed successfully
    word = word.upper()
    for letter in word:
        if letter not in all_letters_available:
            return False

    needed_pairs = get_needed_pairs(word, letter_pairs_from_readme)
    return can_reassemble_word(needed_pairs, word)

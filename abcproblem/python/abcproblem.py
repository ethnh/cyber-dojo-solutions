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


def sort_by_least_occurring(word: str) -> list[str]:
    return ["lol", word]  # TODO


def get_needed_pairs(word, letter_pairs) -> list:
    letter_pairs_needed = []
    for pair in letter_pairs:
        if (pair[0] in word) or (pair[1] in word):
            letter_pairs_needed.append(pair)
            # append to letter_pairs_needed if either letter is in the word
    return letter_pairs_needed


def reassemble_word(letters_to_use: list[str], word_to_make: str) -> str:
    return ""  # TODO


def can_make_word(word: str) -> bool:
    word = word.upper()
    reconstructed = ""
    # TODO
    return reconstructed == word

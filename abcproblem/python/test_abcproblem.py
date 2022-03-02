from abcproblem import *

# plan:
# can_make_word(word) -
#   check for any issues w/ word (optional)
#   call get_needed_pairs w/ get_needed_pairs
#   get_needed_pairs(word) -
#       find every pair that has a letter in the word
#   sort by least used letter
#       This is done to lower the chance that a word cannot be reconstructed because
#       a needed letter is taken by a more common letter,
#       ex: WALL -- ("L", "A"), ("L", "C"), ("W", "D"), ("Q", "L")
#                   L      A      L           W                L
#                   You can make WALL with these letters, but if you use the L from the ("L", "A") pair, you cannot.
#       -- This is not perfect, perhaps there's a better way to do this?
#   remove needed pairs until word is reconstructed
#   check if word reconstructed successfully


def test_fails_if_word_contains_letters_not_in_pairs():
    assert can_make_word("FART11") == False
    assert can_make_word("WOWOWO!!!!") == False
    assert can_make_word("QWERTYo/") == False


def test_get_needed_pairs():
    # This is a low-priority test: Can be deleted if implementation changes and the function is no longer needed.
    #   get_needed_pairs(word) -
    #       find every pair that has a letter in the word
    pairs = get_needed_pairs("HUX")
    assert ("X", "K") in pairs
    # X from (X, K) would be needed to make the word "HU|X|"


def test_sort_by_least_occurring():
    # def sort_by_least_occurring(word: str) -> list[str]: sort by least used letter and remove needed pairs until
    # word is reconstructed
    # assert sort_by_least_occurring("AAABBC") == ["C", "B", "B", "A", "A", "A"]
    # assert sort_by_least_occurring("LAMBDA") == ["L", "M", "B", "D", "A", "A"]
    # ^ Issue with testing like this: L M B D all occur once, the order in which they appear in the list is irrelevant,
    # but this test requires it to be ordered like this arbitrarily.
    # better test: count number of times a letter is in str,
    # and make sure whatever letters have the lowest count comes before the most
    word = "LAMBDA"
    sorted = sort_by_least_occurring(word)
    # L occurs less than A, L should come before A
    assert sorted.index("L") < sorted.index("A")

    word = "COMMON"
    sorted = sort_by_least_occurring(word)
    # C occurs less than M, C should come before M
    assert sorted.index("C") < sorted.index("M")


def test_reassemble_word():
    # check if word reconstructed successfully from pairs
    #   def reassemble_word(letters_to_use: list[tuple[str]], word_to_make: str) -> str:
    assert (
        reassemble_word([("S", "W"), ("R", "A"), ("W", "J"), ("H", "G")], "SWAG")
        == "SWAG"
    )


def test_can_make_word():
    # final test -- from readme
    assert can_make_word("A") is True
    assert can_make_word("BARK") is True
    assert can_make_word("BOOK") is False
    assert can_make_word("TREAT") is True
    assert can_make_word("COMMON") is False
    assert can_make_word("SQUAD") is True
    assert can_make_word("CONFUSE") is True

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


def test_get_needed_pairs():
    #   get_needed_pairs(word) -
    #       find every pair that has a letter in the word

    pass  # TODO: ADD TEST


def test_sort_by_least_occurring():
    # def sort_by_least_occurring(word: str) -> list[str]:
    #   sort by least used letter and remove needed pairs until word is reconstructed
    assert sort_by_least_occurring("AAABBC") == ["C", "B", "B", "A", "A", "A"]
    # assert sort_by_least_occurring("LAMBDA") == ["L", "M", "B", "D", "A", "A"]
    #   TODO : Sorting may be implemented in a different way, perhaps this test isn't the greatest 🤣


def test_reassemble_word():
    #   check if word reconstructed successfully from pairs
    pass  # TODO: ADD TEST


def test_can_make_word():
    # final test -- from readme
    assert can_make_word("A") is True
    assert can_make_word("BARK") is True
    assert can_make_word("BOOK") is False
    assert can_make_word("TREAT") is True
    assert can_make_word("COMMON") is False
    assert can_make_word("SQUAD") is True
    assert can_make_word("CONFUSE") is True

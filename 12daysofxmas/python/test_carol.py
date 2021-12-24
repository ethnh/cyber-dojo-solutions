from carol import *
# not best to import *, but this is dev not prod

def test_empty_carol_is_empty():
    new_carol = Carol()
    assert [] == new_carol._carol


def test_adding_line_to_carol():
    new_carol = Carol()
    new_carol.add_line('Christmas is just a week away!')
    assert ['Christmas is just a week away!'] == new_carol._carol


def test_day_counter_never_exceeds_12():
    new_carol = Carol()
    try:
        for i in range(100):
            new_carol.add_line('Line')
            assert new_carol._day <= 12 # less than or equal
    except ValueError as err: pass
    # If it isn't a ValueError, exception raised, test fail
    # If it allows _day > 12, assertion failed, test fail
    
def test_day_repr():
    new_carol = Carol()
    new_carol.add_line('') # Content does not matter
    assert new_carol.day_as_str() == "First"

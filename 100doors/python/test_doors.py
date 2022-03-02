from doors import *

# not best to import *,
# change if ever prod LOL


def test_initial_doors():
    doors = gen_doors()
    assert doors != None  # make sure something is actually returned lol
    assert len(doors) == 100  # make sure length is correct
    assert False == (True in [door.open for door in doors])
    # make sure door.open is false for every door when starting


def test_hiker_first_visit():
    doors = gen_doors()
    visit_doors(doors, 1)
    assert True in [door.open for door in doors]
    # make sure door.open is true for every door after first visit
    # opposite of initial_doors


def test_hiker_second_visit_half_open():
    doors = gen_doors()
    visit_doors(doors, 1)
    visit_doors(doors, 2)
    count_true = 0
    for door in doors:
        if door.open:
            count_true += 1
    assert count_true == 50


# Not sure what else I can test

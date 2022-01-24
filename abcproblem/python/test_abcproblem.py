from abcproblem import *


def test_global_answer():
    assert global_answer() == 1


def test_instance_method():
    assert Hiker().instance_answer() == 1

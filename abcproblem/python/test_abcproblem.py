from abcproblem import *


def test_global_answer():
    assert global_answer() == 42


def test_instance_method():
    assert Hiker().instance_answer() == 42
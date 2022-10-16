from string_utils import *
from string_utils import _explode_list_of_strings, explode_string

def test_explode_string():
    assert explode_string('Han') == ['H', 'a', 'n']
    assert explode_string('') == []


def test_explode_list_of_strings():
    assert _explode_list_of_strings(['Han', 'Solo']) == [['H', 'a', 'n'], ['S', 'o', 'l', 'o']]
    assert _explode_list_of_strings(['', '', '']) == [[],[],[]]
    assert _explode_list_of_strings([]) == []
import pytest
from list_utils import *

def test_find_one():
    needle = 1
    none = [0, 0 , 5,'s']
    beginning = [1, None,9,6,0,0]
    end = ['x', '0', 1]
    several = [ 0,0,3,4,1,3,2,1,3,4]

    assert find_one(none, needle) == False
    assert find_one(beginning, needle)
    assert find_one(end, needle)
    assert find_one(several, needle)

def test_find_n():
    assert find_n([2, 3, 4, 5, 6], 2, -1) == False
    assert find_n([1, 2, 3, 4, 5], 42, -1) == False
    assert find_n([1, 2, 3, 4, 5], 1, 2) == False
    assert find_n([1, 2, 3, 2, 4, 5], 2, 2)
    assert find_n([1, 2, 3, 4, 5, 6 , 7, 4, 6], 4, 2)
    assert find_n([1, 2, 3, 2, 4, 5], 'x', 0) == True

def test_find_streak():
    assert find_streak([1, 2, 3, 4, 5], 4, -1) == False
    assert find_streak([1, 2, 3, 4, 5], 42, 2) == False
    assert find_streak([1, 2, 3, 4], 4, 1) 
    assert find_streak([1, 2, 3, 1, 2], 2, 2) == False
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 3)
    assert find_streak([5, 5, 5,1, 2, 3, 4], 5, 3)
    assert find_streak([1, 2, 5, 5, 5, 3, 4], 5, 3)
    assert find_streak([1, 2, 3, 4, 5, 5, 5], 5, 4) == False 

def test_first_elements():
    original = [[0,7,3],[4,0,1]]
    #matriz_2 = [[None,7,3,],[None,0,1]]
    #matriz_3 = [[None,None,None],[None,None,None]]

    assert first_elements(original) == [0,4]
    #assert first_elements(matriz_2) == [None,None]
    #assert first_elements(matriz_3) == [None,None]

def test_transpose():
    original = [[0,7,3],[4,0,1]]
    transposed = [[0,4],[7,0],[3,1]]

    assert transpose(original) == transposed
    assert transpose(transpose(original)) == original

from toolkit.randomness import entropy

def test_entropy():
    assert entropy([1,1,1,1]) == 0

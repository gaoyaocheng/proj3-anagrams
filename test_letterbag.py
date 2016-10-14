"""
Nose tests for letterbag.py
"""
from letterbag import LetterBag

def test_empty():
    """
    Empty string <=> empty LetterBag
    """
    assert str(LetterBag("")) == ""

def test_simple_str():
    """
    A simple LetterBag with multiples of a couple letters.
    """
    assert str(LetterBag("xaxyzyb")) == "abxxyyz"


def test_contains_basic_examples():
    """
    Examples from the docstring of LetterBag.contains,
    with and without auto-conversion to LetterBag
    """
    # Passing other as LetterBag
    assert LetterBag("abbc").contains(LetterBag("abc"))
    assert LetterBag("abbc").contains(LetterBag("abbc"))
    assert not LetterBag("abc").contains(LetterBag("abbc"))
    # Passing other as string
    assert LetterBag("abbc").contains("abc")
    assert LetterBag("abbc").contains("abbc")
    assert not LetterBag("abc").contains("abbc")

def test_simple_merge():
    bag_abbc = LetterBag("abbc")
    bag_abccd = LetterBag("abccd")
    bag_abbc.merge(bag_abccd)
    assert bag_abbc.as_string() == "abbccd"
def test_merge_with_empty():
    bag_ = LetterBag("")
    bag_abbc = LetterBag("abbc")
    bag_abbc.merge(bag_)
    assert not bag_abbc.as_string() == ""
    bag_ = LetterBag("")
    bag_abbc = LetterBag("")
    bag_abbc.merge(bag_)
    assert bag_abbc.as_string() == ""
def test_same_merge():
    bag_abc = LetterBag("abc")
    bag_abc_ = LetterBag("abc")
    bag_abc.merge(bag_abc_)
    assert bag_abc.as_string() == "abc"




"""
Nose tests for trie.py
"""

from trie import TrieTree

def test_empty_tree():
    """
    Nothing is present in an empty word list
    """
    tree = TrieTree( [ ] )
    assert tree.travel(tree.tree) == []
    matched, list = tree.search("a")
    assert not matched

def test_single_tree():
    tree = TrieTree([ "a" ])
    assert tree.travel(tree.tree) == ["a"]
    matched, list = tree.search("a")
    assert matched
    assert "a" in list
    matched, list = tree.search("b")
    assert not matched
    assert "b" not in list

def test_small_tree():
    l = ["abc", "abd", "bcd", "cda"];
    tree = TrieTree(l)
    tr = tree.travel(tree.tree)
    assert tr.sort() == l.sort()
    matched, list = tree.search("abc")
    assert matched
    assert "a" not in list
    matched, list = tree.search("ab")
    assert not matched
    assert "ab" not in list
    matched, list = tree.search("e")
    assert not matched
    assert "e" not in list


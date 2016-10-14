"""
A trieTree struct and search method
"""
class TrieTree(object):
  def __init__(self, word_list):
    """
        Initialize the dict tree with word list
    Args:
        wrod_list is a list
    """
    self.tree = {}

    for word in word_list:
        self.add(word)

  def add(self, word):
    """
      add a word to TrieTree
      Args:
        word : string

    """
    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        tree[char] = {}
        tree = tree[char]

    tree['value'] = word

  def travel(self, tree):
    """
    return all words of dict tree
    Args:
        tree : a dict
    Return:
        the word on this dict and subdict
    """
    result = []

    if "value" in tree:
        result.append(tree['value'])

    for (d, x) in tree.items():
        if(d == "value"):
            continue
        child_tree = tree[d]
        result.extend(self.travel(child_tree))

    return result

  def search(self, word):
    """
      Search word in trietree
      Args:
         word : a string
      Returns:
        if word in trietree, return the list of
            prefix match words list
            if matched:
            (True, prefix_match_list)
            if not matched:
            (False, prefix_match_list)
        if not in  return (False, [])
    """
    if word == "":
        return None

    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        return (False, [])
    prefix_match_list = self.travel(tree)
    return ("value" in tree, prefix_match_list)


#words = ['abc', 'abd', 'abcd', 'aesa', 'aefds']
#tree = TrieTree(words)
#print(tree.search("ae"))

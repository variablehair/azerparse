"""Classes for containing morphological objects."""

import methods_morph

class Affix:
    """A class representing a single affix."""
    def __init__(self, string_in, tag):
        self.s = string_in
        self.tag = tag
    def __hash__(self):
        return hash((self.s, self.tag))
    def __eq__(self, other):
        return (self.s, self.tag) == (other.s, other.tag)
    def to_string(self):
        return self.s
    def to_tag(self):
        return self.tag

class ParseList:
    """A class representing a single set of possible affix combinations."""
    def __init__(self):
        self.affixes = []
    def __hash__(self):
        return hash(self.affixes)
    def __eq__(self, other):
        return self.affixes == other.affixes
    def to_string(self):
        tags = map(lambda x: x.to_tag, self.affixes)
        return root + ' - '.join(tags)
    def append(self, a):
        """No validation is done at this step, do it before"""
        self.affixes.append(a)
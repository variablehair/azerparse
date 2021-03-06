"""Contains helper methods pertaining to morphology."""
import sys, os

THIS_PATH = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(THIS_PATH)

import json
import os
from classes_morph import Affix

with open(THIS_PATH + '/affixes.json', encoding='utf-8') as f:
    affix_dict = json.load(f)

def string_to_affix(s):
    """Takes in a string (i.e. 'dir') and returns a list of possible Affix objects. If none, returns []."""
    ret = []

    # Finds the indices of s in values (string lit representation) then appends the corresponding key,
    # which is the morphological tag (e.g. "COP.3SGDIR_i")
    from_i = 0
    taglist = []
    while True:
        try:
            found_i = list(affix_dict.values()).index(s, from_i)
        except ValueError:
            break
        taglist.append(list(affix_dict.keys())[found_i])
        from_i = found_i + 1
        
    for tag in taglist:
        ret.append(Affix(s, tag))
    return ret

def is_affix(s):
    """Returns true if the input string is found among the list of affixes."""
    return s in affix_dict.values()
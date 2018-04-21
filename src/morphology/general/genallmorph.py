"""Generates all possible morphological parses from a given set of possible affixes."""

import methods_morph

AFFIX_LEN_MAX = 4
AFFIX_LEN_MIN = 1

def genallmorph(string_in):
    """Takes the affixes only; pass the word minus the root to this function"""
    ret = []
    interm_dict = {} # dictionary keeping track of intermediate steps

    def consume_one(ParseList p, c1str):
        c1ret = []
        i = AFFIX_LEN_MIN
        while i <= AFFIX_LEN_MAX:
            potential_affix = c1str[0:i]
            if not methods_morph.is_affix(potential_affix):
                raise ValueError(c1str + "is not a valid affix")
            else:

                
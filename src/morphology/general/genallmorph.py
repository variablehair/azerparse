"""Generates all possible morphological parses from a given set of possible affixes."""

import sys, os
from copy import deepcopy

THIS_PATH = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(THIS_PATH)

import methods_morph
from classes_morph import Affix, ParseList

AFFIX_LEN_MAX = 4
AFFIX_LEN_MIN = 1

def genallmorph(string_in):
    """Takes a string and returns a list of ParseList objects.
    Takes the affixes only; pass the word minus the root to this function"""
    ret = []

    def consume_one(c1str):
        """Takes a string and returns a list of tuples: (Affix, remaining string)"""
        c1ret = []
        i = AFFIX_LEN_MIN
        while i <= AFFIX_LEN_MAX and i <= len(c1str):
            potential_affix = c1str[0:i]
            if methods_morph.is_affix(potential_affix):
                affix_list = methods_morph.string_to_affix(potential_affix)
                for a in affix_list:
                    c1ret.append( (a, c1str[i:]) )
            i += 1
        return c1ret

    # iterate through inc_parse_list until it is empty; completed entries are
    # placed in ret. List members are of the form (ParseList, remaining_str)


    inc_parse_list = []
    for result in consume_one(string_in):
        pl = ParseList()
        pl.append(result[0])
        inc_parse_list.append( (pl, result[1]) )
        #print([str(x[0]) for x in inc_parse_list])
   
    while len(inc_parse_list) > 0:
        curr_tup = inc_parse_list.pop()
        #if curr_tup[0] is None: # how does this happen?!
        #    continue
        if len(curr_tup[1]) == 0: # if no more strings to consume, add to ret
            ret.append(curr_tup[0])
        else:
            #print(str(curr_tup[0]), curr_tup[1])
            c1out = consume_one(curr_tup[1])
            #print([(str(f[0]), f[0].to_tag(), f[1]) for f in c1out])
            if len(c1out) == 0:
                continue
            for result in c1out:
                copy_tup = deepcopy(curr_tup)
                parsel = copy_tup[0]
                parsel.append(result[0])
                inc_parse_list.append( (parsel, result[1]) )

    return ret
            

                
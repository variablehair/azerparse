"""Collection of helper methods used by the main azerparse program."""

from lexicon.getsyncat import getsyncat
from lexicon.findallwords import findallwords
from morphology.general.genallmorph import genallmorph

def process_word(query : str):
    """Returns the complete raw text output for a given word"""
    results = {}
    lex_tups = findallwords(query)
    for tup in lex_tups:
        morphs = genallmorph(tup[1])
        if len(morphs) > 0:
            results[tup[0]] = morphs
    
    str_out = ''
    for root in results:
        str_out += ('ROOT = ' + root + '\n')
        morphs_str = [root + ' + ' + str(x) for x in results[root]]
        str_out += '\n'.join(morphs_str) + '\n'

    return str_out
    


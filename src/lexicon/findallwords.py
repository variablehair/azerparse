import sqlite3
import sys, os

THIS_PATH = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(THIS_PATH)

conn = sqlite3.connect(THIS_PATH + '/syncat.db')
c = conn.cursor()

import methods_lexicon

def findallwords(string_in):
    """Returns a list of tuples (word, rest) where rest is the remainder of the string passed in"""
    ret = []
    i = 1
    while (i <= len(string_in)):
        test_word = string_in[0:i]
        if methods_lexicon.is_word(test_word):
            ret.append( (test_word, string_in[i:]) )
        i += 1
    return ret
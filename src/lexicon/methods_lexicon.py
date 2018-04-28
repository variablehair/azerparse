"""Contains helper methods pertaining to the lexicon."""
import sys, os

THIS_PATH = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(THIS_PATH)

import sqlite3

conn = sqlite3.connect(THIS_PATH + '/syncat.db')
c = conn.cursor()

def is_word(word):
    """Returns true if the word is in the lexicon."""
    c.execute('''SELECT word FROM syncat WHERE word=?''', (word.upper(),))
    result = c.fetchone()
    return result is not None
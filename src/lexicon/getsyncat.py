import sqlite3

DB_PATH = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(DB_PATH + '/syncat.db')
c = conn.cursor()

SYNCAT_ORDER = {
    0: 'noun',
    1: 'verb',
    2: 'adjective',
    3: 'causverb',
    4: 'passive',
    5: 'reciprocal',
    6: 'reflexive',
    7: 'participle',
    8: 'nominalization',
    9: 'propername'
}

def getsyncat(word):
    """Returns a list of all syntactic categories of the word as strings or an empty list if no results."""
    syncats = ', '.join(list(SYNCAT_ORDER.values()))
    tup = (word,)

    c.execute('''SELECT {0} FROM syncat WHERE word=?'''.format(syncats), tup)
    result = c.fetchone()

    ret = []
    if result is None:
        return ret
    
    for i in range(len(result)):
        if result[i] == 1:
            ret.append(SYNCAT_ORDER[i])
    
    return ret
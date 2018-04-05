import json
import sqlite3
import string

conn = sqlite3.connect('syncat.db')
c = conn.cursor()

with open('syncat.json', encoding='utf-8') as f:
    j = json.load(f)
c.execute('''CREATE TABLE syncat (word TEXT,
                                  noun INTEGER DEFAULT 0,
                                  verb INTEGER DEFAULT 0,
                                  adjective INTEGER DEFAULT 0,
                                  causverb INTEGER DEFAULT 0,
                                  passive INTEGER DEFAULT 0,
                                  reciprocal INTEGER DEFAULT 0,
                                  reflexive INTEGER DEFAULT 0,
                                  participle INTEGER DEFAULT 0,
                                  nominalization INTEGER DEFAULT 0,
                                  propername INTEGER DEFAULT 0)''')
conn.commit()

def pl(wlist):
    punc = ['"', ',', '.', ':', ';']
    ret = set()
    for word in wlist:
        word = word.strip(string.digits)
        if any(p in word for p in punc):
            continue
        if len(word) == 0 and word != 'O':
            continue
        ret.add(word)
    return ret

nounset = pl(j['is.'])
verbset = pl(j['f.'])
adjset = pl(j['sif.'])
causverbset = pl(j['icb.'])
passiveset = pl(j['məch.'])
reciprocalset = pl(j['qarş.'])
reflexiveset = pl(j['qayıd.'])
participleset = pl(j['f.sif.'])
nominalizationset = pl(j['f.is.'] + j['f.is.\n'])
propernameset = pl(j['is.-dən'])

wordset = set.union(nounset, verbset, adjset, causverbset, passiveset, reciprocalset,  reflexiveset, participleset, nominalizationset, propernameset)

def makein(s):
    ret = '''INSERT INTO syncat (word, '''
    pos = 0
    if s in nounset:
        ret += 'noun, '
        pos += 1
    if s in verbset:
        ret += 'verb, '
        pos += 1
    if s in adjset:
        ret += 'adjective, '
        pos += 1
    if s in causverbset:
        ret += 'causverb, '
        pos += 1
    if s in passiveset:
        ret += 'passive, '
        pos += 1
    if s in reciprocalset:
        ret += 'reciprocal, '
        pos += 1
    if s in reflexiveset:
        ret += 'reflexive, '
        pos += 1
    if s in participleset:
        ret += 'participle, '
        pos += 1
    if s in nominalizationset:
        ret += 'nominalization, '
        pos += 1
    if s in propernameset:
        ret += 'propername, '
        pos += 1
    ret = ret[:-2]
    ret += ') VALUES ("{0}", '.format(s)
    i = 0
    while i < pos:
        ret += '1, '
        i += 1
    ret = ret[:-2]
    ret += ')'
    return ret

for word in wordset:
    c.execute(makein(word))

conn.commit()
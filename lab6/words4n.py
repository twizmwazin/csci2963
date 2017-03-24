"""
Words/Ladder Graph
------------------
Generate  an undirected graph over the 5757 5-letter words in the
datafile words_dat.txt.gz.  Two words are connected by an edge
if they differ in one letter, resulting in 14,135 edges. This example
is described in Section 1.1 in Knuth's book [1]_,[2]_.

References
----------
.. [1] Donald E. Knuth,
   "The Stanford GraphBase: A Platform for Combinatorial Computing",
   ACM Press, New York, 1993.
.. [2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html
"""
# Authors: Aric Hagberg (hagberg@lanl.gov),
#          Brendt Wohlberg,
#          hughdbrown@yahoo.com

#    Copyright (C) 2004-2016 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

import networkx as nx

#-------------------------------------------------------------------
#   The Words/Ladder graph of Section 1.1
#-------------------------------------------------------------------


def generate_graph(words):
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    lookup = dict((c, lowercase.index(c)) for c in lowercase)

    def edit_distance_one(word):
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i + 1:]
            j = lookup[c]  # lowercase.index(c)
            for cc in lowercase[j + 1:]:
                yield left + cc + right
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G


def words_graph():
    """Return the words example graph from the Stanford GraphBase"""
    fh = open('words4.dat', 'r')
    words = set()
    for line in fh.readlines():
        # line = line.decode()
        if line.startswith('*'):
            continue
        w = str(line[0:4])
        words.add(w)
    return generate_graph(words)

if __name__ == '__main__':
    from networkx import *
    G = words_graph()

    print "Ajacent words to SLID:"
    try:
        print G.neighbors('slid')
    except:
        print "No neighbors for slid"

    print "Ajacent words to DOTE:"
    try:
        print G.neighbors('dote')
    except:
        print "No neighbors for dote"

    print "Ajacent words to HERD:"
    try:
        print G.neighbors('herd')
    except:
        print "No neighbors for herd"

    print "Ajacent words to OMEN:"
    try:
        print G.neighbors('omen')
    except:
        print "No neighbors for omen"

    print "Ajacent words to NINE:"
    try:
        print G.neighbors('nine')
    except:
        print "No neighbors for nine"

    print "Ajacent words to SELL:"
    try:
        print G.neighbors('sell')
    except:
        print "No neighbors for sell"

    print "Ajacent words to STAT:"
    try:
        print G.neighbors('stat')
    except:
        print "No neighbors for stat"

    print "Ajacent words to WHAT:"
    try:
        print G.neighbors('what')
    except:
        print "No neighbors for what"

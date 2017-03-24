"""
SGBWords() returns an undirected graph over the 5757 5-letter
words in the datafile words_dat.txt.  Two words are connected by an edge
if they differ in one letter, resulting in 14,135 edges. This example
is described in Section 1.1 in Knuth's book [1,2].

References.
----------

[1] Donald E. Knuth,
    "The Stanford GraphBase: A Platform for Combinatorial Computing",
    ACM Press, New York, 1993.
[2] http://www-cs-faculty.stanford.edu/~knuth/sgb.html

"""

__author__ = """Brendt Wohlberg\nAric Hagberg (hagberg@lanl.gov)"""
__date__ = "$Date: 2005-04-01 07:56:04 -0700 (Fri, 01 Apr 2005) $"
__credits__ = """"""
__revision__ = ""
#    Copyright (C) 2004 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

from networkx import *
import re
import sys

__author__ = """"""
__date__ = ""
__credits__ = """"""
__version__ = ""
# $Header$


#-------------------------------------------------------------------
#   The Words/Ladder graph of Section 1.1
#-------------------------------------------------------------------

def _notComment(line):
    return not(line.startswith('*'))


def _wdist(a, b):
    """ Return simple edit distance between two words a and b. """

    d = abs(len(a) - len(b))
    a1 = list(a)
    b1 = list(b)
    for k in range(min(len(a), len(b))):
        if a[k] in b1:
            b1.remove(a1[k])
        else:
            d = d + 1
    return d


def words_graph():
    """ Return the words example graph from the Stanford GraphBase"""

    import sys
    # open file words_dat.txt.gz (or words_dat.txt)
    try:
        try:
            import gzip
            fh = gzip.open('words_dat.txt.gz', 'r')
        except:
            fh = open("words_dat.txt", "r")
    except IOError:
        raise "File words_dat.txt not found."

    G = Graph(name="words")
    sys.stderr.write("Loading words_dat.txt: ")
    for line in fh.readlines():
        if line.startswith("*"):
            continue
        w = line[0:5]
        G.add_node(w)
    nwords = number_of_nodes(G)
    words = G.nodes()
    for k in xrange(0, nwords):
        if (k % 100 == 0):
            sys.stderr.softspace = 0
            sys.stderr.write(".")
        for l in xrange(k + 1, nwords):
            if _wdist(words[k], words[l]) == 1:
                G.add_edge(words[k], words[l])
    return G

if __name__ == '__main__':
    from networkx import *
    G = words_graph()
    print "Loaded words_dat.txt containing 5757 five-letter English words."
    print "Two words are connected if they differ in one letter."
    print "graph has %d nodes with %d edges"\
          % (number_of_nodes(G), number_of_edges(G))

    print "Ajacent words to SLID:"
    print G.neighbors('slid')

    print "Ajacent words to DOTE:"
    print G.neighbors('DOTE')

    print "Ajacent words to HERD:"
    print G.neighbors('HERD')

    print "Ajacent words to OMEN:"
    print G.neighbors('OMEN')

    print "Ajacent words to NINE:"
    print G.neighbors('NINE')

    print "Ajacent words to SELL:"
    print G.neighbors('SELL')

    print "Ajacent words to STAT:"
    print G.neighbors('STAT')

    print "Ajacent words to WHAT:"
    print G.neighbors('WHAT')

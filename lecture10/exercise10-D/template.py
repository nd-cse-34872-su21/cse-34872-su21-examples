#!/usr/bin/env python3

import collections
import heapq
import sys

# Build Graph

def read_graph():
    ''' Read in undirected graph '''
    g = collections.defaultdict(dict)
    for line in sys.stdin:
        source, target, weight = line.split()
        g[source][target] = int(weight)
        g[target][source] = int(weight)
    return g

# Compute MST

def compute_mst(g):
    return visited

# Main Execution

def main():
    # Read Graph
    g = read_graph()

    # Compute MST
    m = compute_mst(g)

    # Print edges
    e = sorted((min(s, t), max(s, t)) for s, t in m.items() if s != t)
    print(sum(g[s][t] for s, t in e))
    for s, t in e:
        print(s, t)

if __name__ == '__main__':
    main()

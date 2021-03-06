#!/usr/bin/env python3

import sys

# Functions

def read_numbers():
    try:
        n = int(sys.stdin.readline())
        k = int(sys.stdin.readline())
        v = [int(sys.stdin.readline()) for _ in range(n)]
    except ValueError:
        return 0, 0, None

    return n, k, v

def compute_unfairness(n, k, v):
    # TODO: Compute minimum unfairness
    return 0

# Main execution

def main():
    n, k, v = read_numbers()
    while n: 
        print(compute_unfairness(n, k, v))
        n, k, v = read_numbers()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys

################################################################################

def sortBibEntries(bibFilePath): # prints sorted entries to stdout
    entries = {} # entryLabel |-> entryLines

    lines = [line.strip() for line in open(bibFilePath)]
    lines = [line for line in lines if line and line[0] != '%']
    for line in lines:
        if line[0] == '@':
            entryLabel = line.split('{')[1][:-1]
            entries[entryLabel] = [line]
            entryLines = entries[entryLabel]
        else:
            entryLines.append(line)

    for entryLabel in sorted(entries):
        entryLines = entries[entryLabel]
        print('\n  '.join(entryLines[:-1]))
        print(entryLines[-1])
        print()

################################################################################

if __name__ == '__main__':
    sortBibEntries(sys.argv[1])

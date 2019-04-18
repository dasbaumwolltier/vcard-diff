#!/usr/bin/env python3

import sys
import vobject

def main(args: list) -> int:
    if len(args) < 4:
        print("Too few arguments: diff.py [File A] [File B] [Output File]")
        return -1

    first = list()
    second = list()

    with open(args[1]) as filea:
        first = [x for x in vobject.readComponents(filea, validate=True)]

    with open(args[2]) as fileb:
        second = [x.fn for x in vobject.readComponents(fileb, validate=True)]

    with open(args[3], 'w') as file:
        for card in first:
            if not card.fn in second:
                file.write(card.serialize())


main(sys.argv)
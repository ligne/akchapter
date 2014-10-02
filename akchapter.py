#!/usr/bin/python

"""
Generates the index.

"""

import sys, os
import re
import json


def makedata(file, date):
        """ Calculates the number of chapters in each book from the html file
        $file, as well as the start date, and writes them to a file called
        'wp.idx'.
        """

        with open(file, 'r') as book:
                bre = re.compile(r'<span>PART (\w+)')
                cre = re.compile(r'<span>Chapter (\d+)')

                bname = cname = None
                a = []

                for line in book:
                        # look for books first
                        m = bre.search(line)
                        if m:
                                book = m.group(1).lower()
                                continue

                        # now look at chapters
                        m = cre.search(line)
                        if m:
                                a.append('Part {0}, chapter {1}'.format(book, m.group(1)))

        with open('wp.idx', 'w') as f:
                f.write('var wp = ')
                json.dump({ 'date': date.split('-', 3), 'chapters': a }, f)


if __name__ == '__main__':
        # get into the same dir as the script
        os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
        makedata(sys.argv[1], sys.argv[2])


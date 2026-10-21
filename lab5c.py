#!/usr/bin/env python3
# Author: Melissa Aydin
# Date: Oct 21
# Purpose: Process File data and count words
with open("rhyme.txt", "w") as dataFile:
    dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")
f = open("rhyme.txt", "r")
line = f.readline()
while line:
    clean_line = line.strip()
    no_dot_line = clean_line.strip('.')
    words = no_dot_line.split()
    print(f"{clean_line} --- {len(words)} words")
    line = f.readline()
f.close()

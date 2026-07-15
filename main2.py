# A Python program called notebook-merger.py that works with two subject note files. 
# PART 1 uses with open() as f: to read and print science-notes.txt automatically closing the file. 
# PART 2 reads maths-notes.txt line by line, calls split() on each line, and prints how many words each line has. 
# PART 3 uses os.path.exists() to check for all-notes.txt, then merges both note files into it. 
# PART 4 checks if all-notes.txt exists using os.path.exists() and deletes it with os.remove(). 
# Three files are needed — science-notes.txt and maths-notes.txt (given to students) and notebook-merger.py 
# (built during the activity).

import os

totalWords = 0

if os.path.exists("class-notes.txt"):
    with open("class-notes.txt", "r") as f:
        for i in f:
            words = i.split()
            totalWords += len(words)

print(totalWords)
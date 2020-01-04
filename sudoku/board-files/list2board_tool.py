"""
list2board_tool.py

This script is used to convert a python list to a board file.
Just chose a filename, paste the list-version of the board to where the placeholder is, then run the script.

author: Wiley Matthews
"""

filename = 'YOUR FILE NAME HERE'  # New file name
board = [  # Board as list
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

with open(filename, 'w') as f:
    for row in board:
        f.write(' '.join(row) + '\n')
# End

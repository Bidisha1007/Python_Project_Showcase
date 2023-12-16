
'''Regular expressions (regex) are powerful tools for searching and manipulating text in Python. They allow you to define patterns of characters that you want to find, match, or replace in strings. A valid regex, or regular expression, is one that follows the grammar and syntax of the specific regex engine you're using. In Python, it refers to a pattern defined using the re module that successfully matches the desired text in a string.'''

#CODE:
import re
T = int(input())
for _ in range(T):
    try:
        re.compile(input())
        print(True)
    except Exception:
        print(False)
        
import re
import sys



TOKENS = r"""
    (?P<space>\s+)
    |(?P<comment>\#.*)
    |(?P<var>\?\w+)
    |(?P<lan>@[a-z]{2,})
    |(?P<string>"[^"]*")
    |(?P<decimal>[{}.])
    |(?P<number>\d+\b)
    |(?P<word>\w+(?:\w+)?)
    |(?P<error>,)
"""

reserved = ['LIMIT']




def lexer(text):
    for m in re.finditer(TOKENS, text, re.VERBOSE):
        kind = m.lastgroup
        value = m.group()

        if kind in ('space', 'comment'):
            continue
        elif kind == 'word':
            kind == 'reserved' if value in reserved else 'concept'
        elif kind == 'error':
            line = text.cont('\n', 0 , m.start())+1
            print(f'{kind:<9} {value!r} (line {line})')
        else:
            print(f'{kind:<9} {value}')



if __name__ == '__main__':
    if len(sys.argv) > 1:                     # calling
        text = open(sys.argv[1], encoding='utf-8').read()
    else:                                     # pipe, or press Ctrl-D
        if sys.stdin.isatty():
            print('just write whatever bro and end it with Ctrl-D:')
        text = sys.stdin.read()
    lexer(text)
















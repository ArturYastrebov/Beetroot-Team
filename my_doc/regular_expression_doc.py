import re

# text = "[apple] [banana] [cherry] [date]"
# pattern = r"\[(.*?)\]"
#
# matches = re.findall(pattern, text)
# print(matches) # prints ['apple', 'banana', 'cherry', 'date']


# string = "The quick brown fox jumps over the lazy dog."
# # match any word followed by the word 'fox'
# pattern = r'\b(?:\w+) fox\b'
# # search for the pattern in the string
# match = re.search(pattern, string)
#
# if match:
#     print(match.group(0))
# else:
#     print("No match found.")

# Flags
import re

text = "The quick brown Fox jumps over the lazy DOG."
pattern = re.compile("fox", re.IGNORECASE)
result = pattern.findall(text)

print(result)
# re.IGNORECASE or re.I
# re.ASCII or  re.A
# re.MULTILINE or re.M
# re.DOTALL or re.S
# re.VERBOSE or re.X

my_string = "hello, 你好, ¡hola!"

# Match only ASCII letters and punctuation
pattern = re.compile(r'[.*\s]+', flags=re.ASCII)
matches = pattern.findall(my_string)

print(matches)  # Output: ['hello,', ',!']

my_string = "Line 1\nLine 2\nLine 3\n"

# Match the beginning of each line
pattern = re.compile(r'Line \d.*', flags=re.DOTALL)
matches = pattern.findall(my_string)

print(matches)  # Output: ['Line', 'Line', 'Line']

a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

# Functions

# re.compile(pattern, flags=0) - save pattern on re object. whan will be used again
# prog = re.compile(pattern)
# result = prog.match(string)
# is equivalent to # result = re.match(pattern, string)

# re.search(pattern, string, flags=0) - search on hole string
# re.match(pattern, string, flags=0) - start search on first letter
# re.fullmatch(pattern, string, flags=0) - If the whole string matches, return a corresponding match object.
# re.split(pattern, string, maxsplit=0, flags=0) - split string for pattern

# re.findall(pattern, string, flags= - return all matches.

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']
re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
# [('width', '20'), ('height', '10')]

# re.finditer(pattern, string, flags=0) - create iterator

# re.sub(pattern, repl, string, count=0, flags=0)
# new_string = re.sub(pattern, repl, string, count=0, flags=0) - to replace all occurrences of the pattern with a new string
# re.subn(pattern, repl, string, count=0, flags=0)
# new_string, count = re.subn(pattern, repl, string, count=0, flags=0) - to replace all occurrences of the pattern with a new string and count the number of replacements

# re.escape(pattern) - Escape special characters in pattern.
# re.purge() - Clear the regular expression cache.

text = 'Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.'
pattern = r'pattern'
res = re.finditer(pattern, text)
print([i.group() for i in res])

res_pos = re.search(pattern, text, )
print(res_pos.endpos)
# Match Objects
# Match.expand(template) -> can return numeric backreferences (\1, \2) and named backreferences (\g<1>, \g<name>)
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# m.group(0)       # The entire match  -> # 'Isaac Newton'
# m.group(1)       # The first parenthesized subgroup. ->  # 'Isaac'
# m.group(2)       # The second parenthesized subgroup. ->  # 'Newton'
# m.group(1, 2)    # Multiple arguments give us a tuple. ->  # ('Isaac', 'Newton')

# Match.groups(default=None)

# Match.groupdict(default=None)
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}

text_my = "Isaac Newton, physicist"
prog = re.compile(r'a')
print(prog.findall(text_my, 3))
print(prog.findall(text_my, 10))

# Match.groupdict(default=None) return dict
# Match.start([group])
# Match.end([group])
# Match.span([group])
# Match.pos
# Match.endpos
# Match.lastindex
# Match.lastgroup
# Match.re
# Match.string
pattern = r'\d([A-Z][a-z]+)([A-Z][a-z]+)'
line = '1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'
result = re.findall(pattern, line)
print(result)



my_dict = {
    'w': {'p', 'h', 'i', 's', 'u', 'a'},
    'h': {'t', 'p', 'i', 's', 'u', 'a'},
    'a': {'t', 'p', 'i', 's', 'u'},
    'u': {'p'},
    't': {'p', 'i', 's', 'u'},
    'p': set(),
    'i': {'s', 'u'},
    's': {'p', 'u'}}

print(''.join([k for k, v in sorted(my_dict.items(), key=lambda x: len(x[1]), reverse=True)]))
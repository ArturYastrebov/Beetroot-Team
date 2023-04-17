import itertools

# Infinite iterators:
iterobj_1 = itertools.count(-10, 2)  # -> count from -10, step 2
# -10, -8, -6, -4, -2, 0, 2, 4, 6...Infinite

iterobj_2 = itertools.cycle(("ABC", {'2': 2, '4': 5}))  # -> return one letter after another on cycle
# 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'...Infinite

iterobj_3 = itertools.repeat(33, 5)  # -> repeat infinite or up to n times

# Terminating iterators:
my_list = [1, 3, 5, 10, 12, 5, 1, 0]
iterobj_4 = itertools.accumulate(my_list, lambda a, b: a * b, initial=2)
# print(list(iterobj_4)) -> [1, 4, 9, 19]

iterobj_5 = itertools.chain('ABC', 'DEF', {'key1': 1, 'key2': 2, 'key3': 6}, 'Hello', '1')  # -> take *iterables obj
iterobj_6 = itertools.chain.from_iterable(
    ['ABC', 'DEF', {'key1': 1, 'key2': 2, 'key3': 6}, 'Hello', '1'])  # -> take one iterable obj
# print(list(iterobj_5)) -> ['A', 'B', 'C', 'D', 'E', 'F', 'key1', 'key2', 'key3', 'H', 'e', 'l', 'l', 'o', '1']
# print(list(iterobj_6)) -> ['A', 'B', 'C', 'D', 'E', 'F', 'key1', 'key2', 'key3', 'H', 'e', 'l', 'l', 'o', '1']

# my_list = [1, 3, 5, 10, 12, 5, 1, 0]
iterobj_7 = itertools.compress(my_list, ['HeLlo', 'd', 0, 1])  # take iterable_obj, selector like [*Bool_obj_convert]
list(iterobj_7)  # -> [1, 3, 10]   selector = (d[0] if s[0]), (d[1] if s[1])...

iterobj_8 = itertools.dropwhile(lambda x: x < 5, my_list)
list(iterobj_8)  # -> [5, 10, 12, 5, 1, 0] start get than funk false

iterobj_9 = itertools.filterfalse(lambda x: x % 2, my_list)
list(iterobj_9)  # -> [10, 12, 0] get data than filter is true

iterobj_10 = itertools.groupby('AAABBBCCDDDDDD', key=lambda x: x)

data = [
    ('apple', 1),
    ('orange', 2),
    ('apple', 3),
    ('banana', 4),
    ('banana', 5),
    ('orange', 6),
    ('apple', 7),
    ('orange', 8),
    ('banana', 9),
]


def get_fruit(item):
    return item[0]


# for i, j in itertools.groupby(data, get_fruit):
#     print(i)
#     print(list(j))
# print([list(g) for k, g in itertools.groupby('AAAABBBCCDAAAaa')])


# my_list = [1, 3, 5, 10, 12, 5, 1, 0]
list(itertools.islice(my_list, 3, None, 2))  # -> [10, 5, 0]
# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop[, step])

list(itertools.pairwise(my_list))
# [(1, 3), (3, 5), (5, 10), (10, 12), (12, 5), (5, 1), (1, 0)]

my_list2 = ('A', 'B', 'C')  # кожен з кожним
print(list(itertools.permutations(
    my_list2)))  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(list(
    itertools.permutations(my_list2, 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(list(itertools.permutations(my_list2,
                                  3)))  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

list(itertools.product(("RE"), ('AS'),
                       repeat=2))  # -> [('A', 'N'), ('A', 'I'), ('A', 'D'), ('B', 'N'), ('B', 'I'), ('B', 'D'), ('D', 'N'), ('D', 'I'), ('D', 'D')]
# the same itertools.product(A, B) -> ((x,y) for x in A for y in B).
colors = ['red', 'green', 'blue']
materials = ['cotton', 'wool', 'polyester']
print(list(itertools.product(colors, materials)))  # кожен з кожними без повторення

# itertools.starmap(function, iterable)
data_tuple = ((3, 4), (1, 2), (5, 2))
print(list(itertools.starmap(lambda x, y: x * y, data_tuple)))  # -> [12, 2, 10]

# my_list = [1, 3, 5, 10, 12, 5, 1, 0]
iterobj_11 = itertools.takewhile(lambda x: x < 5, my_list)
print(list(iterobj_11))  # -> [1, 3] take while func false

iter_obj_colors1, iter_obj_colors2, iter_obj_colors3, iter_obj_colors4, iter_obj_colors5 = itertools.tee(colors, 5)
# print(next(iter_obj_colors1)) create independence iterators object
# print(next(iter_obj_colors1))
# print(next(iter_obj_colors2))
# print(next(iter_obj_colors1))
# print(next(iter_obj_colors3))
# print(list(iter_obj_colors2))
# print(list(iter_obj_colors3))
# print(list(iter_obj_colors4))
# print(list(iter_obj_colors5))

print(list(itertools.zip_longest(colors, data, fillvalue='-')))

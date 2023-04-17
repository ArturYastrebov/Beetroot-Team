import itertools

# Infinite iterators
itertools.count(5, 5)  # count(start, [step]): iterator object -> 5, 10, 15, 20, 25, 30...
itertools.cycle('AB')  # cycle(iterable): iterator object -> 'A', 'B', 'A', 'B', 'A', 'B'...
itertools.repeat(234)  # repeat(val, num): iterator object -> 234, 234, 234, 234, 234

# Combinatoric iterators
data_letter = ('A', 'B', 'C')
itertools.product(data_letter, repeat=2)  # product(p, q, … [repeat=1]):
# ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')
itertools.permutations(data_letter, 2)  # permutations(p[, r]):
# ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
itertools.combinations(data_letter, 2)  # combinations(p, r):
# ('A', 'B'), ('A', 'C'), ('B', 'C')
itertools.combinations_with_replacement(data_letter, 2)  # combinations_with_replacement(p, r):
# ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')

# Terminating iterators
itertools.accumulate((1, 2, 3, 4, 5))  # -> 1, 3, 6, 10, 15
# accumulate(iterable[, func, *, initial=None])
itertools.chain([1, 2, 4], [2, 5, 3], [6, 6, 6])  # chain(*iterable_obj)-> 1, 2, 4, 2, 5, 3, 6, 6, 6
itertools.chain.from_iterable([(1, 2, 4), {2, 5, 3}, "666"])  # chain.from_iterable([*iterable_obj])
# -> 1, 2, 4, 2, 3, 5, '6', '6', '6'
itertools.compress('ABCDEFG', [1, 1, 0, 1, 0, 4, 0, 23, 1, 0])  # compress(iter, selector):
# -> 'A', 'B', 'D', 'F'
itertools.dropwhile(lambda x: x != 'C', 'ABCDEFG')  # dropwhile(func, iterable):
# -> 'C', 'D', 'E', 'F', 'G'
itertools.filterfalse(lambda x: x not in ['C', 'D', 'I', 'L'], 'ABCDEFG')  # filterfalse(func, iterable)
# -> 'C', 'D'
itertools.islice('ABCDEFG', 4)  # -> 'A', 'B', 'C', 'D'
# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop[, step])
itertools.starmap(lambda a, b, c: a - b + c, [[1, 2, 3], (3, 4, 5), (23, 2, 12)])  # -> 2, 4, 33
# itertools.starmap(function, iterable)
itertools.takewhile(lambda x: x != 'C', 'ABCDEFG')  # takewhile(func, iterable): -> 'A', 'B'
# itertools.takewhile(predicate, iterable)
iter_obj1, iter_obj2 = itertools.tee([1, 2, 3, 4, 5])
list(iter_obj1)  # -> 1, 2, 3, 4, 5
list(iter_obj2)  # -> 1, 2, 3, 4, 5
# itertools.tee(iterable, n=2)
itertools.zip_longest(('A', 'B', 'C'), (1, 5, 6, 2),
                      fillvalue='my_val')  # -> ('A', 1), ('B', 5), ('C', 6), ('my_val', 2)
# zip_longest( iterable1, iterable2, fillvalue=None)
for group_name, iter_obj in itertools.groupby('AAACCBBC'):
    print(group_name, end=' ')
    print(list(iter_obj))

# A ['A', 'A', 'A']
# C ['C', 'C']
# B ['B', 'B']
# C ['C']

itertools.pairwise('iterable')
#  -> ('i', 't'), ('t', 'e'), ('e', 'r'), ('r', 'a'), ('a', 'b'), ('b', 'l'), ('l', 'e')

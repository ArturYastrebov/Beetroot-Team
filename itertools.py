import itertools

# permutations - всі елеменети унікальні, на основі їх позиції, а не значення
# функція приймає iter_obj та group_size, ітерований обєкт та кількість елементів в групі.
# якщо group_size не вказано або None то значення дорівнює len(iter_obj).

print(list(itertools.permutations("abb")))
# [('a', 'b', 'b'), ('a', 'b', 'b'), ('b', 'a', 'b'),
# ('b', 'b', 'a'), ('b', 'a', 'b'), ('b', 'b', 'a')]

triplets = [['a', 'd', 'b'], 'a', 'd', {'f', 's'}]
print(list(itertools.chain.from_iterable(triplets)))

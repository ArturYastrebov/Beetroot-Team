import datetime


def decor(func):
    def inner(*args, **kwargs):
        start_time = datetime.datetime.now()
        res = func(*args, **kwargs)
        end_time = datetime.datetime.now() - start_time
        return end_time.microseconds, res

    return inner


@decor
def sum_num(a, b):
    return a + b


#
# print(sum_num(1, 2))


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


dima = Person(1, 'Dima')


# print(hash('45743573745634572457246'))

def has_hash(obj):
    return hasattr(obj, '__hash__')


# print(has_hash(Person))

# my_dict = {'a': 2, 'b': 12, 'c': 4, 'd': 11}
# a = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:2]
# print([i for i, j in sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:2]])

def chess_board(a: int, b: int) -> int:
    # my_list = [i for i in range(a*b) if i % 2 == 0]
    # return len(my_list)
    return (a * b % 2) + ((a * b) // 2)


print(chess_board(3, 3))

numbers = [1, 2, 3, 4, 5]

squared_numbers = (number ** 2 for number in numbers)
print(next(squared_numbers))

print(type(squared_numbers))  # <class 'generator'>
print(squared_numbers)  # <generator object <genexpr> at 0x7f1883346880>
print(list(squared_numbers))  # [1, 4, 9, 16, 25]
print(list(squared_numbers))  # []

squared_numbers = (number ** 2 for number in numbers)
print(4 in squared_numbers)  # True
print(4 in squared_numbers)  # False

set_of_numbers = {1, 2, 3}
list_of_numbers = [1, 2, 3]
string_of_numbers = '123'

iterator_A = iter(string_of_numbers)
iterator_B = iter(string_of_numbers)


# print(next(iterator_A))
# print(next(iterator_B))
#
# print(next(iterator_A))
# print(next(iterator_B))

class MyIterator:

    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number ** 2


class MyIter:

    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = 0

    def __next__(self):
        try:
            num = self.iter_obj[self.index]
        except IndexError:
            pass
        else:
            return num
        finally:
            self.index += 1

    def __iter__(self):
        return self


my_iter = MyIter(numbers)

fruits_amount = {'apples': 2, 'bananas': 5}

# x, y = fruits_amount
# print(x, y)
# x, y = fruits_amount
# print(x, y)


class MyIt(list):
    pass


my = MyIt([1, 2, 3])

print(my is [1, 2, 3])
print(my == [1, 2, 3])
# for item in my:
#     print(item)

vedeo_lesson = 'https://www.youtube.com/watch?v=oz_SsZuAtS4'


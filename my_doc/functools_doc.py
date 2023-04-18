from functools import *


partial
# partial(func, /, *args, **keywords)
# def power(a, b):
#     return a ** b
#
#
# # partial functions
# pow2 = partial(power, b=2)
# pow4 = partial(power, b=4)
# power_of_5 = partial(power, 5)
#
# print(power(2, 3))
# print(pow2(4))
# print(pow4(3))
# print(power_of_5(2))
#
# print('Function used in partial function pow2 :', pow2.func)
# print('Default keywords for pow2 :', pow2.keywords)
# print('Default arguments for power_of_5 :', power_of_5.args)


Partialmethod
# partialmethod(func, *args, **keywords)
# class Demo:
#     def __init__(self):
#         self.color = 'black'
#
#     def _color(self, type):
#         self.color = type
#
#     set_red = partialmethod(_color, type='red')
#     set_blue = partialmethod(_color, type='blue')
#     set_green = partialmethod(_color, type='green')
#
#
# obj = Demo()
# print(obj.color)
# obj.set_blue()
# print(obj.color)

Cmp_to_key
# function(iterable, key=cmp_to_key(cmp_function))
# Cmp_to_key It converts a comparison function into a key function.
# The comparison function must return 1, -1 and 0 for different conditions.
# It can be used in key functions such as sorted(), min(), max().

reduce(function, sequence[, initial]) -> value
# It applies a function of two arguments repeatedly on the elements of a sequence
# so as to reduce the sequence to a single value.
# For example, reduce(lambda x, y: x^y, [1, 2, 3, 4])# calculates (((1^2)^3)^4).
# If the initial is present, it is placed first in the calculation, and the
# default result is when the sequence is empty.

@total_ordering
# -> It is a class decorator that fills in the missing
# comparison methods (__lt__, __gt__, __eq__, __le__, __ge__).


update_wrapper() # -> The same like @wraps but used for function.
# save f.__name__ and f.__doc__ like func without partial method.
# If a class is given which defines one or more comparison methods,
# “@total_ordering” automatically supplies the rest as per the given definitions.
# However, the class must define one of __lt__(), __le__(), __gt__(), or __ge__() and additionally,
# the class should supply an __eq__() method.

# def power(a, b):
#     ''' a to the power b'''
#     return a ** b
#
#
# # partial function
# pow2 = partial(power, b=2)
# pow2.__doc__ = '''a to the power 2'''
# pow2.__name__ = 'pow2'
#
# print('Before wrapper update -')
# print('Documentation of pow2 :', pow2.__doc__)
# print('Name of pow2 :', pow2.__name__)
# print()
# update_wrapper(pow2, power)
# print('After wrapper update -')
# print('Documentation of pow2 :', pow2.__doc__)
# print('Name of pow2 :', pow2.__name__)

@wraps(f) # It is a function decorator which applies update_wrapper() to the decorated function.
# The func wich decorate has the same f.__name__ and f.__doc__ like func without decorator

@lru_cache
# lru_cache -> cache is a function decorator used for saving up to the maxsize most recent calls of a function.
# This can save time and memory in case of repeated calls with the same arguments.
# @lru_cache(maxsize=128, typed=False)

@singledispatch
# @singledispatch -> func can have different behaviors depending upon the type of its first argument.

# @singledispatch
# def fun(s):
#     print(s)
#
#
# @fun.register(int)
# def _(s):
#     print(s * 2)
#
#
# fun('GeeksforGeeks')
# fun(10)
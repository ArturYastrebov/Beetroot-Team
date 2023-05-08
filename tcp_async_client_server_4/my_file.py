from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class Person:
    name: str = field(hash=True)
    age: int = field(hash=False)



vasya = Person('vasya', 20)
print(hash(vasya))
vasya2 = Person('vasya', 10)
print(hash(vasya2))


# class Num:
#
#     def __init__(self, num):
#         self.num = num
#
#     def __eq__(self, other):
#         if isinstance(other, Num):
#             return self.num == other.num
#         else:
#             raise TypeError
#
# num1 = Num(1)
# num2 = Num(1)
#
# print(num1 == num2)

from functools import wraps, cached_property


def decorator2(a):
    def decorator(func):
        def wraper(*args,**kwargs):
            print(a)
            res = func(*args,**kwargs)
            print('2')
            return res
        return wraper
    return decorator

@decorator2(7777)
def my_sum(a,b):
    return a+b


# print(my_sum(1, 2))

class A:
    @cached_property
    def gen(self):
        for i in range(10):
            a = yield i
            print(a)

a = A()

# g = gen(10)
# print(next(a.gen))
# print(a.gen.send(5))
# print(next(a.gen))
# print(next(a.gen))
# print(a.gen.send(5))
# print(next(a.gen))
# print(next(a.gen))
# print(next(a.gen))
# print(next(a.gen))

def another_dec(*args2, **kwargs2):
    def my_dec(func):
        @wraps(func)
        def inner(*args, **kwargs):
           print(*args2, **kwargs2)
           res = func(*args, **kwargs)
           print('before')
           return res
        return inner
    return my_dec

@another_dec(44,12,213,'asda')
def fun_func(a,b):
    return a+b

print(fun_func(1,2))
print(fun_func.__str__())

class MyIterrator():
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val

it = MyIterrator([1,2,3,4,5,6])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))






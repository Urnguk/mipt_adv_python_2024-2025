# class MyList:
#     def __init__(self):
#         self._data = []
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     def __setitem__(self, item, value):
#         self._data[item] = value
#
#     def append(self, value):
#         self._data.append(value)
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         return MyListIter(self)
#
#
# class MyListIter:
#     def __init__(self, origin):
#         self._origin = origin
#         self._i = -1
#
#     def __next__(self):
#         self._i += 1
#         if self._i == len(self._origin):
#             raise StopIteration
#         return self._origin[self._i]


# A = MyList()
# for i in range(10):
#     A.append(i ** 2)
# it = iter(A)
# print(it)
#
# try:
#     while True:
#         print(next(it))
# except StopIteration:
#     pass
#
# for i in A:
#     print(i)

# a = range(2, 5, 2)
#
# it = iter(a)
#
# print(next(it))
# print(next(it))

# def MyRange(start, stop=None, step=1):
#     if stop is None:
#         start, stop = 0, start
#     curr = start
#     # return
#     while curr < stop:
#         yield curr
#         curr += step
#
#
# for i in MyRange(2, 7, 2):
#     print(i)

# A = [0, 5, 3, 2, 8]
# B = (x ** 2 for x in A)
# print(B)
# import time
#
#
# def time_decorator(func):
#     def wrapped_func(*args):
#         start_time = time.time()
#         res = func(*args)
#         stop_time = time.time()
#         return res, stop_time - start_time
#
#     return wrapped_func
#
#
# @time_decorator
# def fib(n):
#     a, b = 1, 1
#     for i in range(n - 1):
#         a, b = b, a + b
#     return b


# print(fib(12000))

from functools import cache
from functools import lru_cache



# @lru_cache(maxsize=120)
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(120))


# class A:
#     def __init__(self, x):
#         self._x = x
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, x):
#         if x > 1000:
#             raise ValueError("do not accept values above 1000")
#         self._x = x
#
#
# a = A(0)
# print(a.x)
# a.x = 7
# print(a.x)
# a.x = 1001

# class Vector_3D:
#     def __init__(self, x=0, y=0, z=0):
#         self._x = x
#         self._y = y
#         self._z = z
#
#     @classmethod
#     def init_from_tuple(cls, t):
#         return cls(*t)
#
#     def get_pos(self):
#         return self._x, self._y, self._z
#
#     def __add__(self, other):
#         if isinstance(other, Vector_3D):
#             x, y, z = other.get_pos()
#             return Vector_3D(self._x + x, self._y + y, self._z + z)
#         else:
#             return Vector_3D(self._x + other, self._y + other, self._z + other)
#
#     def __radd__(self, other):
#         return self + other
#
#     # def __eq__(self, other):
#     #     return other == None
#
#     def __str__(self):
#         return "Vector_3D: (" + "; ".join((str(a) for a in self.get_pos())) + ")"
#
#     @staticmethod
#     def dist(a, b):
#         x1, y1, z1 = a.get_pos()
#         x2, y2, z2 = b.get_pos()
#         return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
#
#
#
# a = Vector_3D(0, 0, 7)
# b = Vector_3D(8, 2)
#
#
# def dist(a, b):
#     x1, y1, z1 = a.get_pos()
#     x2, y2, z2 = b.get_pos()
#     return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
#
#
# print(dist(a, b))
# print(Vector_3D.dist(a, b))
# c = Vector_3D.init_from_tuple((4, 6, 8))
# print(c.get_pos())


# f = open("test.txt", mode="rt")
# f.readline()
# for line in f:
#     print(line.strip())
# f.close()

# with open("test.txt") as f:
#     for line in f:
#         print(line.strip())
#

# class X:
#     def __enter__(self):
#         return 5
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("I'm closed!")
#
#
# with X() as f:
#     raise ValueError
#     print(f)


class Vector_3D:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def init_from_tuple(cls, t):
        return cls(*t)

    def get_pos(self):
        return self._x, self._y, self._z

    def __add__(self, other):
        if isinstance(other, Vector_3D):
            x, y, z = other.get_pos()
            return Vector_3D(self._x + x, self._y + y, self._z + z)
        else:
            return Vector_3D(self._x + other, self._y + other, self._z + other)

    def __radd__(self, other):
        return self + other

    # def __eq__(self, other):
    #     return other == None

    def __str__(self):
        return "Vector_3D: (" + "; ".join((str(a) for a in self.get_pos())) + ")"

    @staticmethod
    def dist(a, b):
        x1, y1, z1 = a.get_pos()
        x2, y2, z2 = b.get_pos()
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5



import pickle

# A = Vector_3D(5, 6, 2)
# d = A.__getstate__()
# with open("my_data.bin", mode ='wb') as f:
#     pickle.dump(d, f)

with open("my_data.bin", mode="rb") as f:
    d = pickle.load(f)

B = Vector_3D()
B.__dict__ = d
print(B)






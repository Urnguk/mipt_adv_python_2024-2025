# class X:
#     def __init__(self):
#         pass
#
#     def __len__(self):
#         return 3
#
#
# print(len(X()))

# class Vector_3D:
#     def __init__(self, x=0, y=0, z=0):
#         self._x = x
#         self._y = y
#         self._z = z
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
#
# A = Vector_3D(5, 3)
# B = Vector_3D(1, 1, 1)
# print(A + B)
# print(A + 2)
# print(2 + A)

# x = None
# if x == None:
#     print("yay!")


# print(A == None, A is None)
# print(type(None))


# class Character:
#     pass
#
# class Combat(Character):
#     def __init__(self, health, damage):
#         self._h = health
#         self._d = damage
#
#     def hit(self, damage):
#         self._h -= damage
#
#     def check_alive(self):
#         return self._h > 0
#
#
# class MainCharacter(Combat):
#     def __init__(self, health, damage, armor):
#         super().__init__(health, damage)
#         self._a = armor
#
#     def hit(self, damage):
#         self._h -= int(damage * (1 - self._a / 10))
#
#
# T = MainCharacter(10, 5, 1)
# print(T.check_alive())


# def func(x):
#     x.hit()
#
# # print(5 / 0)
# print(func(2))
# print(int("abc"))

# class MyExcepetion(ArithmeticError):
#     pass
#
#
# def func():
#     raise MyExcepetion("some text")
#
#
# func()

def func():
    raise IndentationError
try:
    try:
        func()
    except ArithmeticError:
        print("don't make silly mistakes")
    except ValueError:
        print("type correctly")
    else:
        print("all right")
    finally:
        print("see you")
except IndexError:
    print("wrong index")





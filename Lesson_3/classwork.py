# class Student:
#     x = 10
#
#
# A = Student()
# B = Student()
#
# print(A.x, B.x, Student.x)
#
# A.x = 3
# print(A.x, B.x, Student.x)
#
# Student.x = 0
# print(A.x, B.x, Student.x)

# class Teacher:
#     X = []
#
#
# A = Teacher()
# B = Teacher()
#
# print(A.X, B.X, Teacher.X)
# A.X = [0]
# print(A.X, B.X, Teacher.X)

# class Admin:
#     def __init__(self):
#         self.x = []
#
#
# A = Admin()
# B = Admin()
#
# print(A.x, B.x)
# A.x.append(1)
# print(A.x, B.x)


# class Student:
#     def __init__(self, x):
#         self.x = x
#
#     def increase_x(self, value):
#         self.x += value
#
#
# A = Student(7)
# A.increase_x(2)
# print(A.x)


# class Teacher:
#     def __init__(self):
#         self.__value = 0
#
#     def increment(self, x):
#         self.__value += x
#
#
# A = Teacher()
# A.increment(3)
# print(A.__dict__)


# class Teacher:
#     def __init__(self):
#         self._value = 0
#
#     def increment(self, x):
#         self._value += x


# A = Teacher()
# A.increment(3)
# print(A._value)

class Admin():
    def __init__(self):
        self.x = 0
        self.y = 7

    def get_salary(self):
        print("celebrate")

def func():
    print("oh no!")

# A = Admin()
# print(A.__dict__)
# print(Admin.__dict__)
#
# A.__dict__["get_fired"] = func
#
# A.get_fired()

S = func
S()
